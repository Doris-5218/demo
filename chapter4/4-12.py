my_foods = ["pizza","falafel","carrot cake"]
friend_foods = my_foods[:]
my_foods.append("cannoli")
friend_foods.append("ice ceam")
print("My favorit food are: ")
for food in my_foods:
    print(food)
print("My friend's favorit food are:")
for food in friend_foods:
    print(food)
print("My favorit food are: "+",".join(my_foods))
#可以用join跑出looping在一行的效果