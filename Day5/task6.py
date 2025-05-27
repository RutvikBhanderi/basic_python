def sort_students(student_dict):
    return sorted(student_dict.keys())

students = {
    "Ravie": 20,
    "raj": 27,
    "jay": 28
}

print(list(sort_students(students)))  