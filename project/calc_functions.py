#graphical user interface calculator
import graphics
from graphics import *

# list of buttons (button, label)
buttons = []
#button_labels = ['7', '4', '1', '+ / -', '', '8', '5', '2', '0', '', '9', '6', '3', '.', 'd e l', '/', '*', '+', '-', '=']

def create_button(win, x1, y1, x2, y2, label):
    button = Rectangle(Point(x1,y1), Point(x2, y2))
    button.setFill('aquamarine')
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

def main():
    win = GraphWin("Calculator", 300, 500)

    displayScreen = Rectangle (Point(10,10), Point(290,110))
    displayScreen.setFill('lightcyan')
    displayScreen.draw(win)

    buttons.append(create_button (win, 8, 115, 73, 187, "7"))
    buttons.append(create_button (win, 8, 192, 73, 264, "4"))
    buttons.append(create_button (win, 8, 269, 73, 341, "1"))
    buttons.append(create_button (win, 8, 346, 73, 418, "+/-"))
    buttons.append(create_button (win, 8, 423, 73, 495, ""))
    buttons.append(create_button (win, 81, 115, 146, 187, "8"))
    buttons.append(create_button (win, 81, 192, 146, 264, "5"))
    buttons.append(create_button (win, 81, 269, 146, 341, "2"))
    buttons.append(create_button (win, 81, 346, 146, 418, "0"))
    buttons.append(create_button (win, 81, 423, 146, 495, ""))
    buttons.append(create_button (win, 154, 115, 219, 187, "9"))
    buttons.append(create_button (win, 154, 192, 219, 264, "6"))
    buttons.append(create_button (win, 154, 269, 219, 341, "3"))
    buttons.append(create_button (win, 154, 346, 219, 418, "."))
    buttons.append(create_button (win, 154, 423, 219, 495, "del"))
    buttons.append(create_button (win, 227, 115, 292, 187, "/"))
    buttons.append(create_button (win, 227, 192, 292, 264, "*"))
    buttons.append(create_button (win, 227, 269, 292, 341, "+"))
    buttons.append(create_button (win, 227, 346, 292, 418, "-"))
    buttons.append(create_button (win, 227, 423, 292, 495, "="))

    displayString = ''
    displayTextElement = Text(Point(0, 60), "")
    displayTextElement.draw(win)

    while 1 == 1:
        clicked = win.getMouse()
        x = clicked.getX()
        y = clicked.getY()
        print(x, y)
        for b in buttons:
            button, label = b
            key = check_button(button, label, x, y)
            if key:
                print ("button pressed: %s" % key)
                if key == '=':
                    # do the calculation
                    print ("calculate")
                elif key =='+/-':
                    # change the sign
                    print ("change sign")
                elif key == 'del':
                    # clear current text
                    displayString = ''
                    displayTextElement.undraw()
                    displayTextElement = Text(Point(0, 50), displayString)
                    displayTextElement.draw(win)
                else:
                    # number keys
                    displayString = (displayString + label).rjust(150);
                    displayTextElement.undraw()
                    displayTextElement = Text(Point(0, 50), displayString)
                    displayTextElement.draw(win)

        
main() 
