#Log user actions into a file 
import datetime

def user_action(User_name,Action):
    valid_action = ["login","logout","create","delete","update"]

    if Action.lower() in valid_action:
        status = "SUCCESS"
    else:
        status = "FAIL"
    with open("User.txt","w") as f:
        D = datetime.datetime.now()
        print()
        print("-----------User Action Detail-----------")
        f.write(D.strftime("Date : %D          Time : %T\n"))
        print()
        f.write(f"UserName : {User_name} \nAction : {Action}\n")
        f.write(f"Status :{status} ")

User_name = input("Enter your User_name : ")
print("Action Choices :- Login, Logout, Create, Update, Delete   )")
Action = input("Enter your choice : ")
user_action(User_name,Action)
with open("User.txt")as d:
    print(d.read())




