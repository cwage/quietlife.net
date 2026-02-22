#!/bin/bash
# Import Disqus XML export into staticomment YAML format.
#
# Usage:
#   ./scripts/import_disqus.sh <path-to-disqus-export.xml.gz> [--dry-run]
#
# The export file is mounted read-only into the container.
# Output goes to _data/comments/ in the repo.

set -euo pipefail

if [ $# -lt 1 ]; then
    echo "Usage: $0 <disqus-export.xml[.gz]> [--dry-run]"
    exit 1
fi

EXPORT_FILE="$(realpath "$1")"
shift

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
OUTPUT_DIR="$REPO_DIR/_data/comments"

mkdir -p "$OUTPUT_DIR"

docker build -t disqus-import -f "$REPO_DIR/scripts/Dockerfile.disqus-import" "$REPO_DIR"

docker run --rm \
    -v "$OUTPUT_DIR:/work/_data/comments" \
    -v "$EXPORT_FILE:/import/export.xml.gz:ro" \
    -u "$(id -u):$(id -g)" \
    disqus-import \
    /import/export.xml.gz "$@"
