print("**************************")
print("*        Rene Özbay      *")
print("*        Formeln         *")
print("*         App17b         *")
print("**************************")

import math

p = int(input("Geben sie eine Zahl für P ein: "))
q = int(input("Geben sie eine Zahl für Q ein: "))

sqrt = p ** 2 / 4 - q

if (sqrt > 0):
    x1 = (-p / 2 + math.sqrt(sqrt))
    x2 = (-p / 2 - math.sqrt(sqrt))
    print(x1)
    print(x2)
elif (sqrt == 0):
    x = (-p / 2)
    print(x)
else:
    sqrt = sqrt * (-1)
    x = -p / 2
    wz = math.sqrt(sqrt)
    print("x1 = " + str(x) + " + i " + str(wz))
    print("x2 = " + str(x) + " - i " + str(wz))
