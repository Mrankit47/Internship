n = int(input("Enter no of line : "))

for i in range(n+1):
    for j in range(i):
        print(" *",end="")
    print()