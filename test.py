class Student:
    def __init__(self, student_id, name):
        # Handle invalid inputs: ID and name not empty[cite: 7]
        if not student_id or not name:
            print("Error: Student ID and Name cannot be empty.")
        
        self.student_id = student_id
        self.name = name
        self.grades = []
        self.is_passed = False
        self.honor = False
        self.letter_grade = "F"

    def add_grade(self, grade):
        # Numeric grades in 0-100 range[cite: 7]
        if isinstance(grade, (int, float)):
            if 0 <= grade <= 100:
                self.grades.append(float(grade))
            else:
                print(f"Error: Grade {grade} is out of the 0-100 range.")
        else:
            print(f"Error: Invalid input. '{grade}' is not a numeric value.")

    def calc_average(self):
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def check_honor_and_status(self):
        # Update pass/fail and honor roll status based on average[cite: 7, 8]
        avg = self.calc_average()
        self.is_passed = avg >= 60  # Passed if 60 or higher[cite: 7]
        self.honor = avg >= 90      # Honor roll boolean flag[cite: 8]

        if avg >= 90:
            self.letter_grade = "A"
        elif avg >= 80:
            self.letter_grade = "B"
        elif avg >= 70:
            self.letter_grade = "C"
        elif avg >= 60:
            self.letter_grade = "D"
        else:
            self.letter_grade = "F"

    def remove_grade(self, identifier):
        # Remove by value or index with graceful error handling[cite: 8]
        if isinstance(identifier, int) and 0 <= identifier < len(self.grades):
            del self.grades[identifier]
        elif isinstance(identifier, (int, float)) and identifier in self.grades:
            self.grades.remove(identifier)
        else:
            print(f"Error: Could not remove grade. Index or value '{identifier}' not found.")

    def report(self):
        # Generate formatted summary report[cite: 8]
        self.check_honor_and_status()
        avg = self.calc_average()
        
        print("\n--- Student Summary Report ---")
        print(f"Student ID: {self.student_id}")
        print(f"Student Name: {self.name}")
        print(f"Number of Grades: {len(self.grades)}")
        print(f"Average Grade: {avg:.2f}")
        print(f"Letter Grade: {self.letter_grade}")
        print(f"Pass/Fail Status: {'Passed' if self.is_passed else 'Failed'}")
        print(f"Honor Roll: {self.honor}\n")


def main():
    # 1. Add student
    student1 = Student("S101", "Alex Smith")
    
    # 2. Add grades (testing valid and invalid inputs)
    student1.add_grade(95)
    student1.add_grade(85)
    student1.add_grade(150)     # Invalid range error
    student1.add_grade("Ten")   # Invalid type error
    student1.add_grade(92)
    
    # 3. Remove grade (testing value and index)
    student1.remove_grade(85)   # Removes by value
    student1.remove_grade(10)   # Invalid index error
    
    # 4. Generate report
    student1.report()

if __name__ == "__main__":
    main()