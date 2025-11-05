#add and delete dictionary elements
student = {'name': 'Alice', 'age': 21, 'courses': ['Math', 'CompSci']}
print("Original student dictionary:", student)
student['age'] = 22
student['grade'] = 'A'
print("Updated student dictionary:", student)
del student['grade']
print("Dictionary after deleting grade:", student)
print("Length of dictionary:", len(student))
student.clear()
print("Dictionary after clearing:", student)