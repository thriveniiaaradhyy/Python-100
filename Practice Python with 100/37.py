def my_function(filepath):
    with open(filepath , 'r') as file:
        text = file.read()
    text = text.replace(","," ")    
    words = text.split(" ")
    return len(words)

print(my_function("words2.txt"))
