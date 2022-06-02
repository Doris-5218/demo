def make_shirt(shirt_size,shirt_words = "I Love Python"):
	print("\nYou Order a shirt in " + shirt_size.upper() + " size")
	print("Print '" + shirt_words + "'on it.")

make_shirt("xl")
make_shirt("m")
make_shirt("l",shirt_words = "I LOVE YOU")