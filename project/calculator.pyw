#Intro to Programming
#Author: Susan Cantoni
#Calculator Project 1

#graphical user interface calculator

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
        elif operation == 'sin':
            answer = sine(answer)
        elif operation == 'cos':
            answer = cosine(answer)
        elif operation == 'tan':
            answer = tangent(answer)
        elif operation == '10^x':
            answer = power_of_ten(answer)
        elif operation == 'log':
            answer = log_button(answer)
        elif operation == 'ln':
            answer = natural_log(answer)
        elif operation == 'sin^-1':
            answer = arc_sin(answer)
        elif operation == 'cos^-1':
            answer = arc_cos(answer)
        elif operation == 'tan^-1':
            answer = arc_tan(answer)
        elif operation == 'x^y':
            answer = x_to_the_y(answer, entry)
        entry = 0
    return answer, entry

def create_window(scientific_mode):
    if scientific_mode:
            
        win = GraphWin("Calculator", 446, 654)

        displayScreen = Rectangle (Point(10,10), Point(436,110))
        displayScreen.setFill('lightcyan')
        displayScreen.draw(win)

        del buttons[:]

        buttons.append(create_button (win, 8, 115, 73, 187, "7"))
        buttons.append(create_button (win, 8, 192, 73, 264, "4"))
        buttons.append(create_button (win, 8, 269, 73, 341, "1"))
        buttons.append(create_button (win, 8, 346, 73, 418, "+/-", 'blue'))
        buttons.append(create_button (win, 8, 423, 73, 495, "x2", 'blue'))
        buttons.append(create_button (win, 8, 500, 73, 572, "(", 'blue'))
        buttons.append(create_button (win, 8, 577, 73, 649, "M+", 'lightskyblue'))
        buttons.append(create_button (win, 81, 115, 146, 187, "8"))
        buttons.append(create_button (win, 81, 192, 146, 264, "5"))
        buttons.append(create_button (win, 81, 269, 146, 341, "2"))
        buttons.append(create_button (win, 81, 346, 146, 418, "0"))
        buttons.append(create_button (win, 81, 423, 146, 495, "√", 'blue'))
        buttons.append(create_button (win, 81, 500, 146, 572, ")", 'blue'))
        buttons.append(create_button (win, 81, 577, 146, 649, "MR", 'lightskyblue'))
        buttons.append(create_button (win, 154, 115, 219, 187, "9"))
        buttons.append(create_button (win, 154, 192, 219, 264, "6"))
        buttons.append(create_button (win, 154, 269, 219, 341, "3"))
        buttons.append(create_button (win, 154, 346, 219, 418, "."))
        buttons.append(create_button (win, 154, 423, 219, 495, "1/x", 'blue'))
        buttons.append(create_button (win, 154, 500, 219, 572, "C", 'blue'))
        buttons.append(create_button (win, 154, 577, 219, 649, "MS", 'lightskyblue'))
        buttons.append(create_button (win, 227, 115, 292, 187, "/", 'blue'))
        buttons.append(create_button (win, 227, 192, 292, 264, "*", 'blue'))
        buttons.append(create_button (win, 227, 269, 292, 341, "+", 'blue'))
        buttons.append(create_button (win, 227, 346, 292, 418, "-", 'blue'))
        buttons.append(create_button (win, 227, 423, 292, 495, "%", 'blue'))
        buttons.append(create_button (win, 227, 500, 292, 572, "=", 'blue'))
        buttons.append(create_button (win, 227, 577, 292, 649, "M-", 'lightskyblue'))
        buttons.append(create_button (win, 300, 115, 365, 187, "sin", 'blue'))
        buttons.append(create_button (win, 300, 192, 365, 264, "cos", 'blue'))
        buttons.append(create_button (win, 300, 269, 365, 341, "tan", 'blue'))
        buttons.append(create_button (win, 300, 346, 365, 418, "10^x", 'blue'))
        buttons.append(create_button (win, 300, 423, 365, 495, "log", 'blue'))
        buttons.append(create_button (win, 300, 500, 365, 572, "ln", 'blue'))
        buttons.append(create_button (win, 300, 577, 365, 649, "MC", 'lightskyblue'))
        buttons.append(create_button (win, 373, 115, 438, 187, "sin^-1", 'blue'))
        buttons.append(create_button (win, 373, 192, 438, 264, "cos^-1", 'blue'))
        buttons.append(create_button (win, 373, 269, 438, 341, "tan^-1", 'blue'))
        buttons.append(create_button (win, 373, 346, 438, 418, "x^y", 'blue'))
        buttons.append(create_button (win, 373, 577, 438, 649, "Sci", 'lightskyblue'))

    else:
        win = GraphWin("Calculator", 373, 654)

        displayScreen = Rectangle (Point(10,10), Point(363,110))
        displayScreen.setFill('lightcyan')
        displayScreen.draw(win)

        del buttons[:]
    
        buttons.append(create_button (win, 8, 115, 73, 187, "7"))
        buttons.append(create_button (win, 8, 192, 73, 264, "4"))
        buttons.append(create_button (win, 8, 269, 73, 341, "1"))
        buttons.append(create_button (win, 8, 346, 73, 418, "+/-", 'blue'))
        buttons.append(create_button (win, 8, 423, 73, 495, "x2", 'blue'))
        buttons.append(create_button (win, 8, 500, 73, 572, "MC", 'lightskyblue'))
        buttons.append(create_button (win, 8, 577, 73, 649, "M+", 'lightskyblue'))
        buttons.append(create_button (win, 81, 115, 146, 187, "8"))
        buttons.append(create_button (win, 81, 192, 146, 264, "5"))
        buttons.append(create_button (win, 81, 269, 146, 341, "2"))
        buttons.append(create_button (win, 81, 346, 146, 418, "0"))
        buttons.append(create_button (win, 81, 423, 146, 495, "√", 'blue'))
        buttons.append(create_button (win, 81, 500, 146, 572, "M-", 'lightskyblue'))
        buttons.append(create_button (win, 81, 577, 146, 649, "MR", 'lightskyblue'))
        buttons.append(create_button (win, 154, 115, 219, 187, "9"))
        buttons.append(create_button (win, 154, 192, 219, 264, "6"))
        buttons.append(create_button (win, 154, 269, 219, 341, "3"))
        buttons.append(create_button (win, 154, 346, 219, 418, "."))
        buttons.append(create_button (win, 154, 423, 219, 495, "1/x", 'blue'))
        buttons.append(create_button (win, 154, 500, 219, 572, "C", 'blue'))
        buttons.append(create_button (win, 154, 577, 219, 649, "MS", 'lightskyblue'))
        buttons.append(create_button (win, 227, 115, 292, 187, "/", 'blue'))
        buttons.append(create_button (win, 227, 192, 292, 264, "*", 'blue'))
        buttons.append(create_button (win, 227, 269, 292, 341, "+", 'blue'))
        buttons.append(create_button (win, 227, 346, 292, 418, "-", 'blue'))
        buttons.append(create_button (win, 227, 423, 292, 495, "%", 'blue'))
        buttons.append(create_button (win, 227, 500, 292, 572, "=", 'blue'))
        buttons.append(create_button (win, 227, 577, 292, 649, "Sci", 'lightskyblue'))
        buttons.append(create_button (win, 300, 115, 365, 187, "(", 'blue'))
        buttons.append(create_button (win, 300, 192, 365, 264, ")", 'blue'))

    displayString1 = ''
    displayString2 = ''
    displayTextElement1 = Text(Point(300, 50), "")
    displayTextElement1.draw(win)
    displayTextElement2 = Text(Point(250, 75), "")
    displayTextElement2.draw(win)

    return win, displayString1, displayString2, displayTextElement1, displayTextElement2

