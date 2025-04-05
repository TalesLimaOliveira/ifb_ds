# a
class1 = [
    {"name": "Ana", "age": 14},
    {"name": "Bruno", "age": 15},
    {"name": "Carla", "age": 14}
]

class2 = [
    {"name": "Daniel", "age": 13},
    {"name": "Eduarda", "age": 14},
    {"name": "Felipe", "age": 13}
]

# b
new_student = {"name": "Gabriel", "age": 15}
class1.append(new_student)

# c
student_to_remove = "Carla"
class1 = [student for student in class1 if student["name"] != student_to_remove]

# d
print("Alunos da turma 1:")
for student in class1:
    print(f"Nome: {student['name']}, Idade: {student['age']}")