#Intro to Programming
#Author: Susan Cantoni
#Calculator Project 1

#graphical user interface calculator

#future enhancements:
#TODO deal with decimal numbers
#TODO make buttons change color after pressed

from calc_functions import *
from graphics import *

# list of buttons (button, label)
buttons = []


def create_button(win, x1, y1, x2, y2, label, color = 'aquamarine'):
    button = Rectangle(Point(x1,y1), Point(x2, y2))
    button.setFill(color)
    button.draw(win)
    text = Text(button.getCenter(), label)
    text.setFace('arial')
    text.setSize(20)
    text.draw(win)
    return button, label

def check_button(button, label, x, y):
    x1 = button.p1.getX()
    y1 = button.p1.getY()
    x2 = button.p2.getX()
    y2 = button.p2.getY()
    if x > x1 and x < x2 and y > y1 and y < y2:
        return label
    return False

def do_calculation(answer, entry, operation):
    if answer == None:
        answer = entry
        entry = 0
    else:
        if operation == '+':
            answer = add(answer, entry)
        elif operation == '-':
            answer = subtract(answer, entry)
        elif operation == '*':
            answer = multiply(answer, entry)
        elif operation == '/':
            answer = divide(answer, entry)
        elif operation == '+/-':
            answer = change_sign(answer)
        elif operation == 'x2':
            answer = square(answer)
        elif operation == '%':
            answer = percent(answer)
        elif operation == '√':
            answer = square_root(answer)
        elif operation == '1/x':
            answer = over_x(answer)
        entry = 0
    return answer, entry


def main():
    win = GraphWin("Calculator", 300, 577)

    displayScreen = Rectangle (Point(10,10), Point(290,110))
    displayScreen.setFill('lightcyan')
    displayScreen.draw(win)

    buttons.append(create_button (win, 8, 115, 73, 187, "7"))
    buttons.append(create_button (win, 8, 192, 73, 264, "4"))
    buttons.append(create_button (win, 8, 269, 73, 341, "1"))
    buttons.append(create_button (win, 8, 346, 73, 418, "+/-", 'blue'))
    buttons.append(create_button (win, 8, 423, 73, 495, "x2", 'blue'))
    buttons.append(create_button (win, 8, 500, 73, 572, "", 'blue'))
    buttons.append(create_button (win, 81, 115, 146, 187, "8"))
    buttons.append(create_button (win, 81, 192, 146, 264, "5"))
    buttons.append(create_button (win, 81, 269, 146, 341, "2"))
    buttons.append(create_button (win, 81, 346, 146, 418, "0"))
    buttons.append(create_button (win, 81, 423, 146, 495, "√", 'blue'))
    buttons.append(create_button (win, 81, 500, 146, 572, "", 'blue'))
    buttons.append(create_button (win, 154, 115, 219, 187, "9"))
    buttons.append(create_button (win, 154, 192, 219, 264, "6"))
    buttons.append(create_button (win, 154, 269, 219, 341, "3"))
    buttons.append(create_button (win, 154, 346, 219, 418, "."))
    buttons.append(create_button (win, 154, 423, 219, 495, "1/x", 'blue'))
    buttons.append(create_button (win, 154, 500, 219, 572, "C", 'blue'))
    buttons.append(create_button (win, 227, 115, 292, 187, "/", 'blue'))
    buttons.append(create_button (win, 227, 192, 292, 264, "*", 'blue'))
    buttons.append(create_button (win, 227, 269, 292, 341, "+", 'blue'))
    buttons.append(create_button (win, 227, 346, 292, 418, "-", 'blue'))
    buttons.append(create_button (win, 227, 423, 292, 495, "%", 'blue'))
    buttons.append(create_button (win, 227, 500, 292, 572, "=", 'blue'))


#TODO make more buttons for square root and memory (?)

    displayString = ''
    displayTextElement = Text(Point(200, 50), "")
    displayTextElement.draw(win)
    #answer is running total
    #entry is the current number being typed in
    #operation is adding the math funtion to the equals display
    #clearNextNumber means the display should be cleared next time a number is pressed
    answer = None
    entry = 0
    operation = None
    clearNextNumber = False
    decimal = False 


    while 1 == 1:
        clicked = win.getMouse()
        x = clicked.getX()
        y = clicked.getY()

        for b in buttons:
            button, label = b
            key = check_button(button, label, x, y)
            if key:
                if key == '=':
                    clearNextNumber = True
                    # do the calculation
                    if answer == None:
                        answer = entry
                        displayString = str(answer)
                        entry = 0
                    else:
                        answer, entry = do_calculation(answer, entry, operation)
                        operation = None
                        displayString = str(answer)
#TODO make decimal button print a decimal on display 

                elif key in ['+', '-', '/', '*', '%']:
                    # do the calculation
                    answer, entry = do_calculation(answer, entry, operation)
                    operation = key
                    displayString = displayString + key
                    clearNextNumber = False

#TODO make square root work
                    
                elif key == '+/-':
                    # do the calculation
                    answer, entry = do_calculation(answer, entry, operation)
                    operation = key
                    displayString = str(answer)
                    clearNextNumber = True

                elif key == 'x2':
                    # do the calculation
                    answer, entry = do_calculation(answer, entry, operation)
                    operation = key
                    displayString = str(answer) + str('^2')
                    clearNextNumber = True

                elif key  == '√':
                    #do the calculation
                    answer, entry = do_calculation(answer, entry, operation)
                    operation = key
                    displayString = key + str(answer)
                    clearNextNumber = True

#TODO fix sqrt: make it show symbol and not only sqrt the answer

                elif key == '1/x':
                    x = entry
                    answer, entry = do_calculation(answer, entry, operation)
                    operation = key
                    displayString = str(answer)
                    clearNextNumber = True

                elif key == 'C':
                    # clear current text
                    displayString = ''
                    answer = None
                    entry = 0
                    operation = None

                elif key == '.':
                    displayString = displayString + '.'
                    clearNextNumber = False
                   

                else:
                    # number keys
                    if clearNextNumber:
                        displayString = ''
                        clearNextNumber = False
                        answer = None
                        entry = 0
                        operation = None
                    entry = (entry * 10) + int(key)
                    displayString = displayString + key
                    '''
                    if decimal:
                        displayString = float(answer)
                        print(displayString)
                        return True
                    '''

                displayTextElement.undraw()
                displayTextElement = Text(Point(200, 50), displayString)
                displayTextElement.setFace('arial')
                displayTextElement.setSize(20)
                displayTextElement.draw(win)

main()
