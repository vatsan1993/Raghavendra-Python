import itertools

# count method - generates a list from a starting value and with a step
cnt = itertools.count(2, 2)
print([ next(cnt) for i in range(10)])



# compress method
# returns a new list that contains the values corresponding to True

students = ['Max', 'Mike', 'Jake']
passed = [False, True, False]

print(list(itertools.compress(students, passed)))


# dropwhile
# drops all values until condition becomes false

sales = [2,3,4,5,4,6,434,6,34,4]
# def drop_less_sales(sale):
#     return sale < 5

# result_iter = itertools.dropwhile(drop_less_sales, sales)
result_iter = itertools.dropwhile(lambda sale : sale < 5, sales)

print(list(result_iter))



# filterfalse

result_iter = itertools.filterfalse(lambda sale : (sale < 5), sales)
print(list(result_iter))



sales = {
    "NY": 10,
    'DC': 20,
    'TX': 5,
    'AL': 3
}

result_iter = itertools.filterfalse(lambda sale : (sale[1] <= 5), sales.items())
print(list(result_iter))


# permutations
names = ['Max', 'Mike', 'Jake', 'James', 'Blake', 'Jackson']
print(list(itertools.permutations(names, 4)))

#combination
print(list(itertools.combinations(names, 3)))
