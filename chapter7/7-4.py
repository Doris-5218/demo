prompt = "\nWhat toppings do you want for your pizza?"
prompt += "\nEnter 'quit' when you are finished."

active = True
while active:
    message = input(prompt)
    if message == "quit":
        active = False
    else:
        print("Adding" + message + "!")
print("\nFinished making your pizza!")