#!/bin/bash
set -e

# Auto-detect bind-mount owner so the same image works on both
# root-mode Docker (UID 1000 = host user) and rootless Docker
# (UID 0 = host user via namespace remapping).

MOUNT_UID=$(stat -c '%u' /workspaces/quietlife.net)
MOUNT_GID=$(stat -c '%g' /workspaces/quietlife.net)

if [ "$MOUNT_UID" = "0" ]; then
    # Rootless Docker: container root IS the host user, run directly
    exec "$@"
else
    # Root Docker: drop privileges to match bind-mount owner
    if ! getent group "$MOUNT_GID" >/dev/null 2>&1; then
        groupadd -g "$MOUNT_GID" hostgroup
    fi
    if ! id "$MOUNT_UID" >/dev/null 2>&1; then
        useradd -u "$MOUNT_UID" -g "$MOUNT_GID" -m -s /bin/bash hostuser
    fi
    exec gosu "$MOUNT_UID:$MOUNT_GID" "$@"
fi
