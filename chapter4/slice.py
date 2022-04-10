players = ["charles","martian","michael","florence","eli"]
print(players[0:3])
print(players[:4])
print(players[2:])
print(players[-3:])
print(players[-1])
# 數列從0開始，第一個位置開始到第二個數之前一位結束
# 如數列太開，也可以用-1表示最後一位
print("Here are the first tree players on my team:")
for value in players[:3]:
    print(value.title())