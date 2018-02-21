#graphical user interface calculator
import graphics
from graphics import *

def create_button(win, x1, y1, x2, y2, label):
    button = Rectangle(Point(x1,y1), Point(x2, y2))
    button.setFill('aquamarine')
    button.draw(win)
    text= Text(button.getCenter(), label)
    text.setFace('arial')
    text.setSize(20)
    text.draw(win)


        
def main():
    win = GraphWin("Calculator", 300, 500)
    displayScreen = Rectangle (Point(10,10), Point(290,110))
        #top rect where numbers will show
    displayScreen.setFill('lightcyan')
    displayScreen.draw(win)
    create_button (win, 8, 115, 73, 187, "7")
    create_button (win, 8, 192, 73, 264, "4")
    create_button (win, 8, 269, 73, 341, "1")
    create_button (win, 8, 346, 73, 418, "+ / -")
    create_button (win, 81, 115, 146, 187, "8")
    create_button (win, 81, 192, 146, 264, "5")
    create_button (win, 81, 269, 146, 341, "2")
    create_button (win, 81, 346, 146, 418, "0")
    create_button (win, 154, 115, 219, 187, "9")
    create_button (win, 154, 192, 219, 264, "6")
    create_button (win, 154, 269, 219, 341, "3")
    create_button (win, 154, 346, 219, 418, ".")
    create_button (win, 154, 423, 219, 495, "d e l")
    create_button (win, 227, 115, 292, 187, "/")
    create_button (win, 227, 192, 292, 264, "*")
    create_button (win, 227, 269, 292, 341, "+")
    create_button (win, 227, 346, 292, 418, "-")
    create_button (win, 227, 423, 292, 495, "=")
    
main() 
