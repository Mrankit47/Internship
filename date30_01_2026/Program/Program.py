# Convert previous function-based project to oops
import datetime

class userAction:
    def __init__(self,User_name,Action,Password):
        self.__Password = None
        self.User_name = User_name
        self.Action = Action
    def set_password(self):
         self.__Password = Password
    def get_Password(self):
         return self.__Password

class set_action(userAction):
        def __init__(self, User_name, Action,Password):
             super().__init__(User_name, Action,Password)
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
                 f.write(f"UserName : {User_name} \nAction : {Action}\nPassword : {Password}\n")
    
                 f.write(f"Status :{status} ")


User_name = input("Enter your user name : ")
Password = input("Enter your password :")
print("Action Choices : - Login, Logout, Create, Update, Delete")
Action = input("Enter you choice : ")
S = set_action(User_name,Action,Password)

with open("UserAction.txt") as f:
    print(f.read())

            




