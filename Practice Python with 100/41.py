import string
file = open("lettersinfile.txt",'w')

for i in string.ascii_uppercase:
    file.write(i + "\n")

file.close()

#  or

with open("lettersfile.txt",'w') as file:
    for i in string.ascii_uppercase:
        file.write(i + "\n")
