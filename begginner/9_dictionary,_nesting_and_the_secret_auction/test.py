student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

if 80 < student_scores['Harry'] < 91:
    print(f"{student_scores} Exceeds Expectations")

if 70 < student_scores['Ron'] < 81:
    print("Acceptable")

if 91 < student_scores['Hermione'] < 101:
    print(f"Outstanding")

if 70 < student_scores['Draco'] < 81:
    print(f"Acceptable")

if student_scores['Neville'] < 70:
    print(f"Fail")


