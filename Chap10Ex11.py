import sys

# command line arguments

print(sys.argv) # prints command line arguments

# program to convert temperature
if len(sys.argv) != 3:
    print("Invalid number of arguments. The arguments are type if the temperature with a minus(-) and the actual temerature.")
else:
    units = sys.argv[1]
    if sys.argv[2].isdecimal():
        temp = float(sys.argv[2])
        if units == "-c":
            print((9 / 5) *temp  + 32 , "F")
        elif units == '-f':
            print((temp - 32) * 5 / 9 , "C")
        else:
            print('invalid units.')
    else:
        print("The temperature should be a number")

