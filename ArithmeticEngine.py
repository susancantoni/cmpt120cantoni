# CMPT 120 - Lab #6
# Susan Cantoni
# 03-22-2018
###
def showIntro():
    print("Welcome to the Arithmetic Engine!")
    print("=================================\n")
    print("Valid commands are 'add', 'mult', 'sub', 'div', and 'quit'.\n")
def showOutro():
    print("\nThank you for using the Arithmetic Engine…")
    print("\nPlease come back again soon!")
def doLoop():
    while True:
        cmd = input("What computation do you want to perform? ").lower()
        other = False
        while other == False:
            if cmd == "add" or cmd == "sub" or cmd == "mult" or cmd == "div" or cmd == "quit":
                other = True
            else:
                print (cmd, "is not a valid command.")
                cmd = input("What computation do you want to perform? ").lower()
        if cmd == "quit":
            break
                
        try:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
        except:
            print ("That input is not valid. Enter a number.")
        if num2 == 0:
            raise Exception("Unable to divide by zero!")
        continue
        if cmd == "add":
            print ("you got here")
            result = num1 + num2
        elif cmd == "sub":
            result = num1 - num2
        elif cmd == "mult":
            result = num1 * num2
        elif cmd == "div":
            result = num1 // num2
        elif cmd == "quit":
            break
        print("The result is " + str(result) + ".\n")
            
def main():
    showIntro()
    doLoop()
    showOutro()

main()
