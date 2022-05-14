# store information about a pizza being ordered.
pizza ={
    "crust": "thick",
    "toppings": ["mushrooms","extra cheese"],
}
#the order.
print("You ordered a " + pizza["crust"] + "-crust pizza" + " with the follwing toppings:")

for topping in pizza["toppings"]:
    print("\t" + topping)

favorite_languages = {
    "jen": ["python","ruby"],
    "sarah": ["C"],
    "edward": ["ruby","go"],
    "phil": ["python","haskell"],
    }
for name, languages in favorite_languages.items():
    print("\n" + name.title()+ "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())