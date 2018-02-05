# Introduction to Programming
# Author: Susan Cantoni
# Date: 02-05-18

def fib (n):
    a, b = 1, 1
    for i in range (n-1):
        a, b= b, a + b
    return a

def main():
    n = int(input("Enter the Fibonacci term "))
    print (fib (n))

main ()


    
