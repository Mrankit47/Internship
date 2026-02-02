import os

if os.path.exists("file.txt"):
    os.remove("file.txt")
    print("file remove sucessfully")
else:
    print("file does not exit")

os.rmdir("C:/Users/Ankit/OneDrive/Desktop/pagal")