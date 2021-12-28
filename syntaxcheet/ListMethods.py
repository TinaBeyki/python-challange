import random

friends = ["joe", "chandler", "ross", "monica", "phebe"]

friends.append("rachel")  # Adding an Item to a List
print(friends)

print(friends[-1])

list1 = [1, 2, 3]
list2 = [9, 8, 7]
new_list = list1 + list2  # or list1 += list2 ->  adding 2 list together
print(list1)

random.shuffle(friends)
print(friends)