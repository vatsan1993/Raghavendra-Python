import random

grocery_list = ['Apple', 'bananas', 'oranges']
print(random.random())
print(random.randint(1, 10))
print(random.uniform(3.5, 5.4))
print(random.choice(grocery_list))
random.shuffle(grocery_list)
print(grocery_list)


mylist= [4.6,3,7,45,354,5,6,35,67,4]

print(random.sample(mylist, 3))