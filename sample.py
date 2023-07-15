
def changeList2(data):# data = @ 840
    l2 = data.copy() #l2 = @ 920
    print(f'The data inside the function before change {data}')
    l2[0] = 100
    print(f'The data inside the function after change {data}')
l1 = [1,2,3] # @ 840
print('before calling function',l1)
changeList2(l1)
print('after calling function',l1)