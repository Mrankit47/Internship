try:
    x = int(input("Enter number : "))
    print(19/x)
except ZeroDivisionError:
    print("can not divide by zero")
except ValueError:
    print("Invalid Input")
else:
    print("Sucess")
finally:
    print("Program End")
