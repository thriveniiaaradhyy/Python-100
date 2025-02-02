import glob

file_list = glob.glob("letters/*.txt")
l = []
check = "python"

for filename in file_list:
    with open(filename,'r') as file:
        letter = file.read().strip("\n")
        if letter in check:
            l.append(letter)

print(l)
