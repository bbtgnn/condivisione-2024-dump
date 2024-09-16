#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 source_directory target_directory"
    exit 1
fi

# Assign the source and target directories to variables
SOURCE_DIR="$1"
TARGET_DIR="$2"

# Check if the source directory exists
if [ ! -d "$SOURCE_DIR" ]; then
    echo "Source directory does not exist: $SOURCE_DIR"
    exit 1
fi

# Check if the target directory exists, create it if it doesn't
if [ ! -d "$TARGET_DIR" ]; then
    mkdir -p "$TARGET_DIR"
fi

# Loop through all .gz files in the source directory
for file in "$SOURCE_DIR"/*.gz; do
    if [ -f "$file" ]; then
        # Get the base name of the file (without the .gz extension)
        base_name=$(basename "$file" .gz)
        
        # Decompress the file and save it to the target directory
        gunzip -c "$file" > "$TARGET_DIR/$base_name"
        
        echo "Decompressed: $file to $TARGET_DIR/$base_name"
    else
        echo "No .gz files found in $SOURCE_DIR"
        exit 0
    fi
done
