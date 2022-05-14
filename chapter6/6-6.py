favorite_languages = {
    "jen": "python",
    "sarah": "C",
    "edward": "ruby",
    "phil": "python",
    }
poll_list = ("doris","sarah","lucien","phil")
for name in favorite_languages.keys():
    if name in poll_list:
        print("Hi, "+ name.title() + " thank you taked our poll !")
for name in poll_list:
    if name not in favorite_languages:
        print("Hi," + name.title()+ " please take our poll !")

    
    