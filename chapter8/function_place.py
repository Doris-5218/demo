def describe_pet(animal_type, pet_name):
		print("\nI have a " + animal_type + ".")
		print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
#可多次調用同一個函數

#另一種值對的寫法，不用照順序
def describe_pet(animal_type, pet_name):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(animal_type='hamster', pet_name='harry')