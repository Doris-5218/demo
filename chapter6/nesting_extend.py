aliens = []
for alien_number in range (0,30):
    new_alien =  {"color":"green", "point":5, "speed":"slow"}
    aliens.append(new_alien)

#將前3個外星人改內容
for alien in aliens[0:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 10
for alien in aliens[0:5]:
    print(alien)
print("...")

print("Total number of aliens:" + str(len(aliens)))

#用if_elif，做其他資料的修改
for alien in aliens[0:5]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 10
    elif alien["color"] =="yellow":
        alien["color"] = "red"
        alien["speed"] = "fast"
        alien["points"] = 15
        
for alien in aliens[0:11]:
    print(alien)
print("...")