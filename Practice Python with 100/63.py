import time
i=0

while True:
    i += 1
    if i > 3:
        print("End of Loop")
        break
    print("Hello")
    time.sleep(i)
