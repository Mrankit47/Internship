#arbitrary keyword argument data type is dict
def user_detail (**user):
    print("his Fname is : " + user["fname"])
    print("his Lname is : " + user["lname"])
    print("All detail : ",user)
user_detail(fname="ankit",lname="kushwah")