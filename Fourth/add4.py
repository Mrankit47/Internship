def add(*numbers):
    total =0
    for i in numbers:
        total+=i
    return total
print(add(3,5,2,6,5,9))
print(add(3,5,26,6,58,9))
print(add(3,53,2,66,5,9))
print(add(3,57,2,46,5,99))