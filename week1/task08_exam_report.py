student_name = input("Enter your name: ")
python_score = float(input("Enter your python score: "))
english_score = float(input("Enter your english score: "))
maths_score = float(input("Enter your maths score: "))

average = (python_score + english_score + maths_score) / 3

print("========================================")
print("          STUDENT RESULT")
print("========================================")

print(f"Student: {student_name}")
print()
print(f"Python:       {python_score}")
print(f"English:      {english_score}")
print(f"Mathematics:  {maths_score}")
print("----------------------------------------")
print(f"Average:      {average}")
print("========================================")
