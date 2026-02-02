row = int(input("Enter no of row : "))
for i in range(row,0,-1):
    print(" "*(row-i),end="")
    for j in range(i):
        print("  *",end="")
    print()