favorite_languages = {
    "jen": "python",
    "sarah": "C",
    "edward": "ruby",
    "phil": "python",
    }
for name in favorite_languages.keys():
    print(name.title())

friends = ["phil", "sarah"]
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print("Hi " + name.title() + ", I see your favorite language is " + favorite_languages[name].title() + "!")
#可以用一個list去指定回覆，某些key並回覆對應值

if "erin" not in favorite_languages.keys():
    print("Erin, please take our poll!")
#可以用if去檢查字典中是否有某個值

for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thanke you for taking the poll.")
#可以用sorted(暫時排序)讓資料依序排列顯示