age = 12
if age <4:
    print("your admission cost is $0.")
elif age <18:
    print("your admission cost is $5.")
else:
    print("your admission cost is $10.")

age = 12
if age <4:
    price = 0
elif age <18:
    price = 5
else:
    price = 10
print("your admission cost is $" + str(price)+".")
#一樣的東西不同的寫法

#多加一個收費間/65及65歲以上的老人入門費用半價
age = 65
if age <4:
    price = 0
elif age <18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5
print("your admission cost is $" + str(price)+".")

age = 27
if age <4:
    price = 0
elif age <18:
    price = 5
elif age >= 65:
    price =5
else:
    price = 10
print("your admission cost is $" + str(price)+".")
#另一種寫法，更清楚的表示