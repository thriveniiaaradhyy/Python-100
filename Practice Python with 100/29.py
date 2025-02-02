from math import pi
def volumec(h,r=10):
    a = ((4 * pi * r**3) / 3) - (pi * h**2 * (3 * r - h)  / 3)
    return a

print(volumec(2))
