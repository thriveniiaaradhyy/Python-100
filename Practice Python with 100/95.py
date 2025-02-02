data = input("Enter values: ")
data_list = data.split(",")

with open("user_data.txt",'a+') as file:
    for i in data_list:
        file.write(i + "\n")
