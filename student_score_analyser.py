# Program to manage and analyze student scores

# 1. List of dictionaries storing student information
students = [
    {"name": "Ama", "Maths": 78, "Science": 82, "English": 74},
    {"name": "Kojo", "Maths": 65, "Science": 59, "English": 72},
    {"name": "Esi", "Maths": 90, "Science": 88, "English": 91},
]

# 2. Calculate average for each student using a loop
for student in students:
    maths_score = student["Maths"]
    science_score = student["Science"]
    english_score = student["English"]

    # Calculate average score
    average = (maths_score + science_score + english_score) / 3

    # Store the new value using update()
    student.update({"Average": average})

# 3. Print student results neatly using f-strings
for student in students:
    print(f"{student['name']} – Maths: {student['Maths']}, "
          f"Science: {student['Science']}, English: {student['English']} "
          f"→ Average: {student['Average']:.2f}")

# 5. Determine the student with the highest average
top_student = max(students, key=lambda s: s["Average"])

print("\nStudent with the highest average score:")
print(f"{top_student['name']} → {top_student['Average']:.2f}")
