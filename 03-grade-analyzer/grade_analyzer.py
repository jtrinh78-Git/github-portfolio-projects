def welcome():
    print("Welcome to Student Grade Analyzer!")

welcome() 

students = []

while True:
    print("Student Grade Analyzer")
    print("1. Add Student")
    print("2. View Students")
    print("3. View Average Grade")
    print("4. Highest Grade")
    print("5. Lowest Grade")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        student_name = input("Enter student name: ") 
        try:
          student_grade = float(input("Enter student grade: "))

          student = {
            "name": student_name,
            "grade": student_grade
        }
          students.append(student)

        except ValueError:
                print("Please enter a valid number.")

    elif choice == "2":
        if students:
            for number, student in enumerate(students, start=1):
                print(f'{number}. {student["name"]} - {student["grade"]:.2f}')
        else:
                print("No students yet.")

    elif choice == "3":
       if students:
        total = 0

        for student in students:
            total = total + student["grade"]

        average = total / len(students)
        print(f"Average Grade: {average:.2f}")

       else:
        print("No students yet.")

    elif choice == "4":
         if students:
              highest_student = max(students, key=lambda student: student["grade"]) 
              print(f'Highest Grade: {highest_student["name"]} - {highest_student["grade"]:.2f}')

         else:
          print("No students yet")

    elif choice == "5":
          if students:
               lowest_student = min(students, key=lambda student: student["grade"])
               print(f'Lowest Grade: {lowest_student["name"]} - {lowest_student["grade"]:.2f}')

          else:
            print("No students yet")

    elif choice == "6":
         print("Good bye! Have a great day!")
         break 

    else:
        print("Please choose a valid number 1-6." )


