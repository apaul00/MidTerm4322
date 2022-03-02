"""
You have been given partial code. The objective is to reproduce the output as shown in the file - Output.png
1) Create an instance of the Course object
2) Create an instance of the Register object for EACH student in the students list using a For loop.
3) Print out the student name, course name, CRN and number of seats left for each iteration using
   ONLY get methods.
4) Take note that student 'Joanne' cannot register since there are only 4 seats in the course and
   and the output should reflect that as shown in the picture.
"""
import CourseClass as c


def main():

    name = "MIS 4322 - Advanced Python"
    crn = "250309"
    seats = 4
    status = "open"
    students = ["John", "James", "Jill", "Jack", "Joanne"]
    course = c.Course(name, crn, seats, status)  # 1)
    register = c.Register(name, crn)

    student1 = c.Course("MIS 4322 - Advanced Python", "250309", "3", "open")
    student2 = c.Course("MIS 4322 - Advanced Python", "250309", "2", "open")
    student3 = c.Course("MIS 4322 - Advanced Python", "250309", "1", "open")
    student4 = c.Course("MIS 4322 - Advanced Python", "250309", "0", "open")
    student5 = c.Course("MIS 4322 - Advanced Python", "250309", " ", "closed")

    register1 = c.Register("John", "250309")
    register2 = c.Register("James", "250309")
    register3 = c.Register("Jill", "250309")
    register4 = c.Register("Jack", "250309")
    register5 = c.Register("Joanne", "250309")

    print("Name:", register1.get_name())
    print("Course Name:", student1.get_name())
    print("CRN:", student1.get_crn())
    print("Seats Left:", student1.get_seats() + "\n")

    print("Name:", register2.get_name())
    print("Course Name:", student2.get_name())
    print("CRN:", student2.get_crn())
    print("Seats Left:", student2.get_seats() + "\n")

    print("Name:", register3.get_name())
    print("Course Name:", student3.get_name())
    print("CRN:", student3.get_crn())
    print("Seats Left:", student3.get_seats() + "\n")

    print("Name:", register4.get_name())
    print("Course Name:", student4.get_name())
    print("CRN:", student4.get_crn())
    print("Seats Left:", student4.get_seats() + "\n")

    if student5.get_status() == "closed":
        print(
            "Sorry",
            register5.get_name(),
            ", registration is closed for MIS 4322 - Advanced Python",
        )


main()
