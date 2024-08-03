from dataclasses import dataclass, asdict
from typing import List
import os
import json
import datetime

@dataclass
class EmployeeTasks:
    name: str
    description: str
    status: str

@dataclass
class User:
    name: str
    is_admin: bool
    is_first_login: bool
    tasks: List[EmployeeTasks]
    phone_number: str
    email: str
    time_in: bool
    password: str

user_list_file = "user-list.json"

def save_user(user: User):
    if not os.path.exists(user_list_file):
        with open(user_list_file, 'w') as file:
            json.dump([], file)  # Initialize the file with an empty list

    with open(user_list_file, 'r+') as file:
        users = json.load(file)
        users.append(asdict(user))
        file.seek(0)
        json.dump(users, file)

def load_users():
    if os.path.exists(user_list_file):
        with open(user_list_file, 'r') as file:
            return json.load(file)
    return []

# def turn_to_Object(usersList: list):
#     for each in usersList:
#         objectifiedTasks = [EmployeeTasks(task['name'], task['description'], task['status']) for task in each["tasks"]]
#         each["tasks"] = objectifiedTasks
#     return usersList

def sign_in(updateuser : User):
    users = load_users()
    name = input("Please provide your First and Last Name: ").strip().capitalize()
    search = [user for user in users if name.lower() in user["name"].lower()]
    if search:
        print("Welcome " + name.capitalize())
        password = input("Password: ")
        user_found = False

        for user in search:
         if password == user["password"]:
            updateuser.name = user["name"]
            updateuser.is_admin = user["is_admin"]
            updateuser.is_first_login = user["is_first_login"]
            updateuser.email = user["email"]
            updateuser.tasks = user["tasks"]
            updateuser.phone_number = user["phone_number"]
            updateuser.password = user["password"]
            updateuser.time_in = user["time_in"]

            user_found = True
        if user_found:
            print("You have signed in. Thank you")
            return user
        if not user_found:
            print("User not found, please contact Admin for assistance.")
    else:
        print("incorrect or invalid password.")
        
def create_new_user():
    admin = input("Should this user have Admin Access? |Y/N|: ")
    if admin.upper() == "Y" or admin.upper()=="N":
        if admin.upper() == "Y":
            admin = True
        else:
            admin = False
    name = input("First and Last Name: ").capitalize()
    phone = input("Phone Number: ")
    email = input("Email Address: ")
    newuser = User(name,admin,True,[],phone,email,False,"non")
    save_user(newuser)

def populate_userTBU(TBU : User):
    users = load_users()
    emp_name = input("Name of employee: ")
    search = [user for user in users if emp_name.lower() in user["name"].lower()]
    for user in search:
        TBU.name = user["name"]
        TBU.is_admin = user["is_admin"]
        TBU.is_first_login = user["is_first_login"]
        TBU.email = user["email"]
        TBU.tasks = [EmployeeTasks(name=task[0], description=task[1], status=task[2]) for task in user["tasks"]]
        TBU.phone_number = user["phone_number"]
        TBU.password = user["password"]
        TBU.time_in = user["time_in"]
        return TBU
    
def update_userJSON(TBU :User):
    if os.path.exists(user_list_file):
        with open(user_list_file, 'r') as file:
            data = json.load(file)
            print(f"here {TBU.tasks}")
            for task in TBU.tasks:
                print(task)
            for user in data:
                if user["name"] == TBU.name:
                    user["name"] = TBU.name
                    user["is_admin"]=TBU.is_admin
                    user["is_first_login"] = TBU.is_first_login
                    user["email"] = TBU.email
                    user["tasks"] = [[task[0], task[1], task[2]] for task in TBU.tasks]
                    user["phone_number"] = TBU.phone_number
                    user["password"] = TBU.password
                    user["time_in"] = TBU.time_in
                    with open(user_list_file, 'w') as file: 
                        json.dump(data, file) 

def update_userJSONDataClass(TBU :User):
    if os.path.exists(user_list_file):
        with open(user_list_file, 'r') as file:
            data = json.load(file)
            for user in data:
                if user["name"] == TBU.name:
                    user["name"] = TBU.name
                    user["is_admin"]=TBU.is_admin
                    user["is_first_login"] = TBU.is_first_login
                    user["email"] = TBU.email
                    user["tasks"] = [[task.name, task.description, task.status] for task in TBU.tasks]
                    user["phone_number"] = TBU.phone_number
                    user["password"] = TBU.password
                    user["time_in"] = TBU.time_in
                    with open(user_list_file, 'w') as file: 
                        json.dump(data, file) 

def create_password(user1:User):
    users = load_users()
    name = user1.name
    search = [user for user in users if name.lower() in user["name"].lower()]
    if search:
        for user in search:
            password = input("Please create a password: ")
            confirm = input("Please re-type your password to confirm: ")
            while password != confirm:
                print("Passwords do not match, please try again.")
                password=""
                confirm="_"
                password = input("Please create a password: ")
                confirm = input("Please re-type your password to confirm: ")
            user["password"] = password
            print("You have updated your password!")
            user1.is_first_login = False

