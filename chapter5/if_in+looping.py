requested_toppings = ["mushrooms","onins","pineapple"]
print(("mushrooms" in requested_toppings))
#要PRINT出布林值，必須要有二個()
#使用in 可以檢查出特定值是否在數列中
print(("pepperoni" in requested_toppings))

requested_toppings = ["mushrooms","extra cheese"]
if "mushrooms" in requested_toppings:
    print("Adding mushrooms.")
if "pepperoni" in requested_toppings:
    print("Adding pepproni.")
if "extra cheese" in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making you pizza!")

#如果想要每個都檢查到，就要用if寫單獨式
#如果只想執行一個程式區塊，就用if-elif-else

requested_toppings = ["mushrooms","extra cheese"]
if "mushrooms" in requested_toppings:
    print("Adding mushrooms.")
elif "pepperoni" in requested_toppings:
    print("Adding pepproni.")
elif "extra cheese" in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making you pizza!")


#另一種寫法，用for
requested_toppings = ["mushrooms","green peppers","extra cheese"]

for requested_topping in requested_toppings:
    print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")

#如green pepers用完了，加入if_else
requested_toppings = ["mushrooms","green peppers","extra cheese"]

for requested_topping in requested_toppings:
    if requested_topping == "green peppers":
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")
