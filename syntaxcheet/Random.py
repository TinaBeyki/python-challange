import random

friends = ["joe", "chandler", "ross", "monica", "phebe", "rachel"]
chosen_name = random.randint(0, len(friends) - 1)
print(friends[chosen_name])  # print(random.choice(friends))

random_int = random.random()  # random number between 0 and 1 but not exactly 1
print(random_int)

random_num = random.randint(0, 1000) # random number between 0 and 1000
print(random_num)

random.shuffle(friends)
print(friends)