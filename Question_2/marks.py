import os

FILE_NAME = "student.txt"


class Student:
    def __init__(self, rollno, name, m1, m2, m3, m4, m5):
        self.rollno = rollno
        self.name = name
        self.marks1 = m1
        self.marks2 = m2
        self.marks3 = m3
        self.marks4 = m4
        self.marks5 = m5
        self.totalmarks = m1 + m2 + m3 + m4 + m5

    def to_line(self):
        return f"{self.rollno},{self.name},{self.marks1},{self.marks2},{self.marks3},{self.marks4},{self.marks5},{self.totalmarks}\n"

    @staticmethod
    def from_line(line):
        data = line.strip().split(",")
        return Student(
            int(data[0]),
            data[1],
            int(data[2]),
            int(data[3]),
            int(data[4]),
            int(data[5]),
            int(data[6])
        )


def add_student():
    name = input("enter name: ")
    rollno = int(input("enter rollno: "))

    m1 = int(input("enter marks1: "))
    m2 = int(input("enter marks2: "))
    m3 = int(input("enter marks3: "))
    m4 = int(input("enter marks4: "))
    m5 = int(input("enter marks5: "))

    student = Student(rollno, name, m1, m2, m3, m4, m5)

    with open(FILE_NAME, "a") as f:
        f.write(student.to_line())

    print("student added successfully...")


def update_marks():
    roll_no = int(input("\nenter rollno to update: "))
    found = False
    students = []

    if not os.path.exists(FILE_NAME):
        print("No records found.")
        return

    with open(FILE_NAME, "r") as f:
        for line in f:
            st = Student.from_line(line)
            if st.rollno == roll_no:
                found = True
                print("enter the new set of marks")
                st.marks1 = int(input("enter marks1: "))
                st.marks2 = int(input("enter marks2: "))
                st.marks3 = int(input("enter marks3: "))
                st.marks4 = int(input("enter marks4: "))
                st.marks5 = int(input("enter marks5: "))
                st.totalmarks = (
                    st.marks1 + st.marks2 + st.marks3 + st.marks4 + st.marks5
                )
            students.append(st)

    with open(FILE_NAME, "w") as f:
        for st in students:
            f.write(st.to_line())

    if found:
        print("\nMarks updated successfully...")
    else:
        print("\nStudent not found...")


def display():
    print("\n---Student details----")
    print(
        f"{'Rollno':<10}{'Name':<20}{'Sub1':<10}{'Sub2':<10}{'Sub3':<10}"
        f"{'Sub4':<10}{'Sub5':<10}{'Total':<10}"
    )

    if not os.path.exists(FILE_NAME):
        print("No records to display.")
        return

    with open(FILE_NAME, "r") as f:
        for line in f:
            st = Student.from_line(line)
            print(
                f"{st.rollno:<10}{st.name:<20}{st.marks1:<10}{st.marks2:<10}"
                f"{st.marks3:<10}{st.marks4:<10}{st.marks5:<10}{st.totalmarks:<10}"
            )


def teacher():
    print("\n1. add student")
    print("2. update marks")
    print("3. display marks")
    val = int(input("enter choice: "))

    if val == 1:
        add_student()
    elif val == 2:
        update_marks()
    elif val == 3:
        display()
    else:
        print("invalid input")


def student():
    display()


def main():
    while True:
        print("\n1. teacher")
        print("2. student")
        print("0. exit")
        val = int(input("enter choice: "))

        if val == 1:
            teacher()
        elif val == 2:
            student()
        elif val == 0:
            break
        else:
            print("invalid input")


if __name__ == "__main__":
    main()
