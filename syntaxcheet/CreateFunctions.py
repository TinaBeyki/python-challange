def my_function(n):
    if n == 0 or n == 1:
        return 1
    return my_function(n - 1) + my_function(n - 2)


for i in range(0, 5):
    print(my_function(i))

# ---------------------------------------------------


def greet_by_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}? ")


#greet_by_name("Tina")
# name -> parameter(name of parameter which is passed to method),  Tina -> argument(actual data which is passed)


def greet_with_name_location(name, location):
    print(f"Hello {name}")
    print(f"How is it like in {location}? ")


# greet_with_name_location("Tina", "Iran")
greet_with_name_location(location="Iran", name="Tina")  # for solving this problem ->
# greet_with_name_location("Iran","Tina")
