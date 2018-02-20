# CMPT 120 Intro to Programming
# Lab #5 – Working with Strings and Functions
# Author: Susan Cantoni
# Created: 2018-02-19

def nameDetails():
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    return first, last

def maristStyle(first, last):
    uname = first + "." + last
    return uname.lower()

def passwordCheckStrength (passwd):
    if len(passwd) >=8 and passwd!=passwd.lower():
        return True
    else:
        return False

def passwordCheckLength (uname):
    passwd = input("Create a new password: ")
    while not passwordCheckStrength(passwd):
        print("That password is feeble! It must contain 8 characters and at least one Uppercase!")
        passwd = input("Create a new password: ")
    return passwd

def main():
    first, last = nameDetails()
    uname = maristStyle(first, last) 
    passwd = passwordCheckLength(uname)
    print("The force is strong in this one…")
    print("Account configured. Your new email address is", uname + "@marist.edu")
    
main()
