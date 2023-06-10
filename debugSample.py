word = input('Enter a string: ')
index = 0
newString = ''
while index < len(word):
#     // checking if the current character is z
    if word[index] == 'z':
#         // finding location of p. We are using the z location and finding the next occuring p
        pos = word.find('p', index)
        if pos != -1: # if p exists
            # extracting the part between the z and p
            substring = word[index +1  : pos]
            # checking if substring has z inbetween
            if 'z' in substring:
                # we skip the current z and move to the next one.
                newString += word[index]
                index += 1
            else:
                # if z is not in substring, we delete the substring
                newString += 'zp'
                index = pos + 1
        else:
            # if p doesnt exist after z , moving to the next character.
            newString += word[index]
            index += 1
    else:
#         //if the current character is not z. adding the current character to the newString.
        newString += word[index]
        index += 1
print(newString)