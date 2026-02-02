def my_detail(username,**detail):
    print("username : ",username)
    print("Aditional Detail")
    for key,value in detail.items():
        print(" ",key + ":",value)
my_detail("ankit0210k", age=24, cource="Mca", college = "svvv")