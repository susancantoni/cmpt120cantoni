#Intro to Programming
#Author: Susan Cantoni
#Calculator Project 1

#graphical user interface calculator

from calc_functions import *
from graphics import *
from button import *

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
        buttons.append(Button(win, Point(40.5, 151), 65, 72, "7"))
        buttons.append(Button(win, Point(40.5, 228), 65, 72, "4"))
        buttons.append(Button(win, Point(40.5, 305), 65, 72, "1"))
        buttons.append(Button(win, Point(40.5, 382), 65, 72, "+/-", 'blue'))
        buttons.append(Button(win, Point(40.5, 459), 65, 72, "x2", 'blue'))
        buttons.append(Button(win, Point(40.5, 536), 65, 72, "(", 'blue'))
        buttons.append(Button(win, Point(40.5, 613), 65, 72, "M+", 'lightskyblue'))
        buttons.append(Button(win, Point(113.5, 151), 65, 72, "8"))
        buttons.append(Button(win, Point(113.5, 228), 65, 72, "5"))
        buttons.append(Button(win, Point(113.5, 305), 65, 72, "2"))
        buttons.append(Button(win, Point(113.5, 382), 65, 72, "0"))
        buttons.append(Button(win, Point(113.5, 459), 65, 72, "√", 'blue'))
        buttons.append(Button(win, Point(113.5, 536), 65, 72, ")", 'blue'))
        buttons.append(Button(win, Point(113.5, 613), 65, 72, "MR", 'lightskyblue'))
        buttons.append(Button(win, Point(186.5, 151), 65, 72, "9"))
        buttons.append(Button(win, Point(186.5, 228), 65, 72, "6"))
        buttons.append(Button(win, Point(186.5, 305), 65, 72, "3"))
        buttons.append(Button(win, Point(186.5, 382), 65, 72, "."))
        buttons.append(Button(win, Point(186.5, 459), 65, 72, "1/x", 'blue'))
        buttons.append(Button(win, Point(186.5, 536), 65, 72, "C", 'blue'))
        buttons.append(Button(win, Point(186.5, 613), 65, 72, "MS", 'lightskyblue'))
        buttons.append(Button(win, Point(259.5, 151), 65, 72, "/", 'blue'))
        buttons.append(Button(win, Point(259.5, 228), 65, 72, "*", 'blue'))
        buttons.append(Button(win, Point(259.5, 305), 65, 72, "+", 'blue'))
        buttons.append(Button(win, Point(259.5, 382), 65, 72, "-", 'blue'))
        buttons.append(Button(win, Point(259.5, 459), 65, 72, "%", 'blue'))
        buttons.append(Button(win, Point(259.5, 536), 65, 72, "=", 'blue'))
        buttons.append(Button(win, Point(259.5, 613), 65, 72, "M-", 'lightskyblue'))       
        buttons.append(Button(win, Point(332.5, 151), 65, 72, "sin", 'blue'))
        buttons.append(Button(win, Point(332.5, 228), 65, 72, "cos", 'blue'))
        buttons.append(Button(win, Point(332.5, 305), 65, 72, "tan", 'blue'))
        buttons.append(Button(win, Point(332.5, 382), 65, 72, "10^x", 'blue'))
        buttons.append(Button(win, Point(332.5, 459), 65, 72, "log", 'blue'))
        buttons.append(Button(win, Point(332.5, 536), 65, 72, "ln", 'blue'))
        buttons.append(Button(win, Point(332.5, 613), 65, 72, "MC", 'lightskyblue'))
        buttons.append(Button(win, Point(405.5, 305), 65, 72, "sin^-1", 'blue'))
        buttons.append(Button(win, Point(405.5, 382), 65, 72, "cos^-1", 'blue'))
        buttons.append(Button(win, Point(405.5, 459), 65, 72, "tan^-1", 'blue'))
        buttons.append(Button(win, Point(405.5, 536), 65, 72, "x^y", 'blue'))
        buttons.append(Button(win, Point(405.5, 613), 65, 72, "Sci", 'lightskyblue'))


    else:
        win = GraphWin("Calculator", 373, 654)

        displayScreen = Rectangle (Point(10,10), Point(363,110))
        displayScreen.setFill('lightcyan')
        displayScreen.draw(win)

        del buttons[:]
    
        buttons.append(Button(win, Point(40.5, 151), 65, 72, "7"))
        buttons.append(Button(win, Point(40.5, 228), 65, 72, "4"))
        buttons.append(Button(win, Point(40.5, 305), 65, 72, "1"))
        buttons.append(Button(win, Point(40.5, 382), 65, 72, "+/-", 'blue'))
        buttons.append(Button(win, Point(40.5, 459), 65, 72, "x2", 'blue'))
        buttons.append(Button(win, Point(40.5, 536), 65, 72, "MC", 'blue'))
        buttons.append(Button(win, Point(40.5, 613), 65, 72, "M+", 'lightskyblue'))
        buttons.append(Button(win, Point(113.5, 151), 65, 72, "8"))
        buttons.append(Button(win, Point(113.5, 228), 65, 72, "5"))
        buttons.append(Button(win, Point(113.5, 305), 65, 72, "2"))
        buttons.append(Button(win, Point(113.5, 382), 65, 72, "0"))
        buttons.append(Button(win, Point(113.5, 459), 65, 72, "√", 'blue'))
        buttons.append(Button(win, Point(113.5, 536), 65, 72, "M-", 'blue'))
        buttons.append(Button(win, Point(113.5, 613), 65, 72, "MR", 'lightskyblue'))
        buttons.append(Button(win, Point(186.5, 151), 65, 72, "9"))
        buttons.append(Button(win, Point(186.5, 228), 65, 72, "6"))
        buttons.append(Button(win, Point(186.5, 305), 65, 72, "3"))
        buttons.append(Button(win, Point(186.5, 382), 65, 72, "."))
        buttons.append(Button(win, Point(186.5, 459), 65, 72, "1/x", 'blue'))
        buttons.append(Button(win, Point(186.5, 536), 65, 72, "C", 'blue'))
        buttons.append(Button(win, Point(186.5, 613), 65, 72, "MS", 'lightskyblue'))
        buttons.append(Button(win, Point(259.5, 151), 65, 72, "/", 'blue'))
        buttons.append(Button(win, Point(259.5, 228), 65, 72, "*", 'blue'))
        buttons.append(Button(win, Point(259.5, 305), 65, 72, "+", 'blue'))
        buttons.append(Button(win, Point(259.5, 382), 65, 72, "-", 'blue'))
        buttons.append(Button(win, Point(259.5, 459), 65, 72, "%", 'blue'))
        buttons.append(Button(win, Point(259.5, 536), 65, 72, "=", 'blue'))
        buttons.append(Button(win, Point(259.5, 613), 65, 72, "Sci", 'lightskyblue'))       
        buttons.append(Button(win, Point(332.5, 151), 65, 72, "(", 'blue'))
        buttons.append(Button(win, Point(332.5, 228), 65, 72, ")", 'blue'))

    for b in buttons:
        b.activate()
        
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
            if b.clicked(Point(x,y)):
                key = b.getLabel()
                if key == '=':
                    clearNextNumber = False
                    if answer == None:
                        answer = entry
                        displayString1 = ''
                        displayString2 = str(answer)
                        entry = 0
                        entryString = ''
                    else:
                        answer, entry = do_calculation(answer, entry, operation)
                        operation = None
                        displayString1 = ''
                        displayString2 = '%20.3f' % (answer) 

                elif key in ['+', '-', '/', '*', '%']:
                    answer, entry = do_calculation(answer, entry, operation)
                    entryString = ''
                    operation = key
                    displayString1 = displayString1 + key
                    displayString2 = str(answer)
                    clearNextNumber = False
                    
                elif key == '+/-':
                    answer, entry = do_calculation(answer, entry, operation)
                    operation = key
                    displayString1 = ''
                    displayString2 = str(answer)
                    clearNextNumber = True

                elif key == 'x2':
                    answer, entry = do_calculation(answer, entry, operation)
                    operation = key
                    displayString1 = str(answer) + str('^2')
                    displayString2 = ''
                    clearNextNumber = True

                elif key  == '√':
                    answer, entry = do_calculation(answer, entry, operation)
                    entryString = ''
                    operation = key
                    displayString1 = key + str(answer)
                    displayString2 = str(answer)
                    clearNextNumber = True

                elif key == '1/x':
                    x = entry
                    answer, entry = do_calculation(answer, entry, operation)
                    entryString = ''
                    operation = key
                    displayString1 = '1/' + str(answer)
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
                    if answer:
                        displayString2 = str(answer)
                    else:
                        displayString2 = ''
                    clearNextNumber = False

                elif key == ')':
                    displayString1 = displayString1 + ')'
                    if answer:
                        displayString2 = str(answer)
                    else:
                        displayString2 = ''
                    clearNextNumer = False

                    
                else:
                    # number keys or '.'
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
                    displayString2 = key

                displayTextElement1.undraw()
                displayTextElement1 = Text(Point(300, 50), displayString1)
                displayTextElement1.setFace('arial')
                displayTextElement1.setSize(20)
                displayTextElement1.draw(win)
                displayTextElement2.undraw()
                displayTextElement2 = Text(Point(300, 75), displayString2)
                displayTextElement2.setFace('arial')
                displayTextElement2.setSize(20)
                displayTextElement2.draw(win)

main()



calc = Calculator()
calc.run()
