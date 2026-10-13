students = {


    "s101": {

        "name": "Rahim",
        "department": "CSE"
    },

     "s102": {
    
            "name": "Nadia",
            "department": "EEE"
        },
    
}
student_id = input("Enter student ID: ")
student = students.get(student_id)

if student is not None:
    print("student Name:", student.get("name", "Name not found"))
    print("student Department:", student.get("department", "Department not found"))
else:
    print("student not found!")