# students_scores = input("enter students scores, separated by space: ").split()
import math

students_scores = [10, 20, 100, 5, 90]

min_score = max_score = int(students_scores[0])
for i in range(len(students_scores)):
    students_scores[i] = int(students_scores[i])
    max_score = max(students_scores[i], max_score)
    min_score = min(students_scores[i], min_score)

# print(f"Highest score is {max_score}")
# print(f"Lowest score is {min_score}")

# ---------------------------------------------------------
print(3+2)  # Add
print(4-1)  # Subtract
print(2*3)  # Multiply
print(5/2)  # Divide
print(5**2)  # Exponent
print(round(5 / 2))
print(math.ceil(2.3)) # up round




