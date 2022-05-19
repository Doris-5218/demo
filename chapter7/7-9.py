sandwich_orders = ["Tuna Sandwich","pastrami sandwich","ham sandwich","pastrami sandwich","meat floss sandwich","pastrami sandwich"]
finished_sandwiches = []
while sandwich_orders:
	current_order = sandwich_orders.pop()
	if current_order == "pastrami sandwich":
		print("Sorry,pastrami sandwich is sold out!")
	else:
		print("I made your "+ current_order + ".")
		finished_sandwiches.append(current_order)

while "pastrami sandwich" in finished_sandwiches:
		finished_sandwiches.remove("pastrami sandwich")
print("\nThe following have been finished:")
for finished_sandwiche in finished_sandwiches:
		print(finished_sandwiche.title())