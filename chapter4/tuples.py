# tuples多元組:不能修改的值稱為不可變的(immutalbe)，而這個不可變的串列就稱為多元組，用小括號表示()
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
# 多元組不可修改，但可以重寫
dimensions = (400,100)
print("modified dimensions:")
for dimension in dimensions:
    print(dimension)
