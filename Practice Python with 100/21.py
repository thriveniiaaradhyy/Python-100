d = {"a": 1, "b": 2, "c": 3}

d = dict((k,v) for k,v in d.items() if v <= 1)
print(d)

'''
Explanation:

Here we're using a dictionary comprehension. The comprehension is the expression inside dict() . The comprehension iterates through the existing dictionary items, and if an item is less or equal to 1, the item is added to a new dict. This new dict is assigned to the existing variable d  , so we end up with a filtered dictionary in d.
'''
