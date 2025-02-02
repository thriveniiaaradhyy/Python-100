my_range = range(10, 201,10)
print(list(my_range))

my_range2 = range(1,21)
print([10*x for x in my_range2])
# or
print(list(10*x for x in my_range2))
