from dataclasses import dataclass
import datetime   

# @dataclass
# class System :
#   on_off : bool
#   admin_access : bool

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
   
def updatetaskProgress(current_user): # Quan/Spencer
    if current_user.tasks == []:
        print("This employee has no current tasks.")
    else:
        updatedTask = input("Which task would you like to update: ")
        if updatedTask in current_user.tasks:
            status = input("In progress or Completed: ").capitalize()
            if status == "In progress":
                print(f"Task: {updatedTask} (In progress)")
            elif status == "Completed":
                print(f"Tasks: {updatedTask} (Completed)")
                current_user.tasks.remove(updatedTask)
    
def viewTask():  #temp place holder Quan/Spencer
        userTask = input("Who's task would you like to see: ")
        if userTask in users.keys():
            assignedPerson = users[userTask]
        if assignedPerson.tasks == []:
            print("This employee has no current tasks.")
        else:
            for each in assignedPerson.tasks:
                print(f"Task: {each} (Uncompleted)")
                

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

def first_login(current_user, userList): #Daniel
    if current_user.is_first_login == True:
        print("\nWelcome! This is your first login.")

        while True:
            password = input("Please choose a password: ")
            confirmPassword = input("Please confirm password: ")

            if password == confirmPassword:
                current_user.password = password
                current_user.is_first_login = False

                #updating user-list.txt with password
                with open(userList, "r") as f:
                    lines = f.readlines()
                
                with open(userList, "w") as f: #HAVE TO USE WRITE TO OVERWRITE THE LINE
                    for line in lines:
                        userInfo = line.strip().split(',')
                        if userInfo[0] == current_user.name:
                            userInfo[7] = password 
                            userInfo[2] = "False"
                            line = ','.join(userInfo)
                        f.write(line)
                print("Password set.\n")
                break
            else:
                print("Passwords do not match. Please try again.")

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
        username = input("Logging in: Please enter your name to sign-in: ").strip()

        current_user = users.get(username)

        if current_user is None:
            print("User not found. Please contact your admin for assistance.\n")
            continue

        #Check to see if it is the users first time logging in.
        first_login(current_user, userList)

        password = input("Logging in: Please enter your password: ").strip()

        if current_user.password != password:
            print("Incorrect password.\n")
            continue

        if current_user != None and current_user.password == password:
            if current_user.is_admin:
                    print(f"Welcome, Admin {current_user.name}\n")
                    admSignedIn = True
                    
                    while admSignedIn:
                        command = input("You can [view] tasks, [assign] tasks, [create] a new user [clock] in/out, or [sign] out. ").lower().strip()
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
                            viewTask()
                        elif command == "update":
                            updatetaskProgress(current_user)
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

