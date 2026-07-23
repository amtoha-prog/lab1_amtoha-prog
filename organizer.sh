#!/bin/bash

ARCHIVE_DIR="archive"
LOG_FILE="organizer.log"
SOURCE_FILE="grades.csv"

# Checks if the archive folder exists yet if not creates it 
if [ ! -d "$ARCHIVE_DIR" ]; then
    mkdir "$ARCHIVE_DIR"
    echo "Created archive directory."
fi


# If grades.csv is missing there is nothing to archive
if [ ! -f "$SOURCE_FILE" ]; then
    echo "Error: '$SOURCE_FILE' not found. Nothing to archive."
    exit 1
fi
# A timestamp generated so archived files don't overwrite each other
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
ARCHIVED_NAME="grades_${TIMESTAMP}.csv"

# Moving the original file into the archive with its new timestamped name
mv "$SOURCE_FILE" "$ARCHIVE_DIR/$ARCHIVED_NAME"

# Creating a new, empty grades.csv
touch "$SOURCE_FILE"

# Appending the archive details into a log file
echo "$TIMESTAMP: archived $SOURCE_FILE as $ARCHIVE_DIR/$ARCHIVED_NAME" >> "$LOG_FILE"
echo "Done! Your grades have been safely archived, and a fresh grades.csv is ready to use."
