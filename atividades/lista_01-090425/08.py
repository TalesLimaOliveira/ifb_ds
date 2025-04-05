import numpy as np

# Lista de nomes dos alunos
students = np.array(["Ana", "Bruno", "Carla", "Daniel", "Eduarda", "Felipe", "Gabriel"])
# Notas correspondentes
grades = np.array([7.5, 5.0, 8.0, 6.0, 4.5, 9.0, 3.5])

# a
average_grade = np.mean(grades)
print(f"Média da turma: {average_grade:.2f}")

# b
max_grade = np.max(grades)
min_grade = np.min(grades)

students_max = students[grades == max_grade]
students_min = students[grades == min_grade]

print(f"Maior nota: {max_grade} - Aluno(s): {', '.join(students_max)}")
print(f"Menor nota: {min_grade} - Aluno(s): {', '.join(students_min)}")

# c
approved = students[grades >= 5.0]
approved_grades = grades[grades >= 5.0]

reproved = students[grades < 5.0]
reproved_grades = grades[grades < 5.0]

print("Alunos aprovados:")
for name, grade in zip(approved, approved_grades):
    print(f"{name}: {grade}")

print("\nAlunos reprovados:")
for name, grade in zip(reproved, reproved_grades):
    print(f"{name}: {grade}")
