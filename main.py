from dataclasses import dataclass
import datetime



now = datetime.datetime.now()

@dataclass
class System :
  on_off : bool
  admin_access : bool

@dataclass
class User:
  is_admin : bool
  name : str
  tasks : list
  phone_number : str
  email : str
  time_in : str
  time_out : str

def timesheet():
    ...

def assignTask():
    ...

def taskProgress():
    ...

def viewTask():
    ...

def main():
    ...


if __name__ == "__main__":
    main()

