people = {
    "doris":{
        "first_name":"Chen",
        "last_name":"Ting Yun",
        "age":36,
        "city":"New Taipei City",
        },
    "lucien":{
        "first_name":"CHUNG",
        "last_name":"YUN-CHU",
        "age":26,
        "city":"Taipei",
        },
    "john":{
        "first_name":"LI",
        "last_name":"CHIA-CHUN",
        "age":48,
        "city":"Keelung",
        },
}
for name, user_info in people.items():
    print("\n" + name.title())
    full_name = user_info["first_name"] + " " + user_info["last_name"]
    age = user_info["age"]
    city = user_info["city"]

    print("\tFull_name:" + full_name.title())
    print("\tAge:" + str(age))
    print("\tCity:" + city.title())