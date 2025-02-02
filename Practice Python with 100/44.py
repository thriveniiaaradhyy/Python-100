import string
s = string.ascii_lowercase+" "
with open("letters-3-by-3.txt",'w') as file:
    for letter1, letter2, letter3 in zip(s[0::3],s[1::3],s[2::3]):
        file.write(letter1 + letter2 + letter3 + "\n")
