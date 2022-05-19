# while 重複執行到條件不符合才停止
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1


prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

message = ""
while message != "quit":
    message = input(prompt)
    
    if message != "quit":
        print(message)
#加上if是為了不讓循環結束還印出"quit"

#使用旗標
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

active = True
while active:
    message = input(prompt)
    
    if message == "quit":
        active = False
    else:
        print(message)

#break離開迴圈
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\nEnter 'quit' when you are finished."

while True:
    city = input(prompt)

    if city == "quit":
        break
    else:
        print("I'd love to go to " + city.title() + "!")

#continue返回迴圈的開頭
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
         continue

    print(current_number)

