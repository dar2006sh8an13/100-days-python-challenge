#dictionary operations
student = {'name': 'Alice', 'age': 21, 'courses': ['Math', 'CompSci']}
print("name:", student['name'])
print("age:", student['age'])
print("courses:", student['courses'])
student['age'] = 22
student['grade'] = 'A'
print("Updated student dictionary:", student)
print("All keys:", student.keys())
print("All values:", student.values())
print("Items in dictionary:", student.items())
del student['grade']
print("Dictionary after deleting grade:", student)
print("Length of dictionary:", len(student))
student.clear()
print("Dictionary after clearing:", student)
                                