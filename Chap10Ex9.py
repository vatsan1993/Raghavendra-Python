# importing and using components of the package

# method1
# import package1
# print(package1.b)
#
# print(package1.find_value([2,5,36,36,34,53,4,4,7,634], 4))

# method2
from package1 import b, find_value

print(b)
print(find_value([2,5,36,36,34,53,4,4,7,634], 4))


# importing from the pack_mod module which is inside the package
# method1
# from package1 import pak_mod
# print(pak_mod.random_value)
# print(pak_mod.add_odds([3,6,2,4,6,8,4,3]))


# method2
from package1.pak_mod import random_value, add_odds

print(random_value)
print(add_odds([3,6,2,4,6,8,4,3]))