class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.scores = {}

    def add_score(self, subject, score):
        self.scores[subject] = score

    def get_average_score(self):
        total_score = sum(self.scores.values())
        num_subjects = len(self.scores)
        average_score = total_score / num_subjects
        return average_score


def main():
    students = []

    while True:
        print("\n1. Add student")
        print("2. Add score for a student")
        print("3. Calculate average score for a student")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            name = input("Enter student name: ")
            student_id = input("Enter student ID: ")
            student = Student(name, student_id)
            students.append(student)
            print("Student added successfully!")

        elif choice == "2":
            if not students:
                print("No students found. Please add a student first.")
                continue

            print("\nSelect a student:")

            for i, student in enumerate(students):
                print(f"{i+1}. {student.name}")

            student_choice = int(input("Enter student number (1-{}): ".format(len(students))))

            if student_choice < 1 or student_choice > len(students):
                print("Invalid student number.")
                continue

            selected_student = students[student_choice - 1]

            subject = input("Enter subject name: ")
            score = float(input("Enter score for {}: ".format(subject)))

            selected_student.add_score(subject, score)
            print("Score added successfully!")

        elif choice == "3":
            if not students:
                print("No students found. Please add a student first.")
                continue

            print("\nSelect a student:")

            for i, student in enumerate(students):
                print(f"{i+1}. {student.name}")

            student_choice = int(input("Enter student number (1-{}): ".format(len(students))))

            if student_choice < 1 or student_choice > len(students):
                print("Invalid student number.")
                continue

            selected_student = students[student_choice - 1]
            average_score = selected_student.get_average_score()
            print("Average score for {} is: {:.2f}".format(selected_student.name, average_score))

        elif choice == "4":
            print("Exiting program...")
            break

        else            print("Invalid choice. Please enter a number from 1 4.")


if __name__ == "__main__":
    main()
