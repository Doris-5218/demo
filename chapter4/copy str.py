my_foods = ["pizza","falafel","carrot cake"]
friend_foods = my_foods[:]
# copy 字串，不會同部改變
print("My favorite foods are:")
print(my_foods)
print("My friend's favorite foods are:")
print(friend_foods)

my_foods.append("cannoli")
friend_foods.append("ice ceam")

print("My favorite foods are:")
print(my_foods)
print("My friend's favorite foods are:")
print(friend_foods)

