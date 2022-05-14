favorite_places = {
    "doris":["taipei","Taichung", "New Taipei city"],
    "lucien":["taipei","Taichung","Yilan"],
    "john":["taipei", "keelung", "Hualien"],
}
for name, places in favorite_places.items():
    print("\n" + name.title())
    for place in places:
        print("\t" + place.title())
#如果字典內的值大於1個，就要再寫迴圈(FOR)去顯示