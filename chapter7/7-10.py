responses = {}
while True:
		name = input("\nWhat is your name? ")
		response = input("If you could visit one place in the world, where would you go? ")
		responses[name] = response
		break		
for name, response in responses.items():
		print(name + " would like to visit " + response + ".")