def timeclock(user, timesheet):
    now = datetime.datetime.now()
    if user.time_in == False:
        user.time_in = True
        print(f"{user.name} has been clocked in. ")
        with open(timesheet, "a") as clockInSheet:
            clockInSheet.write(f"{user.name} Clock-in: {now.strftime("%Y-%m-%d %H:%M:%S")}\n")
    elif user.time_in == True:
        user.time_in = False
        print(f"{user.name} has been clocked out. ")
        with open(timesheet, "a") as clockOutSheet:
            clockOutSheet.write(f"{user.name} Clock-out: {now.strftime("%Y-%m-%d %H:%M:%S")}\n")

def create_task(user_to_be_updated) -> EmployeeTasks:
    task_name = input("Name of task to be completed: ")
    task_description = input("Any additional details/description for this task: ")
    new_task = EmployeeTasks(name = task_name, description = task_description, status = "Not started.")
    user_to_be_updated.tasks.append(new_task)
    print(f"{task_name} added successfully. ")
    return new_task

def admin_view_tasks():
    users = load_users()
    if not users:
        print("No users found.")
        return
    
    if users:
        for user in users:
            print(f"{user["name"]}'s Tasks: ")
            tasks = user.get("tasks")
            
            if not tasks:
                print(f"{user["name"]} has no tasks.")
                continue

            for task in tasks:
                print(f"Task: {task[0]}")
                print(f"Description: {task[1]}")
                print(f"Status: {task[2]}")

def emp_view_tasks(user):
    if not user.tasks:
        print("You have no tasks assigned. ")
        return
    
    else:
        print(f"Tasks for {user.name}: ")
        for task in user.tasks:
            print(f"Task: {task[0]}")
            print(f"Description: {task[1]}")
            print(f"Status: {task[2]}")

def update_task_status(user):
    if not user.tasks:
        print("You have no tasks assigned.")
        return

    task_name = input("Enter the name of the task you want to update: ").strip()
    for i in user.tasks:
        if i[0] == task_name:
            new_status = input("Enter new status (In Progress or Completed): ").strip()
            if new_status in ["In Progress", "Completed"]:
                user.tasks[0][2] = new_status
                update_userJSON(user)
                print("Task updated successfully.")
                return
            else:
                print("Invalid status.")
                return
    print("Task not found.")


def main():
    user_user = User(name="", is_admin=False, is_first_login=True, tasks=[], phone_number="", email="", time_in=False, password="")
    user_to_be_updated = User(name="", is_admin=False, is_first_login=True, tasks=[], phone_number="", email="", time_in=False, password="")
    newTask = EmployeeTasks(name="", description="", status="Not started")
    
    timesheet = "timesheet.txt"

    # users = load_users()
    # users = turn_to_Object(users)

    admSignedIn = False
    empSignedIn = False

    print("Welcome to TaskTycoon")

    while True:
        command = input("Please [S]ign-in, or [Q]uit: ").strip().upper()
        if command.upper() == "Q":
            break
        elif command.upper() =="S":
            sign_in(user_user)
            if user_user.is_admin:
                admSignedIn = True
                
                while admSignedIn:
                    command = input("You can [V]iew tasks, [A]ssign tasks, [C]reate a new user, [U]pdate an existing user, [Clock]-in/out, or [S]ign out. ").upper().strip()
                    if command == "V":
                        admin_view_tasks()
                    elif command == "A":
                        populate_userTBU(user_to_be_updated)
                        create_task(user_to_be_updated)
                        update_userJSONDataClass(user_to_be_updated)
                        
                    elif command == "C":
                        create_new_user()
                    elif command == "U":
                        populate_userTBU(user_to_be_updated)

                        new_phone = input("Enter new phone number or press enter to keep previous: ")
                        if new_phone:
                            user_to_be_updated.phone_number = new_phone
                        new_email = input("Enter new email address or press enter to keep previous: ")
                        if new_email:
                            user_to_be_updated.email = new_email
                        new_password = input("Enter new password or press enter to keep previous: ")
                        if new_password:
                            user_to_be_updated.password = new_password

                        update_userJSONDataClass(user_to_be_updated)
                    elif command == "CLOCK":
                        timeclock(user_user, timesheet)
                    elif command == "S":
                        print("Signing out... ")
                        admSignedIn = False
                        break
                    else:
                        print("Invalid input. ")

            elif user_user.is_admin == False:
                empSignedIn = True

                while empSignedIn:
                    command = input("You can [V]iew your tasks, [U]pdate progress on a task, [Clock]-in/out, or [S]ign out. ").upper().strip()
                    if command == "V":
                        emp_view_tasks(user_user)
                    elif command == "U":
                        update_task_status(user_user)
                    elif command == "CLOCK":
                        timeclock(user_user, timesheet)
                    elif command == "S":
                        print("Signing out... ")
                        empSignedIn = False
                        break
                    else:
                        print("Invalid input. ")
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()
