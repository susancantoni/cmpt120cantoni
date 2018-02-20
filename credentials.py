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
    return uname

def main():
    first, last = nameDetails()
    uname = maristStyle(first, last) 
    # ask user to create a new password
    passwd = input("Create a new password: ")
    # TODO modify this to ensure the password has at least 8
    if len(passwd) >= 8:
        print("Account configured. Your new email address is", uname + "@marist.edu")
    if len(passwd) < 8:
        print("Fool of a Took! That password is feeble! It must contain 8 characters!")
        passwd = input("Create a new password: ")
        print("The force is strong in this one…")
        print("Account configured. Your new email address is", uname + "@marist.edu")
main()
