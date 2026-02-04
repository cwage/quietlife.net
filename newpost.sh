#!/bin/bash

# Usage: ./newpost.sh my-post-slug
# Creates a new Jekyll post with today's date and the given slug

if [ -z "$1" ]; then
    echo "Usage: $0 <post-slug>"
    echo "Example: $0 my-awesome-post"
    exit 1
fi

SLUG="$1"

# Validate slug: only allow alphanumeric characters and hyphens
if ! [[ "$SLUG" =~ ^[A-Za-z0-9-]+$ ]]; then
    echo "Error: invalid slug '$SLUG'"
    echo "Slug may only contain letters, numbers, and hyphens."
    exit 1
fi

DATE=$(date +%Y-%m-%d)
FILENAME="_posts/${DATE}-${SLUG}.md"

if [ -f "$FILENAME" ]; then
    echo "Error: $FILENAME already exists"
    exit 1
fi

# Find the highest post_id and increment
MAX_POST_ID=$(grep -h "^post_id:" _posts/*.md 2>/dev/null | sed 's/post_id: //' | sort -n | tail -1)
POST_ID=$((MAX_POST_ID + 1))

cat > "$FILENAME" << EOF
---
post_id: ${POST_ID}
title: ${SLUG}
author: cwage
layout: post
guid: http://quietlife.net/?p=${POST_ID}
permalink: /${DATE//-/\/}/${SLUG}
categories:
  - Uncategorized
tags:
  -
---

EOF

echo "Created $FILENAME"
