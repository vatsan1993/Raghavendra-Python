from math import pi, pow
print(dir())

radius = 10
area = pi * pow(radius, 2)
print(area)

# if a compoenent is a normal variable or a function, we dont need to use dir
# dir can be used on classes, packages, modules.
print(dir(pi))
print(dir(pow))