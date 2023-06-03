# Check if every element is greater than 5.
ratings = {
    'laptop': 7,
    'bread' : 8,
    'toy' : 3,
    'bell' : 2,
    'desk' : 5,
    'tv': 10
}
# cannot diretly use a dictionary with while loop
# convert the dictionary into a list.
items = list(ratings.keys())
start = 0
itemList = []
while start < len(items):
    key = items[start]
    value = ratings[key]
    if value > 5:
        itemList.append(key)
    start += 1
print(itemList)