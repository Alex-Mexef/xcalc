#My first calculator on Python
import math

what = input("What to do? (+, - ): ")

a = float( input("Put first numeral:") )
b = float( input("Put second numeral:") )

if what =="+":
    c = a + b
    print("Result: " + str(c))
elif what == "-":
    c = a - b
    print("Result: " + str(c))
else:
    print("Wrong operation!")
