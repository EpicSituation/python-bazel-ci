#!/bin/bash
set -e  # Exit immediately if a command fails

# Install pylint if not already installed
pip install pylint

# Get Bazel's execution environment path
PROJECT_ROOT=$(pwd)

# Locate source and test files in Bazel's sandbox environment
SRC_DIR="$PROJECT_ROOT/src"
TESTS_DIR="$PROJECT_ROOT/tests"

# Check if directories exist before running pylint
if [ -d "$SRC_DIR" ] && [ -d "$TESTS_DIR" ]; then
    echo "FILE FOUND"
    pylint $(find "$SRC_DIR" "$TESTS_DIR" -name "*.py") --fail-under=8.0
else
    echo "No files to lint: exiting."
    exit 0
fi
