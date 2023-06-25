mylist = [1,2, 5,6,7, 9, 10, 11, 12, 20]
largestLength = 1
start = 0
while start < len(mylist)-1:
    start2 = start
    count= 1
    while start2 < len(mylist):
        val1 = mylist[start2]
        val2 = mylist[start2 + 1]
        if val2  == val1 + 1:
            count += 1
        else:
            if count > largestLength:
                largestLength = count
                count = 1
                start = start2
                break
        start2 += 1
    start += 1
print(largestLength)