num = int(input("Enter any number : "))
T=num
digits = len(str(num))
sum = 0
while T>0:
    digit = T%10
    sum += digit**digits
    T //=10
    
if sum == num:
    print("yes")
else:
    print("not")
    