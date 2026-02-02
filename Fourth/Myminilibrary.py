#build a mini library system using function
Library = []

def add_book():
    book = input("\nEnter book name : ")
    Library.append(book)
    print("Book added sucessfully.\n")

    
def show_book():
    if not Library:
        print("No Book Available\n")
    else:
        print("\n All Available Books\n")
    
        for i in Library:
            print(i)
        print("\n")

def issue_book():
    book_n= input("\nEnter book name : ")
    if book_n in Library:
        print("Book issued sucessfully\n")
        Library.remove(book_n)
    else:
        print("Invalid book name\n")

def Return_book():
    
    R_book = input("\nReturn book name : ")
    Library.append(R_book)
    print("Book Return Sucessfully\n")


print("\n********* MINI LIBRARY SYSTEM *********\n")


while True:
    print(" 1. Add Book ")
    print(" 2. Show Book ")
    print(" 3. Issue Book ")
    print(" 4. Return Book ")
    print(" 5. Exit \n")
    Option = input("Choose any option : ")


    if Option == "1":
        add_book()
    elif Option == "2":
        show_book()
    elif Option == "3":
        issue_book()
    elif Option == "4":
        Return_book()
    elif Option == "5":
        print("\nThanks for using this library")
        break
    else:
        print("\nInvalid Input Try again \n")

