# Lab 1: Grade Evaluator & Archiver

This project has two parts: a Python script that reads a student's grades from a CSV file and works out their final GPA and pass orfail status, and a Bash script that archives that CSV and resets it for the next batch.

## The files include:
- "grade-evaluator.py" – this python script reads grades.csv, validates it, calculates GPA and pass/fail, and shows which assignments need resubmission.
- "organizer.sh" – this shell script archives the current grades.csv with a timestamp and creates a new one, logging each run.

## How to run the Python script
Run this command:

python3 grade-evaluator.py

It will ask for a filename — type "grades.csv" and press enter. The CSV needs these columns: assignment, group, score, weight, where group is either Formative or Summative.


## How to run the shell script
First make it runnable:

chmod +x organizer.sh

Then run it:

./organizer.sh

Each time you run it, it archives grades.csv into the archive folder with a timestamp, creates a new empty grades.csv, and adds a line to organizer.log.
