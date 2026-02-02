#arbitrary keyword argument data type is tuple
def Detail (*data):
    print("name : ",data[0])
    print("age : ",data[1])
    print("email : ",data[2])
    print("All Detail : ",data)
Detail("Ankit",24,"ankitkushwah0210k@gamil.com")
