# Intro to Programming
# Author: Susan Cantoni
# Date: 02-08-18

# approximate the value of pi

def main():
    n = int(input("Enter the amount of terms to use:"))
    pi = 0
    sign = 1
    for i in range (1, n * 2 + 1, 2):
        term = 4/i * sign
        pi = pi + term
        sign = sign * -1
    print( "The approximate value of pi is", pi)

main() 
