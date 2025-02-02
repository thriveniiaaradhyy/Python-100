a = [1, 2, 3]

for i in range(len(a)):
    print("item " + str(a[i]) + " has index " + str(i))
# or
for index,item in enumerate(a):
    print("Item %s has index %s" %(item,index))
