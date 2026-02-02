#Read a fileand handle the case when the file does not exist

file = "ankit.txt"

try:
    f = open(file,"r")
except FileNotFoundError:
    print("file does't exist")
finally:
    if file:
        file.read("ankit.txt")
        file.close()
    print("file readed sucessfully")
    print("file closed ")