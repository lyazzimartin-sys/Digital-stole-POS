#a student academic system
students = {
    "2026001":{"name":"martin", "course": "bict":, "marks":82},
    "2026002":{"name":"elija", "course": "cs":, "marks":95},
    "2026003":{"name":"jolie", "course": "cm":, "marks":72},
    "2026004":{"name":"john", "course": "sw":, "marks":80},
    "2026005":{"name":"douglas", "course": "theo":, "marks":68},

}
#display a student record based on on thier reg number
def display_student_record(regestration_number):
    student=student.get(regestration_number)
    if student:
        print(f"regestration number :{regestration_number}")
        print(f"name: {student['name']}")
        print(f"course:{student['course']}")
        print(f"marks: {student['marks']}")

    else:
        print("student not found.")

#tell th e user to input and show results
reg_no = input("enter registration number:")
display_student_record(reg_no)

print("\n---all students summary---")
for reg, data in studens.items():
    print(f"{reg} - {data['name']} ({data['course']}): {data['marks']}")
