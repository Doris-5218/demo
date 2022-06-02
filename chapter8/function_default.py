def describe_pet(pet_name, animal_type='dog'):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='willie')
#有實參的放在前面（默認值在後面）

describe_pet(pet_name='harry', animal_type='hamster')
#如果要描述的動物不是小狗