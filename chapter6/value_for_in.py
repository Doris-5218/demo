favorite_languages = {
    "jen": "python",
    "sarah": "C",
    "edward": "ruby",
    "phil": "python",
    }
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

for language in set(favorite_languages.values()):
    print(language.title())
#用set()可以排除重複值(回傳唯一)