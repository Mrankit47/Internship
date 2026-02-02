#open a file and close it using finally even if an error occurs


fil = None

try:
    t=open("ankit.txt")
except FileNotFoundError:
    print("file not found")
finally:
    if fil:
        fil.close()
    print("file is close")