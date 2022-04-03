motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
del motorcycles[0]
# 指定位置
print(motorcycles)

popped_motorcycle=motorcycles.pop()
# 字串堆疊的最後
print(motorcycles)
print(popped_motorcycle)

motorcycles=['honda','yamaha','suzuki']
last_owned=motorcycles.pop()
print("The last motorcycle I owned was a "+last_owned.title()+".")
# 加入文字

motorcycles=['honda','yamaha','suzuki']
motorcycles.remove("honda")
print(motorcycles)
# 指定故定直去刪除

motorcycles=['honda','yamaha','suzuki','ducati']
too_expensive="ducati"
motorcycles.remove(too_expensive)
print("\nA "+too_expensive.title()+" is too expensive for me")