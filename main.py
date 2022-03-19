import replit as sys
import time 
from os import environ as env
import re


def odd_indices(lst):
  return [lst[i] for i in range(len(lst)) if i % 2 != 0]


def even_indices(lst):
  return [lst[i] for i in range(len(lst)) if i % 2 == 0]




file = open("passwords.txt", "r")
information = file.read().lower()
split_info = re.split('[,\n]', information)


#Manage and handle passwords
UN_passwords = odd_indices(split_info)
K = 13
passwords = [sub[K :] for sub in UN_passwords]

#Manage and handle usernames
UN_usernames = even_indices(split_info)
Y = 10
gamer = [sub[Y :] for sub in UN_usernames]
usernames = [sub[ :-3] for sub in gamer]




owner_username = env["REPL_OWNER"]

logged_in = False



def type(text):
    for char in text:
                time.sleep(0.05)
                print(char, end ='', flush = True)


def type_fast(text):
    for char in text:
                time.sleep(0.005)
                print(char, end ='', flush = True)


def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            print(line.rstrip())
             


def add():
    
    username = input("What is your username?" + "\n")
    pwd = input("What is your password?" + "\n")

    with open("passwords.txt", "a") as f:
        f.write("Username =" + username + "   ,   " + "Password =" + pwd + "\n")


def password_sys():
    while True:
        mode = input("Would you like to add a new password or view your passwords?  (view/add)\n or q to quit" + "\n").lower()

        if mode == "q":
            sys.clear()
            break

        if mode == "view":
            sys.clear()
            view()
            input("Press enter to continue\n")
            sys.clear()
        elif mode == "add":
            sys.clear()
            add()
            sys.clear()
        else:
            sys.clear()
            print("That is not a valid option")
            time.sleep(1)
            sys.clear()
            continue


#codes starts running
#log-in system
while True:
    user_name = str(input("What is your username :\n")).lower()
    user_password = str(input("What is the password :\n")).lower()
    
    if  user_name not in usernames or user_password not in passwords:
        print("Incorrect username or password")
        time.sleep(1.3)
        sys.clear()
        continue
    elif user_name in usernames and user_password in passwords:
        sys.clear()
        type("Welcome, " + str(owner_username))
        print("")
        logged_in = True
        break




#code for main system
while logged_in == True:
    print("1.Passwords")
    print("2.log out")
    option = int(input("Option: "))    
    if option == 1:
        sys.clear()
        password_sys()
    elif option == 2:
        confirmation = str(input("confirm? (y/n)\n")).lower()
        if confirmation == "y":
            logged_in = False
            sys.clear()
            print("You have logged out")
        elif confirmation == "n":
            sys.clear()
            logged_in = True
            
    else:
        print("Invalid option")
        time.sleep(1)
        sys.clear()


