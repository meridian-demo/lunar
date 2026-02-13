#!/bin/bash
set -e

version=$("$LUNAR_CI_COMMAND_BIN_DIR/$LUNAR_CI_COMMAND_BIN" -version 2>&1 | grep -oE '[0-9]+\.[0-9]+\.[0-9]+' | head -1 || true)

if [[ -n "$version" ]]; then
    echo "{\"cmds\":[{\"cmd\":$LUNAR_CI_COMMAND,\"version\":\"$version\"}]}" | \
        lunar collect -j ".lang.java.native.ant.cicd" -
fi
