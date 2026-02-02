x = int(input("Enter any number :"))
if x < 0: 
    raise Exception("sorry, no numbers below zero")
print("x =",x)