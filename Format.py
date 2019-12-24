#This program will show several different ways of formatting using the .format

import random

def main():
    print ("Hello {0} {1}, you may have won ${2}".format ("Mr.", "Smith",10000))

    print ("This int, {0:5}, was placed in a field of width 5".format(7))

    print ("This int, {0:10}, was placed in a field of width 10".format(7))

    print ("This float, {0:10.5} has a width of 10 and a percision of 5" .format(3.1415926))

    print ("This float, {0:10.5f} is fixed at 5 decimal places".format(3.1415926))

    print ("This float, {0:0.5} has a width of 0 and a precision of 5".format(3.1415926))

    print ("Compare {0} and {0:0.20}".format(3.14))


main()
