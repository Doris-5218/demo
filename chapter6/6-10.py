numbers = {}
numbers["Allen"] = 3, 10, 11
numbers["Tina"] = 7, 17, 27
numbers["Lucien"] = 5, 8, 10, 20, 36
numbers["Doris"] = 9, 11, 3, 6,
numbers["Una"] = 6, 99, 66
for name, number in numbers.items():
    print("\n" + name.title())
    for no in number:
        print("\t" + str(no))