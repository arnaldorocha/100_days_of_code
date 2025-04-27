# student_scores = {
#     "Alice": 85,
#     "Bob": 78,
#     "Charlie": 92,
#     "David": 88,
#     "Eva": 95,
#     }


import random


names = ["Alice", "Bob", "Charlie", "David", "Eva"]
student_scores = {name: random.randint(50, 100) for name in names}

passed_students = {name: score for name, score in student_scores.items() if score >= 60}

print("Student Scores:", student_scores)
print("Passed Students:", passed_students)