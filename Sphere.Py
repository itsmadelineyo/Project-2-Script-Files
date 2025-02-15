>>> import math
>>> radius = float(input("Radius = "))
Radius = 5
>>> diameter = 2 * radius
>>> circumference = diameter * math.pi
>>> surf_area = 4 * math.pi * radius**2
>>> volume = (4/3) * math.pi * radius**3
>>> print()

>>> print("%-13s: " %("Diameter"), end = "")
>>> Diameter:6
>>> print("%-13s: " %("Circumference"), end = "")
>>> Circumference: 4
>>> print("%-13s: " %("Surface area"), end = "")
>>> Surface area: 3
  File "<python-input-12>", line 1
    Surface area: 3
            ^^^^
SyntaxError: invalid syntax
>>> print("%-13s: " %("Volume"), end = "")
>>> Volume: 4
>>> =
  File "<python-input-15>", line 1
    =
    ^
SyntaxError: invalid syntax
>>>
