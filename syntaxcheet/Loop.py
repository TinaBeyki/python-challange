students_height = input("enter students height: ").split()
total_weight = 0
num = len(students_height)
for i in range(0, len(students_height)):
    students_height[i] = int(students_height[i])
    total_weight += students_height[i]

print(sum(students_height))
average = round(total_weight / num)  # (total_weight // num)
print(f"average height in this grade is: {average}")


# -------------------------------------------------------------------------------------------------
movie_name_letters = ["f", "r", "i", "e", "n", "d", "s"]
name = ""
for i in range(0, len(movie_name_letters)):
    name += movie_name_letters[i] + "."
print(name)