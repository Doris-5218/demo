def city_country(city_name,country_name):
	full = f"{city_name}, {country_name}"
	return full.title()
x = city_country("santiago","chile")
print(x)
x = city_country("rome","italy")
print(x)
x = city_country("Kyiv","Ukraine")
print(x)