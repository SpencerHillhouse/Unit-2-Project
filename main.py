from dataclasses import dataclass
import datetime
from tqdm import tqdm

now = datetime.datetime.now()
now.strftime("%Y-%m-%d %H:%M:%S")


@dataclass
class System :
  on_off : bool
  admin_access : bool

@dataclass
class User:
  name: str
  is_admin : bool
  is_first_login : bool
  tasks : list
  phone_number : str
  email : str
  time_in : bool
  password : str

def timeclock(current_user, timesheet): #Daniel
    if current_user.time_in == False: #CLOCKING IN
        current_user.time_in == True
        print(f"{current_user} has been clocked in.")
        with open(timesheet, "a") as clockInSheet:
            clockInSheet.write(f"{current_user.name} Clock-in: {now.strftime("%Y-%m-%d %H:%M:%S")}\n")
    if current_user.time_in == True: #CLOCKING OUT
        current_user.time_in = False
        print(f"{current_user} has been clocked out")
        with open(timesheet, "a") as clockOutSheet:
            clockOutSheet.write(f"{current_user.name} Clock-out: {now.strftime("%Y-%m-%d %H:%M:%S")}\n")

def createTask():
    ...

def assignTask(employee: User): #Spencer
    if employee.is_admin:
        pick_task = ("Which task would you like to assign: ")
        if pick_task in employee.tasks:
            assign_task = input("\nWho would you like to assign this task to: ")
            if assign_task == employee:
                employee.tasks.append(pick_task)
        
        

def taskProgress():
    if User.is_admin == True:
        for i in tqdm (range (100), 
               desc="Loading…", 
               ascii=False, ncols=75):
            User.tasks(0.01)
            print("Task are Complete.")

def viewTask():  #temp place holder
        if User.is_admin == True:
            user_input = input("Name? ")
            for each in user_input:
                print(each.tasks)
                #change after admins are made

def create_user(): #Product of Jet 
    is_admin = input("Should this new user have admin access? [Y/N]: ")
    
    while is_admin != "Y" or is_admin != "N":
        print("Invalid, please try again.")
        is_admin = input("Should this new user have admin access? [Y/N]: ")

    name = input("Name: ")
    #task will be added in seperate function. 
    phone = input("Phone Number: ")
    email = input("Email Address: ")
                
    if is_admin == "Y":
        is_admin = True
    else:
        is_admin = False
    
    new_user = User(name, is_admin, True,[], phone, email, False, "")

    with open("user-list.txt", 'a') as file:
        file.write(new_user + "\n")


    

    

    ...
    
    
def main():
    timesheet = "timesheet.txt"
    userList = "user-list.txt"
    admin = User("Test_Admin", True, False, [], "123-456-7890", "test_admin@company.org", True, "AdminPass!")
    now.strftime("%Y-%m-%d %H:%M:%S")

    empSignedIn = False
    admSignedIn = False

    print("Hello, welcome to [PROJECT]! \n")
    current_user = input("Please enter your name to sign-in: ")

    with open(userList, "r") as userList:
        if current_user in userList.readlines():
            if current_user.is_admin == False:
                empSignedIn = True
            elif current_user.is_admin == True or current_user == admin:
                admSignedIn = True
        elif current_user not in userList.readlines():
            print("User not found. Please contact an admin for assistance.")

    while empSignedIn:
        print(f"Welcome {current_user.name}\n")
        command = input("Yo" can [])
    #view tasks, update progress, timeclock

    while admSignedIn:
        ...
    #view timesheet, assign/create tasks, create user, timecock


    timeclock(current_user,timesheet)

if __name__ == "__main__":
    main()

