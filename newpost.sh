#!/bin/bash

# Usage: ./newpost.sh my-post-slug
# Creates a new Jekyll post with today's date and the given slug

if [ -z "$1" ]; then
    echo "Usage: $0 <post-slug>"
    echo "Example: $0 my-awesome-post"
    exit 1
fi

SLUG="$1"
DATE=$(date +%Y-%m-%d)
FILENAME="_posts/${DATE}-${SLUG}.md"

if [ -f "$FILENAME" ]; then
    echo "Error: $FILENAME already exists"
    exit 1
fi

cat > "$FILENAME" << EOF
---
title: ${SLUG}
author: cwage
layout: post
permalink: /${DATE//-/\/}/${SLUG}
categories:
  - Uncategorized
tags:
  -
---

EOF

echo "Created $FILENAME"
