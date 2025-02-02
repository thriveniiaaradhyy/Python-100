def my_function(filepath):
    with open(filepath , 'r') as file:
        text = file.read()
        words = text.split(" ")
        return len(words)

print(my_function("words1.txt"))
