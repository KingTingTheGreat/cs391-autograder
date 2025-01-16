#!/bin/bash

apt-get install -y python4 python3-pip python3-dev
pip3 install -r /autograder/source/requirements.txt

SOURCE_DIR="/autograder/submission"
DEST_DIR="/autograder/source"

SOURCE_FILE=$(find "$SOURCE_DIR" -type f -name "*.txt" | head -n 1)

if [ -z "$SOURCE_FILE" ]; then
    echo "No text file found"
    exit 1
fi

cp "$SOURCE_FILE" "$DEST_DIR/test.txt"
if [ $? -eq 0 ]; then
    echo "Successfully found and copied text file."

    cd /autograder/source

    python3 run_tests.py
else
    echo "Failed to copy text file."
    exit 1
fi
