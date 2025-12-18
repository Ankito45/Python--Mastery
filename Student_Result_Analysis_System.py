students = [{'roll' : 101 , 'name' : "Ameet " , 'branch' : "CSE" , 'marks' : (78, 67, 89)} ,
{'roll' : 102 , 'name' : "Riyaa " , 'branch' : "CSE" , 'marks' : (88, 91, 76)} ,
{'roll' : 103 , 'name' : "Suman " , 'branch' : "ECE" , 'marks' : (92, 81, 74)} ,
{'roll' : 104 , 'name' : "Priya " , 'branch' : "EEE" , 'marks' : (65, 69, 72)} ,
{'roll' : 105 , 'name' : "Kunal " , 'branch' : "CSE" , 'marks' : (91, 73, 84)} ,
{'roll' : 106 , 'name' : "Meera " , 'branch' : "ME" , 'marks' : (58, 82, 55)} ,
{'roll' : 107 , 'name' : "Ameet " , 'branch' : "CSE" , 'marks' : (78, 67, 89)} ,
{'roll' : 108 , 'name' : "Diyaa " , 'branch' : "EEE" , 'marks' : (85, 81, 76)} ,
{'roll' : 109 , 'name' : "Rohan " , 'branch' : "ECE" , 'marks' : (37, 87, 70)} ,
{'roll' : 110 , 'name' : "Sriya " , 'branch' : "EEE" , 'marks' : (65, 66, 72)} ,
{'roll' : 111 , 'name' : "Kusal " , 'branch' : "ME" , 'marks' : (88, 73, 84)} ,
{'roll' : 112 , 'name' : "Manoj " , 'branch' : "ME" , 'marks' : (78, 73, 65)} ,]

print("="*70)
print(" "*15 + "STUDENT RESULT ANALYSIS SYSTEM")
print("="*70)

# Task 1 — Basic Display 
print("\n" + "="*70)
print("TASK 1 — BASIC DISPLAY")
print("="*70)

# Count how many student records are present in the given list by using list functions or basic iteration.
print("\nTotal number of student records:", len(students))

# Create a list that contains only the names of all students (Hints: extract the name value from each dictionary)
print("\nList of student names:")
# List comprehension to extract names using key 'name'
Student_names = [x['name'] for x in students]   
print(Student_names)

# Collect all roll numbers from the dataset and store them inside a tuple. Then print the tuple.
roll_num = tuple([x['roll'] for x in students])
print("\nTuple of roll numbers:", roll_num)

# Task 2: Augment Dataset Using Grades
print("\n" + "="*70)
print("TASK 2 — AUGMENT DATASET USING GRADES")
print("="*70)

new_AgumentData = []  # Copying the original list to avoid modifying it directly
# For each student, calculate total and percentage using list/tuple only.
for str in students:
    total_marks = sum(str['marks'])  # Sum of marks from the tuple
    percentage = (total_marks / 300) * 100  # Assuming each subject is out of 100
    
    # Augment the input data set by including an additional item (feature), Grade, for each student using their percentage
    match percentage:
        case percentage if percentage >= 90:
            grade = 'O'
        case percentage if percentage >= 80:
            grade = 'A'
        case percentage if percentage >= 70:
            grade = 'B'
        case percentage if percentage >= 60:
            grade = 'C'
        case percentage if percentage >= 50:
            grade = 'P'
        case _:
            grade = 'F'
    new_AgumentData.append({'total_marks': total_marks, 'percentage': percentage, 'grade': grade})
    print(f"Total Marks: {total_marks} of {str['name']}, Percentage: {percentage:.2f}%, Grade: {grade}")

# Given a roll number as input, write code to display that student's grade
roll_input = int(input("\nEnter the roll number: "))
for i in range(len(new_AgumentData)):
    if students[i]['roll'] == roll_input:
        print(f"Student Roll Number: {roll_input}, Grade: {new_AgumentData[i]['grade']}")
        break
else:
    print("Roll number not found.")

# Print all the students having a particular grade, inputted by user. (Hints: Ask the user for a grade
# (O/A/B/C/P/F) and print all students matching that grade.)
input_grade = input("\nEnter the grade to filter students (O/A/B/C/P/F): ").upper()
found = False
for i in range(len(new_AgumentData)):
    if new_AgumentData[i]['grade'] == input_grade:
        print(f"Student Name: {students[i]['name']}")
        found = True
if not found:
    print("No students with the specified grade.")

# Task 3 — Branch Analysis Using Sets
print("\n" + "="*70)
print("TASK 3 — BRANCH ANALYSIS USING SETS")
print("="*70)

# Create a set of all unique branches. (Hints: Extract branch values and store them in a set so that duplicates get removed.)
branches = set(students[i]['branch'] for i in range(len(students)))
print("\nUnique branches in the dataset:", branches)

