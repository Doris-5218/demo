cars = ["audi","bmw","subaru","toyota"]
for car in cars:
    if car == "bmw":
        # =是將資料寫進變數，==是檢查變數裡的資料是否相同
        print(car.upper())
    else:
        print(car.title())