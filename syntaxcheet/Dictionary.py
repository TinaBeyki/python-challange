programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected",
    "Fuction": "A piece of code that you can easily call over and over again",
    "Loop": "The action of doing something over and over again",
}
# dictionary format -> {key: value}
# retrieve by key
# print(programming_dictionary["Bug"])


# adding new item to dictionary --------------
programming_dictionary["DocumentaionString"] = "Multi-line string"
# print(programming_dictionary)


empty_dictionary = {}

# wipe an existing dicationary ---------------
# programming_dictionary = {}
# print(programming_dictionary)

# edit an item in a dictionary ---------------
programming_dictionary["Bug"] = "What the hell, why its not running:/"
print(programming_dictionary)

for key in programming_dictionary:
    print(f"key: {key}")  # prints keys
    print(f"value: {programming_dictionary[key]}")


# -------------------------------------------------------------------

students_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 90,
    "Draco": 74,
    "Neville": 65
}

students_grades = {}

for student in students_scores:
    score = students_scores[student]
    if score <= 70:
        students_grades[student] = "Fail"
    elif 71 <= score <= 80:
        students_grades[student] = "Accepatble"
    elif 81 <= score <= 90:
        students_grades[student] = "Exceeds Expectation"
    else:
        students_grades[student] = "Outstanding"


# print(students_grades)
# -------------------------------------------------------------------
"""
Nested -> {
            key: [List]
            key: [Dict]
          }
"""
capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# Nesting list in a dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamborg", "Stuttgart"],
}

# Nesting dictionary in a dictionary
travel_visit_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamborg", "Stuttgart"],
        "total_visits": 5
    }
}

# Nesting dictionary inside a list
travel_visit_log_list = [
    {
        "country": "France",
        "visited_cities": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
     },
    {
        "country": "Germany",
        "visited_cities": ["Berlin", "Hamborg", "Stuttgart"],
        "total_visits": 5
    }
]


def add_new_country(visited_country, visited_cities, total_visits):
    new_country = {}
    new_country["country"] = visited_country
    new_country["visited_cities"] = visited_cities
    new_country["total_visits"] = total_visits

    travel_visit_log_list.append(new_country)


add_new_country(visited_country="Iran", visited_cities=["Kish", "Tehran"], total_visits=2)
print(travel_visit_log_list)