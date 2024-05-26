# this program shows an example of dir function

print(dir())

print(__name__) # prints __main__ showing that we are running the current file.
print(__file__) # prints complete file path.
print(__package__) # if the current file is inside a package, it will display that package.
print(__builtins__)