from dataclasses import dataclass
import datetime   

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

new_task = []
users = {}

def load_users(userList): #Daniel - Loads users into a dictionary from the user-list file
    with open(userList, "r") as file:
        for line in file:
            userInfo = line.strip().split(',')
            if len(userInfo) < 8:  #HAS TO CHECK TO MAKE SURE LINE HAS ALL EXPECTED FIELDS
                continue
            name = userInfo[0]
            adminStatus = userInfo[1] == "True"
            isFirstLogin = userInfo[2] == "True"
            tasks = userInfo[3].split(',') if userInfo[3] else []
            phone = userInfo[4]
            email = userInfo[5]
            clockedIn = userInfo[6] == "True"
            password = userInfo[7]
            users[name] = User(name, adminStatus, isFirstLogin, tasks, phone, email, clockedIn, password)
    return users

def loaded_user(userList):
    load = input("Please provide the name of the user you would like to load for the selected progress: ")

    with open(userList, "r") as file:
        with open(userList, "r") as file:
            for line in file:
                userInfo = line.strip().split(',')
                if userInfo[0] == load:
                    continue
                name = userInfo[0]
                adminStatus = userInfo[1] == "True"
                isFirstLogin = userInfo[2] == "True"
                tasks = userInfo[3].split(',') if userInfo[3] else []
                phone = userInfo[4]
                email = userInfo[5]
                clockedIn = userInfo[6] == "True"
                password = userInfo[7]
                user_load = User(name, adminStatus, isFirstLogin, tasks, phone, email, clockedIn, password)
    return user_load
    
def timeclock(current_user, timesheet): #Daniel
    now = datetime.datetime.now()
    if current_user.time_in == False: #CLOCKING IN
        current_user.time_in = True
        print(f"{current_user} has been clocked in.")
        with open(timesheet, "a") as clockInSheet:
            clockInSheet.write(f"{current_user.name} Clock-in: {now.strftime("%Y-%m-%d %H:%M:%S")}\n")
    elif current_user.time_in == True: #CLOCKING OUT
        current_user.time_in = False
        print(f"{current_user} has been clocked out")
        with open(timesheet, "a") as clockOutSheet:
            clockOutSheet.write(f"{current_user.name} Clock-out: {now.strftime("%Y-%m-%d %H:%M:%S")}\n")

# def createTask():#Spencer
        
#         user.tasks.append(new_task)
#         user.tasks.append(f"{description}\n")
    
    # if pick_task in employee.tasks:
    #     # assign_task = input("\nWho would you like to assign this task to: ")
    #     if assign_task == employee:
    #         employee.tasks.append(pick_task)
        
def updatetaskProgress(user: User): # Quan
    if user.is_admin == False:
       user_input = input("Name? ")
       if user_input == user.name :
        for each in user.tasks:
           user.tasks.append(each)
        print("Task Updated.")

def viewTask():  #temp place holder Quan/Spencer
        user_input = input("Name: ")
        if user_input in users.keys():
            assignedPerson = users[user_input]
            for each in assignedPerson.tasks:
                print(f"Task: {each}")
                #change after task are made

def create_user(): #Product of Jet 
    is_admin = input("Should this new user have admin access? [Y/N]: ")
    while is_admin != "Y" and is_admin != "N":
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
        file.writelines("\n" + name+"," + str(is_admin)+"," + "True," + "," + phone+"," + email+"," + "False," + "")

def assignTask(): #Spencer
    assign_person = input("Who would you like to assign this task to: ")
    if assign_person in users.keys():
        assignedPerson = users[assign_person]   
        task = input("Task: ")
        assignedPerson.tasks.append(task)
        print(f"New task has been assigned to {assignedPerson.name}")
    
def main():
    employee = User("", False, True, [], "", "", False, "")
    timesheet = "timesheet.txt"
    userList = "user-list.txt"

    print("Hello, welcome to [PROJECT]! \n")

    users = load_users(userList)

    admSignedIn = False
    empSignedIn = False

    while True:
        username = input("Please enter your name to sign-in: ").strip()
        password = input("Please enter your password: ").strip()

        current_user = users.get(username)
        
        if current_user is None:
            print("User not found. Please contact your admin for assistance.\n")
            continue

        if current_user.password != password:
            print("Incorrect password.\n")
            continue

        if current_user != None and current_user.password == password:
            if current_user.is_admin:
                    print(f"Welcome, Admin {current_user.name}\n")
                    admSignedIn = True
                    
                    while admSignedIn:
                        command = input("You can [view] tasks, [add] tasks, [assign] tasks, [create] a new user [clock] in/out, or [sign] out. ").lower().strip()
                        if command == "view":
                            viewTask()
                        elif command == "assign":
                            assignTask()
                            
                        elif command == "create":
                            create_user()
                        elif command == "clock":
                            timeclock(current_user, timesheet)
                        elif command == "sign":
                            print("Signing out...\n")
                            admSignedIn = False
                            break
                        else:
                            print("Invalid input.")

            elif current_user.is_admin == False:
                    print(f"Welcome, {current_user.name}\n")
                    empSignedIn = True
                    
                    while empSignedIn:
                        command = input("You can [view] tasks, [update] progress on a task, [clock] in/out, or [sign] out. ").lower().strip()
                        if command == "view":
                            viewTask(current_user)
                        elif command == "update":
                            ...
                        elif command == "clock":
                            timeclock(current_user, timesheet)
                        elif command == "sign":
                            print("Signing out...\n")
                            empSignedIn = False
                            break
                        else:
                            print("Invalid input.")


if __name__ == "__main__":
    main()

