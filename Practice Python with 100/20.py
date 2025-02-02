d = {"a": 1, "b": 2, "c": 3}

print(sum(d.values()))

# or

d = {"a": 1, "b": 2, "c": 3}
s = 0
for k in d:
     s += d[k]

print(s)
