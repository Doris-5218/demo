answer = 39
gussing = None

while gussing != answer:
    gussing = int(input("請輸入你要猜的數字:"))
    if gussing < answer:
        print("大一點")
    elif gussing > answer:
        print("小一點")
print("你贏了!!!!")


answer = 39
gussing = None
gussing_count = 0
gussing_limit = 3
out_of_limit = False

while gussing != answer and not (out_of_limit):
    gussing_count += 1
    if gussing_count <= gussing_limit:
        gussing = int(input("請輸入你要猜的數字:"))
        if gussing < answer:
            print("大一點")
        elif gussing > answer:
            print("小一點")
    else:
        out_of_limit = True

if out_of_limit:
    print("你輸了= =")
else:
    print("你贏了!!!!")