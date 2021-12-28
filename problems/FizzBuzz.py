nums = []
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        nums.append("FizzBuzz")
    elif i % 3 == 0 and i % 5 != 0:
        nums.append("Fizz")
    elif i % 5 == 0 and i % 3 != 0:
        nums.append("Buzz")
    else:
        nums.append(i)
print(nums)
