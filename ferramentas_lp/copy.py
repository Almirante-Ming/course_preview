from dataclasses import make_dataclass
from copy import copy, deepcopy
 
Point = make_dataclass("Point", ("x", "y"))
 
original = [Point(0, 5), Point(-3, 6)]
reference = original
shallowcopied1 = original.copy()
shallowcopied2 = copy(original)
deepcopied = deepcopy(original)
 
original.append(Point(0, 0))
original[0].x, original[0].y = 1, 1
 
print("Original Points:      ", original)
print("Reference Points:     ", reference)
print("Shallow Copied Points:", shallowcopied1)
print("Also Shallow Copy:    ", shallowcopied2)
print("Deep Copied Points:   ", deepcopied)
