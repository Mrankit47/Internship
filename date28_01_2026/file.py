#for write an existing file
# with open("file.txt","w") as f:
#     f.write("my name is ankit kushwah")
# #for append in existing file
# with open("file.txt","a") as f:
#     f.write(" To write to an existing file you must add a p")
# # for read the file
# with open("file.txt") as f:
#     print(f.read())
# for create new file 
# with open("my_file.txt","x") as k:
#     k.write("Python file creation")
with open("my_file.txt","b+r") as q:
    print(q.read())


    