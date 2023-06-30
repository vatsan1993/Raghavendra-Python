word = input('Enter a word: ')
index = 0
newString = ''
pos = 0
pos2 = 0
found = False
while index < len(word):
    if word[index: index + 5] == 'bread':
        pos = index + 5
        pos2 = pos
        while pos2 < len(word) - 4:
            if word[pos2: pos2 + 5] == 'bread':
                found = True
                break
            pos2 += 1
        if found:
            break
    index += 1

if found:
    print(word[pos: pos2])
else:
    print("Not a sandwitch")