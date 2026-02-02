# def recurtion (n):
#     if n<=0:
#         print("Complete")
#     else:
#         print(n)
#         recurtion(n-1)
# recurtion(10)

#print table with help of recurtion

def table(j,no=1):
    
    if no>10:
        print("Table done")
    else:
        print(j*no  )
        table(j,no+1)



n = int(input("Enter any no : "))

table(n)