def make_car(dealer, model, **car_info):
    profile = {}
    profile['dealer_name'] = dealer
    profile['model_name'] = model
    for key, value in car_info.items():
        profile[key] = value
    return profile
user_profile = make_car("subaru","outback",color = "blue", tow_package = True)
print(user_profile)