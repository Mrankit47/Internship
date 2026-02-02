#find max value in user intput tuple

def find_max(*tup):
    if len(tup) == 0:
        return 0
    max = tup[0]
    for i in tup:
        if i>max:
            max=i
    return max

tup = ()
n = int(input("Enter no of element : "))
a = list(tup)
for j in range(n):
    v = int(input("enter value : "))
    a.append(v)
tup = tuple(a)
max_value = find_max(*tup)
print("max value is : ",max_value)





