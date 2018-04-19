#Intro to Programming
#Working with Objects
#Author: Susan Cantoni
#Date: 04-17-18

class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def checkStock(self, count):
        if self.quantity >= int(count):
            return True
        else:
            return False

    def totalCost(self,count):
        totalCost = int(count) * self.price
        return totalCost

    def updateQuantity(self,count):
        self.quantity = self.quantity - int(count)
        return self.quantity
        

        
def printStock(products):
    print()
    print("Available Products")
    print("------------------")
    n = 0
    for p in products:
        if p.quantity > 0:
            print(n, p.name, "$", p.price)
        n += 1
    print()
    
def main():
    products = [
        Product("Ultrasonic range finder", 2.50, 4),
        Product("Servo motor", 14.99, 10),
        Product("Servo controller", 44.95, 5),
        Product("Microcontroller Board", 34.95, 7),
        Product("Laser range finder", 149.99, 2),
        Product("Lithium polymer battery", 8.99, 8)
        ]

    cash = float(input("How much money do you have? $"))
    while cash > 0:
        printStock(products)
        
        vals = input("Enter product ID and quantity you wish to buy: ").split(" ")

        if vals[0] == "quit": break

        prodId = int(vals[0])
        product = products[prodId]
        count = int(vals[1])

        if product.checkStock(count):
            if cash >= product.totalCost(count):
                product.updateQuantity(count)
                cash -= product.totalCost(count)
                print ("You purchased", count, product.name+".")
                print ("You have $", "{0:.2f}".format(cash), "remaining.")
            else:
                print("Sorry, you cannot afford that product.")
        else:
            print("Sorry, we are sold out of", product.name)

main()

