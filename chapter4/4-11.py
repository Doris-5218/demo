my_flavors = ["Hawaiian","Margherita","Smoked Salmon"]
my_friend_flavors = my_flavors[:]
print(my_flavors)
print(my_friend_flavors)
my_flavors.append("Pepperoni")
my_friend_flavors.append("Neapolitan")
print("My favorite pizzas are:")
for pizza in my_flavors:
    print(my_flavors)
print("My friend's favorite pizzas are:")
for pizza in my_friend_flavors:
    print(my_friend_flavors)