def main():
    scientific_mode = False
    win, displayString1, displayString2, displayTextElement1, displayTextElement2 = create_window (scientific_mode)
    #answer is running total
    #entry is the current number being typed in
    #operation is adding the math funtion to the equals display
    #clearNextNumber means the display should be cleared next time a number is pressed
    answer = None
    entry = 0
    operation = None
    clearNextNumber = False
    memory = 0
    entryString = ''

    while 1 == 1:
        clicked = win.getMouse()
        x = clicked.getX()
        y = clicked.getY()

        for b in buttons:
            button, label = b
            key = check_button(button, label, x, y)
            if key:
                if key == '=':
                    clearNextNumber = False
                    # do the calculation
                    if answer == None:
                        answer = entry
                        displayString1 = entryString
                        displayString2 = str(answer)
                        entry = 0
                        entryString = ''
                    else:
                        answer, entry = do_calculation(answer, entry, operation)
                        operation = None
                        displayString1 = displayString1
                        displayString2 = '%20.3f' % (answer) 

                elif key in ['+', '-', '/', '*', '%']:
                    # do the calculation
                    answer, entry = do_calculation(answer, entry, operation)
                    entryString = ''
                    operation = key
                    displayString1 = displayString1 + key
                    displayString2 = ''
                    clearNextNumber = False
                    
                elif key == '+/-':
                    # do the calculation
                    answer, entry = do_calculation(answer, entry, operation)
                    entryString = ''
                    operation = key
                    displayString1 = ''
                    displayString2 = str(answer)
                    clearNextNumber = True

                elif key == 'x2':
                    # do the calculation
                    answer, entry = do_calculation(answer, entry, operation)
                    operation = key
                    displayString1 = str(answer) + str('^2')
                    displayString2 = ''
                    clearNextNumber = True

                elif key  == '√':
                    #do the calculation
                    answer, entry = do_calculation(answer, entry, operation)
                    entryString = ''
                    operation = key
                    #trial -- + entry
                    displayString1 = key + entry
                    displayString2 = str(answer)
                    clearNextNumber = True

                elif key == '1/x':
                    x = entry
                    answer, entry = do_calculation(answer, entry, operation)
                    entryString = ''
                    operation = key
                    displayString1 = ''
                    displayString2 = str(answer)
                    clearNextNumber = True

                elif key == 'C':
                    # clear current text
                    displayString1 = ''
                    displayString2 = ''
                    answer = None
                    entry = 0
                    entryString = ''
                    operation = None

                elif key == 'M+':
                    memory = add(float(memory), entry or answer)
                    displayString1 = ''
                    displayString2 = str(memory)

                elif key == 'MR':
                    displayString1 = ''
                    displayString2 = str(memory)
                    
                elif key == 'M-':
                    memory = subtract(float(memory), entry or answer)
                    displayString1 = ''
                    displayString2 = str(memory)

                elif key == 'MC':
                    memory = 0

                elif key == 'MS':
                    temp = memory
                    memory = entry
                    entry = temp
                    displayString1 = ''
                    displayString2 = str(memory)
                    
                elif key == '10^x':
                    answer, entry = do_calculation(answer, entry, operation)
                    operation = key
                    #entry ?
                    displayString1 = '10^' + str(answer)
                    displayString2 = ''
                    clearNextNumber = True
                    
                elif key in ['sin', 'cos', 'tan', 'log', 'ln', 'sin^-1', 'cos^-1', 'tan^-1']:
                    answer, entry = do_calculation(answer, entry, operation)
                    operation = key

                    if answer == None:
                        answer = entry
                        displayString1 = key + '(' + entryString + ')'
                        displayString2 = str(answer)
                        entry = 0
                        entryString = ''
                    else:
                        answer, entry = do_calculation(answer, entry, operation)
                        operation = None
                        displayString1 = key + '(' + entryString + ')'
                        displayString2 = '%20.3f' % (answer)

                    clearNextNumber = True


                elif key == 'x^y':
                    answer, entry = do_calculation(answer, entry, operation)
                    entryString = ''
                    operation = key
                    displayString1 = displayString1 + '^'
                    displayString2 = str(answer)
                    clearNextNumber = False

                elif key == 'Sci':
                    #kill old window; invert it; create new one; reset
                    win.close()
                    scientific_mode = not scientific_mode
                    #added to below
                    win, displayString1, displayString2, displayTextElement1, displayTextElement2 = create_window (scientific_mode)
                    displayString1 = ''
                    displayString2 = ''
                    clearNextNumber = False
                    answer = None
                    entry = 0
                    entryString = ''
                    operation = None

                elif key == '(':
                    entryString = ''
                    displayString1 = displayString1 + '(' + entryString
                    displayString2 = ''
                    clearNextNumber = False

                elif key == ')':
                    displayString1 = displayString1 + ')'
                    displayString2 = ''
                    clearNextNumer = False

                    
                else:
                    # number keys or '.'
                    """
                    # JA: SIngle argument functions, e.g. sin could
                    # calculate without waiting for =
                    """
                    if clearNextNumber:
                        displayString1 = ''
                        displayString2 = ''
                        clearNextNumber = False
                        answer = None
                        entry = 0
                        entryString = ''
                        operation = None
                    entryString = entryString + key
                    if entryString[0] == '.':
                        entry = eval("0" + entryString)
                    else:
                        entry = eval(entryString) 
                    displayString1 = displayString1 + key
                    displayString2 = ''

                displayTextElement1.undraw()
                displayTextElement1 = Text(Point(300, 50), displayString1)
                displayTextElement1.setFace('arial')
                displayTextElement1.setSize(20)
                displayTextElement1.draw(win)
                displayTextElement2.undraw()
                displayTextElement2 = Text(Point(250, 75), displayString2)
                displayTextElement2.setFace('arial')
                displayTextElement2.setSize(20)
                displayTextElement2.draw(win)

                # debug printouts
                """
                if answer:
                    print("key: %s answer: %15.3f entry %15.3f" % (key, answer, entry))
                else:
                    print("key: %s answer: None     entry %15.3f" % (key, entry))

                """
main()
