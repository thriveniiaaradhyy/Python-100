d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))

for k in d:
    print("{} has value {}".format(k,d[k]))

# 0r

for k,v in d.items():
    print(k, "has value", v)
