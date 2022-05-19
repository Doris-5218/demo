sandwich_orders = ["Tuna Sandwich","ham sandwich","meat floss sandwich"]
finished_sandwiches = []
while sandwich_orders:
		current_order = sandwich_orders.pop()
		print("I made your "+ current_order + ".")
		finished_sandwiches.append(current_order)
print("\nThe following have been finished:")
for finished_sandwiche in finished_sandwiches:
		print(finished_sandwiche.title()) 