# For each unique branch, count how many students belong to that branch.
for branch in branches:
    count = 0
    for i in range(len(students)):
        if students[i]['branch'] == branch:
            count += 1
    print(f"Number of students in branch {branch}: {count}")

# Display branch-wise student data using a dictionary of sets. Display a dictionary where:
# • Key = branch name
# • Value = set of roll numbers belonging to that branch
branch_wise = {}
for branch in branches:
    roll_num = {students[i]['roll'] for i in range(len(students)) if students[i]['branch'] == branch}
    branch_wise[branch] = roll_num        
print("\nBranch-wise data:", branch_wise)

# Task 4 — Toppers & Ranking
print("\n" + "="*70)
print("TASK 4 — TOPPERS & RANKING")
print("="*70)

# Identify overall topper of the institute. (Hints: Find the student with the highest percentage.)
Highest_index = 0
for i in range(1, len(new_AgumentData)):
    if new_AgumentData[i]['percentage'] > new_AgumentData[Highest_index]['percentage']:
        Highest_index = i
print(f"\nOverall Topper: {students[Highest_index]['name']} with Percentage: {new_AgumentData[Highest_index]['percentage']:.2f}%")

# Identify branch-wise topper of the institute. (Hints: For each branch (CSE, ECE, EEE, ME), find the student who has the highest percentage in that branch.)
highest_per_branch = {}
for branch in branches:
    highest_index = 0
    for i in range(len(students)):
        if students[i]['branch'] == branch:
            if highest_index == 0 or new_AgumentData[i]['percentage'] > new_AgumentData[highest_index]['percentage']:
                highest_index = i
    highest_per_branch[branch] = (students[highest_index]['name'], new_AgumentData[highest_index]['percentage'])
print("\nBranch-wise toppers:", highest_per_branch)

# Create a manually sorted list (bubble/selection sort) of names of the top 10 students of the institute by
# percentage in descending order. (N.B.: Do not use any built-in sort function.
sorted_students = students.copy() # done bcz we dont want to modify the original list
sorted_augmented = new_AgumentData.copy() # Also copy the augmented data
for i in range(len(sorted_students)):
    for j in range(0, len(sorted_students)-i-1):
        if sorted_augmented[j]['percentage'] < sorted_augmented[j+1]['percentage']:
            # this is used to swap the student names based on percentage
            sorted_students[j], sorted_students[j+1] = sorted_students[j+1], sorted_students[j]
            # this is imp because we are sorting based on percentage in descending order
            sorted_augmented[j], sorted_augmented[j+1] = sorted_augmented[j+1], sorted_augmented[j]
top_10_students = sorted_students[:10] # getting top 10 students data to a new list
print("\nTop 10 students by percentage:")
for i in range(len(top_10_students)):
    print(f"{i+1}. {top_10_students[i]['name']} - {sorted_augmented[i]['percentage']:.2f}%")

# Take roll number as input and display complete student details. If the roll number doesn't exist, print "Not Found".
Roll = int(input("\nEnter roll number to get details: "))
for i in range(len(students)):
    if students[i]['roll'] == Roll:
        print(f"\nDetails of Roll Number {Roll} --> ")
        print(f"Name: {students[i]['name']}")
        print(f"Branch: {students[i]['branch']}")
        print(f"Marks: {students[i]['marks']}")
        print(f"Total Marks: {new_AgumentData[i]['total_marks']}")
        print(f"Percentage: {new_AgumentData[i]['percentage']:.2f}%")
        print(f"Grade: {new_AgumentData[i]['grade']}")
        break
else:
    print("No Details Found")

# Task 5 — Data Correction
print("\n" + "="*70)
print("TASK 5 — DATA CORRECTION")
print("="*70)

# Given a dictionary of roll numbers and their corrected marks for each subject, update the original dataset accordingly.
correction_marks = {104: (70, 75, 80), 106: (92, 97, 97)}

print("\nApplying corrections...")
# ONLY do data correction if the roll number exists in the original dataset.
for roll_no, marks in correction_marks.items():
    for i in range(len(students)):
        if students[i]['roll'] == roll_no:
            old_marks = students[i]['marks']
            students[i]['marks'] = marks
            print(f"Roll {roll_no}: Marks changed from {old_marks} to {marks}")
            # After correction, recalculate the total marks, percentage and grades for the affected students.
            # UPDATE the existing new_AgumentData instead of creating new list
            total_marks = sum(students[i]['marks'])
            percentage = (total_marks / 300) * 100
            if percentage >= 90:
                grade = 'O'
            elif percentage >= 80:
                grade = 'A'
            elif percentage >= 70:
                grade = 'B'
            elif percentage >= 60:
                grade = 'C'
            elif percentage >= 50:
                grade = 'P'
            else:
                grade = 'F'
            # Update the existing new_AgumentData
            new_AgumentData[i]['total_marks'] = total_marks
            new_AgumentData[i]['percentage'] = percentage
            new_AgumentData[i]['grade'] = grade
            
            print(f"Updated - Total: {total_marks}, Percentage: {percentage:.2f}%, Grade: {grade}")

