# Function to create a dictionary with 5 key-value pairs (Student ID and Name)
def create_student_dict():
    students = {
        101: "Alice",
        102: "Bob",
        103: "Charlie",
        104: "David",
        105: "Eve"
    }
    return students

# Function to add a new student to the dictionary
def add_student(students, student_id, student_name):
    students[student_id] = student_name
    return students

# Function to update a student's name in the dictionary
def update_student_name(students, student_id, new_name):
    if student_id in students:
        students[student_id] = new_name
    return students

# Function to access a student's name by their ID
def get_student_name(students, student_id):
    return students.get(student_id, "Student not found")

# Function to create a nested dictionary (Student ID -> Name and Subjects)
def create_nested_dict():
    nested_students = {
        101: {"Name": "Alice", "Subjects": ["Math", "Science", "History"]},
        102: {"Name": "Bob", "Subjects": ["Math", "English"]},
        103: {"Name": "Charlie", "Subjects": ["Physics", "Chemistry"]},
        104: {"Name": "David", "Subjects": ["Math", "Biology"]},
        105: {"Name": "Eve", "Subjects": ["History", "Literature"]}
    }
    return nested_students

# Function to access a student's subjects from the nested dictionary
def get_student_subjects(nested_students, student_id):
    return nested_students.get(student_id, {}).get("Subjects", "No subjects found")

# Function to print all keys (student IDs) in the dictionary
def print_keys(dictionary):
    print("Keys in dictionary:", list(dictionary.keys()))

# Function to delete a student by ID from the dictionary
def delete_student(students, student_id):
    if student_id in students:
        del students[student_id]
    return students

# Main code to execute all operations
students = create_student_dict()
print("Initial Students Dictionary:", students)

# 1.1 Adding a student
students = add_student(students, 106, "Frank")
print("After Adding Student 106:", students)

# 1.2 Updating a student's name
students = update_student_name(students, 103, "Charles")
print("After Updating Student 103:", students)

# 1.3 Accessing a student's name
print("Student with ID 102:", get_student_name(students, 102))

# 1.4 Creating a nested dictionary
nested_students = create_nested_dict()

# 1.5 Accessing a student's subjects
print("Charlie's Subjects:", get_student_subjects(nested_students, 103))

# 1.6 Print the keys in the nested dictionary
print_keys(nested_students)

# 1.7 Deleting a student (ID 105)
students = delete_student(students, 105)
print("After Deleting Student 105:", students)
