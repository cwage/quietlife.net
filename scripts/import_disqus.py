#!/usr/bin/env python3
"""Import Disqus XML export into staticomment YAML format.

Reads a Disqus XML export (optionally gzipped) and generates per-comment
YAML files compatible with https://github.com/cwage/staticomment.

Output structure:
    _data/comments/<slug>/<timestamp>-<random>.yml
"""

import argparse
import gzip
import os
import random
import sys
import xml.etree.ElementTree as ET
from datetime import datetime
from urllib.parse import urlparse

import markdownify
import yaml


def literal_str_representer(dumper, data):
    """Use literal block style (|) for multiline strings."""
    if "\n" in data:
        return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)


yaml.add_representer(str, literal_str_representer)


DISQUS_NS = "http://disqus.com"
DISQUS_INTERNAL_NS = "http://disqus.com/disqus-internals"

NS = {
    "d": DISQUS_NS,
    "dsq": DISQUS_INTERNAL_NS,
}


def parse_xml(path):
    """Parse the Disqus XML export, handling gzip transparently."""
    if path.endswith(".gz"):
        with gzip.open(path, "rb") as f:
            return ET.parse(f)
    else:
        return ET.parse(path)


def url_to_slug(url):
    """Convert a Disqus thread URL to a staticomment slug.

    Example:
        http://quietlife.net/2001/07/13/hi-this-is-my-first/
        -> 2001-07-13-hi-this-is-my-first
    """
    parsed = urlparse(url)
    path = parsed.path.strip("/")
    return path.replace("/", "-")


def html_to_markdown(html):
    """Convert Disqus comment HTML to Markdown."""
    if not html or not html.strip():
        return ""
    md = markdownify.markdownify(html, strip=["img"])
    # Clean up excessive blank lines and trailing whitespace
    # (trailing spaces prevent YAML literal block style)
    lines = md.split("\n")
    cleaned = []
    prev_blank = False
    for line in lines:
        stripped = line.rstrip()
        is_blank = stripped == ""
        if is_blank and prev_blank:
            continue
        cleaned.append(stripped)
        prev_blank = is_blank
    return "\n".join(cleaned).strip()


def generate_filename(date_str):
    """Generate a staticomment-compatible filename from a date string.

    Format: YYYYMMDDHHmmss-<8 hex chars>
    """
    dt = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
    timestamp = dt.strftime("%Y%m%d%H%M%S")
    rand_hex = format(random.randint(0, 0xFFFFFFFF), "08x")
    return f"{timestamp}-{rand_hex}"


def text(element, tag):
    """Get text content of a child element, or empty string."""
    child = element.find(f"d:{tag}", NS)
    if child is not None and child.text:
        return child.text.strip()
    return ""


