row = int(input("Enter no of row : "))
for i in range(1,row+1):
    print(" "*(row-i),end="")
    for j in range(i):
        print("*",end="")
    print()