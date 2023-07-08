a = 10  # global variable
def sampleFunction(b):
    c = 20 # b and c are local
    print(a) # no proble
    print(b) # no problem
    print(c) # no problem
print(a) # no problem
sampleFunction(40)
print(b) # error
print(c) # error



# def func1():
#     a = 10
#
# def func2():
#     func1()
#
# def func3():
#     func2()
#
# func3()
