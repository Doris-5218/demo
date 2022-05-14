#字典中的字典，中間還是要用，區隔及注意位置
from turtle import title


users = {
    "aeinstein": {
        "first": "albert",
        "last": "einstein",
        "location": "princetion",
        },
    "mcurie": {
        "first": "marie",
        "last": "curie",
        "location": "paris",
        },
}

for username, user_info in users.items():
    print("\nUsername:" + username)
    full_name = user_info["first"] + " " + user_info["last"]
    location = user_info["location"]
    print("\tfull name:" + full_name.title())
    print("\tLocation:" + location.title())
