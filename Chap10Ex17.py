import functools

# print(dir(functools))

# partial function
# partial works like a closure.
# where the parent function's value is taken by the child.

def power(a, b):
    return a ** b

pow2 = functools.partial(power, b = 2)
print(pow2(5))
print(pow2(10))

pow5 = functools.partial(power, b = 5)
print(pow5(10))
print(pow5(7))


def mult(a, b):
    return a * b

mult5 = functools.partial(mult, b = 5 )

for i in range(1, 11):
    print(f'{i} * 5 = {mult5(i)}')


# the partial function simplifies the following closure
# def partial_mult(b):
#     def mult(a):
#         return a * b
#     return mult
#
# mult10 = partial_mult(10)


# partialmethod() is used inside a class. But it works similar to the partial().


