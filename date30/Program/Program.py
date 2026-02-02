# Convert previous function-based project to oops
import datetime

class usercAtion:
    def __init__(self,User_name,Action):
        self.User_name = User_name
        self.Action = Action

class set_action(usercAtion):
        def __init__(self, User_name, Action):
             super().__init__(User_name, Action)
             valid_action = ["login","logout","create","delete","update"]
             if Action.lower() in valid_action:
                 status = "SUCCESS"
             else:
                 status = "FAIL"
             with open("UserAction.txt","w") as f:
                 D = datetime.datetime.now()
                 print()
                 print("-----------User Action Detail-----------")
                 f.write(D.strftime("Date : %D          Time : %T\n"))
                 print()
                 f.write(f"UserName : {User_name} \nAction : {Action}\n")
                 f.write(f"Status :{status} ")


User_name = input("Enter your user name : ")
print("Action Choices : - Login, Logout, Create, Update, Delete")
Action = input("Enter you choice : ")
S = set_action(User_name,Action)

with open("UserAction.txt") as f:
    print(f.read())

            




