import sys

n = len(sys.argv)

if (n > 2):
    sys.exit("AssertionError: more than one argument are provided")
elif (not sys.argv[1].isdigit()):
    sys.exit("AssertionError: argument is not an integer")

number = int(sys.argv[1])

if (number == 0):
    print("I'm Zero.")
elif (number % 2 == 0):
    print("I'm Even.")
elif (number % 2 != 0):
    print("I'm Odd.")