import datetime

# Parent class (Encapsulation)
class User:
    def __init__(self, user_name, action):
        self.user_name = user_name
        self.action = action
        self.__status = None   # private variable

    def _set_status(self):
        valid_action = ["login", "logout", "create", "delete", "update"]
        if self.action.lower() in valid_action:
            self.__status = "SUCCESS"
        else:
            self.__status = "FAIL"

    def get_status(self):
        return self.__status


# Child class (Inheritance)
class UserAction(User):
    def __init__(self, user_name, action):
        super().__init__(user_name, action)
        self._set_status()
        self.save_to_file()

    def save_to_file(self):
        with open("User.txt", "w") as f:
            D = datetime.datetime.now()
            print("\n----------- User Action Detail -----------\n")

            f.write(D.strftime("Date : %D          Time : %T\n"))
            f.write(f"UserName : {user_name}\n")
            f.write(f"Action   : {action}\n")
            f.write(f"Status   : {self.get_status()}\n")


# Object creation
user_name = input("Enter your User_name : ")
print("Action Choices :- Login, Logout, Create, Update, Delete")
action = input("Enter your choice : ")

obj = UserAction(user_name, action)

# Read file
with open("User.txt") as d:
    print(d.read())