def main():
    parser = argparse.ArgumentParser(description="Import Disqus XML to staticomment YAML")
    parser.add_argument("xml_file", help="Path to Disqus XML export (may be .gz)")
    parser.add_argument(
        "-o", "--output-dir",
        default="_data/comments",
        help="Output directory (default: _data/comments)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Parse and report stats without writing files",
    )
    args = parser.parse_args()

    print(f"Parsing {args.xml_file}...")
    tree = parse_xml(args.xml_file)
    root = tree.getroot()

    # --- Pass 1: Build thread map (dsq:id -> slug) ---
    threads = {}
    deleted_threads = set()
    for thread_el in root.findall("d:thread", NS):
        dsq_id = thread_el.get(f"{{{DISQUS_INTERNAL_NS}}}id")
        link = text(thread_el, "link")
        is_deleted = text(thread_el, "isDeleted").lower() == "true"

        if is_deleted:
            deleted_threads.add(dsq_id)
            continue

        if link:
            threads[dsq_id] = url_to_slug(link)

    print(f"Threads: {len(threads)} active, {len(deleted_threads)} deleted")

    # --- Pass 2: Parse all posts, generate filenames ---
    posts = []
    stats = {
        "total": 0,
        "deleted": 0,
        "spam": 0,
        "orphan_thread": 0,
        "empty_body": 0,
        "imported": 0,
    }
    # Map Disqus post dsq:id -> generated filename (for threading)
    post_id_to_filename = {}

    for post_el in root.findall("d:post", NS):
        stats["total"] += 1
        dsq_id = post_el.get(f"{{{DISQUS_INTERNAL_NS}}}id")

        is_deleted = text(post_el, "isDeleted").lower() == "true"
        if is_deleted:
            stats["deleted"] += 1
            continue

        is_spam = text(post_el, "isSpam").lower() == "true"
        if is_spam:
            stats["spam"] += 1
            continue

        # Get thread reference
        thread_ref = post_el.find("d:thread", NS)
        thread_id = thread_ref.get(f"{{{DISQUS_INTERNAL_NS}}}id") if thread_ref is not None else None

        if thread_id in deleted_threads:
            stats["deleted"] += 1
            continue

        if thread_id not in threads:
            stats["orphan_thread"] += 1
            continue

        slug = threads[thread_id]

        # Get message body
        message_html = text(post_el, "message")
        body = html_to_markdown(message_html)
        if not body:
            stats["empty_body"] += 1
            continue

        # Get author name
        author_el = post_el.find("d:author", NS)
        name = ""
        email = ""
        if author_el is not None:
            name = text(author_el, "name")
            email_el = author_el.find(f"d:email", NS)
            if email_el is not None and email_el.text:
                email = email_el.text.strip()

        if not name:
            name = "Anonymous"

        # Get date
        created_at = text(post_el, "createdAt")
        if not created_at:
            continue

        # Get parent reference (for threading)
        parent_el = post_el.find("d:parent", NS)
        parent_dsq_id = None
        if parent_el is not None:
            parent_dsq_id = parent_el.get(f"{{{DISQUS_INTERNAL_NS}}}id")

        # Generate filename
        filename = generate_filename(created_at)
        post_id_to_filename[dsq_id] = filename

        posts.append({
            "dsq_id": dsq_id,
            "name": name,
            "email": email,
            "body": body,
            "date": created_at,
            "slug": slug,
            "parent_dsq_id": parent_dsq_id,
            "filename": filename,
        })

    # --- Pass 3: Resolve threading ---
    resolved_replies = 0
    unresolved_replies = 0
    for post in posts:
        if post["parent_dsq_id"]:
            parent_filename = post_id_to_filename.get(post["parent_dsq_id"])
            if parent_filename:
                post["reply_to"] = parent_filename
                resolved_replies += 1
            else:
                # Parent was filtered (spam/deleted) — import as top-level
                unresolved_replies += 1

    # --- Write YAML files ---
    if not args.dry_run:
        for post in posts:
            slug_dir = os.path.join(args.output_dir, post["slug"])
            os.makedirs(slug_dir, exist_ok=True)

            comment = {
                "name": post["name"],
                "body": post["body"],
                "date": post["date"],
                "slug": post["slug"],
            }
            if post.get("email"):
                comment["email"] = post["email"]
            if post.get("reply_to"):
                comment["reply_to"] = post["reply_to"]

            filepath = os.path.join(slug_dir, f"{post['filename']}.yml")
            with open(filepath, "w") as f:
                yaml.dump(
                    comment,
                    f,
                    default_flow_style=False,
                    allow_unicode=True,
                    sort_keys=False,
                )

    stats["imported"] = len(posts)

    # --- Summary ---
    print("\n--- Import Summary ---")
    print(f"Total posts in export:   {stats['total']}")
    print(f"Deleted (post+thread):   {stats['deleted']}")
    print(f"Spam:                    {stats['spam']}")
    print(f"Orphan threads:          {stats['orphan_thread']}")
    print(f"Empty body:              {stats['empty_body']}")
    print(f"Imported:                {stats['imported']}")
    print(f"Threaded replies:        {resolved_replies} resolved, {unresolved_replies} unresolved (parent filtered)")

    if not args.dry_run:
        # Count unique slugs
        slugs = set(p["slug"] for p in posts)
        print(f"Posts with comments:     {len(slugs)}")
        print(f"Output directory:        {args.output_dir}")
    else:
        print("\n(dry run — no files written)")


if __name__ == "__main__":
    main()
