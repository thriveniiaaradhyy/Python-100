with open("urls.txt",'r') as file:
    lines = file.readlines()

with open("urls_corrected.txt",'w') as file:
        for line in lines:
            line_remove_s = line.replace("s","",1)
            print(line_remove_s)
            line_remove_s_add_slash = line_remove_s[:6] + "/" + line_remove_s[6:]
            print(line_remove_s_add_slash)
            file.write(line_remove_s_add_slash)
