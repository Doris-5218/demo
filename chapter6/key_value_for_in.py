user_0 = {
    "username": "efermi",
    "first": "enrico",
    "last" : "fermi",
    }
for key, value in user_0.items():
    print("\nKey:" + key)
    print("Value:" + value)
#key=鍵，value=值，可以同時用二個變數，中間用，區隔
#.items()指字典中的全部鍵值對

favorite_languages = {
    "jen": "python",
    "sarah": "C",
    "edward": "ruby",
    "phil": "python",
    }
for name, language in favorite_languages.items():
    print(name.title()+ "'s favorite language is " + language.title() + ".")