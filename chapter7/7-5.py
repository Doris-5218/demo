while True :
		age = input("\nWhat is your age ?")
		age = int(age)
		if age < 3:
				print("your ticket fare is free.")
				break
		elif age <12:
				print("your ticket fare is 10.")
				break
		elif age >12:
				print("your ticket fare is 15.")
				break