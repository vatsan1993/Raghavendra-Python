# most important things are imported or directly created here.
"""
We can use the find_value directly instead of importing from the pak_mod
We have 2 other components that we can directly import
1. b = 200
2. sum_three_multiples: adds multiples of 3
"""


from package1.pak_mod import find_value

b = 200

def sum_three_multiples(lst):
    """
    adds multiples of 3
    :param lst: a list
    :return: the total
    """
    total = 0
    for val in lst:
        if val % 3 == 0:
            total += val
    return total