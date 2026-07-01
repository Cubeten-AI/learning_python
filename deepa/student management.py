students = []

def add_student():
    roll = input("Enter roll number: ")
    name = input("Enter name: ")
    marks = float(input("Enter marks: "))
    students.append({"roll": roll, "name": name, "marks": marks})
    print("Student added successfully!")

def display_students():
    if not students:
        print("No students to display.")
        return
    print("\n--- Student List ---")
    for s in students:
        print(f"Roll: {s['roll']}, Name: {s['name']}, Marks: {s['marks']}")

def search_student():
    roll = input("Enter roll number to search: ")
    for s in students:
        if s['roll'] == roll:
            print(f"Found: Roll: {s['roll']}, Name: {s['name']}, Marks: {s['marks']}")
            return
    print("Student not found.")

def update_student():
    roll = input("Enter roll number to update: ")
    for s in students:
        if s['roll'] == roll:
            s['name'] = input("Enter new name: ")
            s['marks'] = float(input("Enter new marks: "))
            print("Student updated!")
            return
    print("Student not found.")

def delete_student():
    roll = input("Enter roll number to delete: ")
    for s in students:
        if s['roll'] == roll:
            students.remove(s)
            print("Student deleted!")
            return
    print("Student not found.")

def calculate_average():
    if not students:
        print("No students to calculate average.")
        return
    total = sum(s['marks'] for s in students)
    avg = total / len(students)
    print(f"Class average: {avg:.2f}")

def find_topper():
    if not students:
        print("No students available.")
        return
    topper = max(students, key=lambda x: x['marks'])
    print(f"Topper: {topper['name']} with {topper['marks']} marks")

def save_to_file():
    with open("students.txt", "w") as f:
        for s in students:
            f.write(f"{s['roll']},{s['name']},{s['marks']}\n")
    print("Data saved to students.txt")

def menu():
    while True:
        print("\n========== Student Management =========")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Calculate Average")
        print("7. Find Topper")
        print("8. Save")
        print("9. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '1': add_student()
        elif choice == '2': display_students()
        elif choice == '3': search_student()
        elif choice == '4': update_student()
        elif choice == '5': delete_student()
        elif choice == '6': calculate_average()
        elif choice == '7': find_topper()
        elif choice == '8': save_to_file()
        elif choice == '9': 
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

menu()