# Check whether the ranking list changes after changes in marks of the students in correction marks dictionary.
print("\n" + "-"*70)
print("UPDATED RANKINGS AFTER DATA CORRECTION")
print("-"*70)

# Create a combined list for sorting
combined_data = []
for i in range(len(students)):
    combined_data.append({
        'roll': students[i]['roll'],
        'name': students[i]['name'],
        'branch': students[i]['branch'],
        'percentage': new_AgumentData[i]['percentage'],
        'total_marks': new_AgumentData[i]['total_marks'],
        'grade': new_AgumentData[i]['grade']
})

# Bubble sort in descending order by percentage
# Use sorted function to sort by percentage in descending order
new_Ranks = sorted(combined_data, key=lambda x: x['percentage'], reverse=True)
# Print updated rankings
print("\nUpdated Top 10 Rankings:")
for i in range(min(10, len(new_Ranks))):
    print(f"{i+1}. {new_Ranks[i]['name']} (Roll: {new_Ranks[i]['roll']}) - {new_Ranks[i]['percentage']:.2f}%")

# Task 6 — Dictionary-Based Report
print("\n" + "="*70)
print("TASK 6 — DICTIONARY-BASED REPORT")
print("="*70)

# Find overall topper from updated data
overall_topper_name = new_Ranks[0]['name']

# Find branch-wise toppers from updated data
branch_topper_names = {}
for branch in branches:
    highest_percentage = -1
    topper_name = ""
    for i in range(len(students)):
        if students[i]['branch'] == branch:
            if new_AgumentData[i]['percentage'] > highest_percentage:
                highest_percentage = new_AgumentData[i]['percentage']
                topper_name = students[i]['name']
    branch_topper_names[branch] = topper_name

# Create the report dictionary
report = {
    "total_students": len(students),
    "branches": list(branches),
    "toppers": {
        "overall": overall_topper_name,
        "CSE": branch_topper_names.get("CSE", "N/A"),
        "ECE": branch_topper_names.get("ECE", "N/A"),
        "EEE": branch_topper_names.get("EEE", "N/A"),
        "ME": branch_topper_names.get("ME", "N/A")
    }
}

# Display the report in clean format
print("\n" + "="*70)
print(" "*22 + "INSTITUTE REPORT")
print("="*70)
print(f"\nTotal Students: {report['total_students']}")
print(f"Branches: {', '.join(report['branches'])}")
print("\n" + "-"*70)
print(" "*25 + "TOPPERS")
print("-"*70)
print(f"\nOverall Topper: {report['toppers']['overall']}")
print("\nBranch-wise Toppers:")
print(f"  CSE: {report['toppers']['CSE']}")
print(f"  ECE: {report['toppers']['ECE']}")
print(f"  EEE: {report['toppers']['EEE']}")
print(f"  ME:  {report['toppers']['ME']}")
print("\n" + "="*70)

# Task 7 — Display the below Structures
print("\n" + "="*70)
print("TASK 7 — DISPLAY REQUIRED STRUCTURES")
print("="*70)

# Create the following Python data structures from the processed dataset:
# 1. List of tuples → (roll, name, total, percentage)
list_of_tuples = [(students[i]['roll'], students[i]['name'], 
                   new_AgumentData[i]['total_marks'], new_AgumentData[i]['percentage']) 
                   for i in range(len(students))]
print("\n1. List of tuples (roll, name, total, percentage):")
for tup in list_of_tuples:
    print(f"   {tup}")

# 2. Create a dictionary mapping roll numbers to percentage. Dictionary → { roll : percentage } Example: {101: 78.2, 102: 85.6, ...}
roll_to_percentage = {students[i]['roll']: new_AgumentData[i]['percentage'] for i in range(len(students))}
print("\n2. Dictionary {roll: percentage}:")
print(f"   {roll_to_percentage}")

# 3. Set of all students scoring ≥ 75%. Add the names (or roll numbers) of students who have percentage >= 75.
students_above_75 = set(students[i]['name'] for i in range(len(students)) if new_AgumentData[i]['percentage'] >= 75)
print("\n3. Set of students scoring >= 75%:")
print(f"   {students_above_75}")

print("\n" + "="*70)
print(" "*15 + "ANALYSIS COMPLETED SUCCESSFULLY!")
print("="*70)