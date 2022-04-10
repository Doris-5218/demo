unmbers = list(range(1,6))
print(unmbers)
even_numbers = list(range(2,11,2))
#range開始於2結束於11的前一位數，以2為單位遞增
print(even_numbers)
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

squares = []
for value in range(1,100):
    squares.append(value**2)
print(squares)

squares = [value**2 for value in range(1,11)]
#使用這個寫法，range後面不用加:
print(squares)