rivers = {
    "Nile":"Africa",
    "Amazon":"Brazil",
    "Yangtze":"Sichuan",
}
for key, value in rivers.items():
    print("The " + key + " runs through " + value + ".")

for name in rivers.keys():
    print(name.title())

for country in rivers.values():
    print(country.title())