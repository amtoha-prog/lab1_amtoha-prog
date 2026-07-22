import csv
import sys
import os

def load_csv_data():
    """
    Prompts the user for a filename, checks if it exists, 
    and extracts all fields into a list of dictionaries.
    """
    filename = input("Enter the name of the CSV file to process (e.g., grades.csv): ")
    
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
        
    assignments = []
    
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert numeric fields to floats for calculations
                assignments.append({
                    'assignment': row['assignment'],
                    'group': row['group'],
                    'score': float(row['score']),
                    'weight': float(row['weight'])
                })
        return assignments
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)

def evaluate_grades(data):
    """
    Implement your logic here.
    'data' is a list of dictionaries containing the assignment records.
    """
    print("\n--- Processing Grades ---")
    
    # TODO: a) Check if all scores are percentage based (0-100)
    for assignment in data:
        score = assignment['score']
        if score < 0 or score > 100:
            print(f"Error: '{assignment['assignment']}' has an invalid score of {score}.")
            sys.exit(1)


    # TODO: b) Validate total weights (Total=100, Summative=40, Formative=60)
    # Spliting first the category to formative and summative 
    formative_list = []
    summative_list = []

    for assignment in data:
        if assignment['group'] == 'Formative':
            formative_list.append(assignment)
        elif assignment['group'] == 'Summative':
            summative_list.append(assignment)
# Adding weight for total weight, then each category on it own.
    total_weight = 0
    for assignment in data:
        total_weight += assignment['weight']

    formative_weight = 0
    for assignment in formative_list:
        formative_weight += assignment['weight']

    summative_weight = 0
    for assignment in summative_list:
        summative_weight += assignment['weight']

    # If grades excced the write grades print an error
    if total_weight != 100:
        print(f"Error: The total weight is {total_weight}, it must be exactly 100.")
        sys.exit(1)

    if formative_weight != 60:
        print(f"Error: The formative weight is {formative_weight}, it must be exactly 60.")
        sys.exit(1)

    if summative_weight != 40:
        print(f"Error: The summative weight is {summative_weight}, it must be exactly 40.")
        sys.exit(1)

    # TODO: c) Calculate the Final Grade and GPA
    # 
    total_grade = 0
    for assignment in data:
        weight_score = assignment['score'] * assignment['weight'] / 100
        total_grade += weight_score

    # converting the total grrade out of 100 into GPA out of 5.0
    gpa = (total_grade / 100) * 5.0

    # TODO: d) Determine Pass/Fail status (>= 50% in BOTH categories)
    # TODO: e) Check for failed formative assignments (< 50%)
    #          and determine which one(s) have the highest weight for resubmission.
    # TODO: f) Print the final decision (PASSED / FAILED) and resubmission options
    
    pass

if __name__ == "__main__":
    # 1. Load the data
    course_data = load_csv_data()
    
    # 2. Process the features
    evaluate_grades(course_data)