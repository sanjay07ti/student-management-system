students = {}

def add_student():
    roll_no = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    students[roll_no] = name
    print("Student added successfully!")

def view_students():
    if not students:
        print("No student records found.")
    else:
        print("\nStudent Records:")
        for roll_no, name in students.items():
            print(f"Roll No: {roll_no}, Name: {name}")

def delete_student():
    roll_no = input("Enter Roll Number to delete: ")
    
    if roll_no in students:
        del students[roll_no]
        print("Student deleted successfully!")
    else:
        print("Student not found.")

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_student()

    elif choice == '2':
        view_students()

    elif choice == '3':
        delete_student()

    elif choice == '4':
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")
