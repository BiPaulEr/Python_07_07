class Vector(object):
     def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

     def __repr__(self):
         return f"<Vector: x={self.x}, y={self.y}, z={self.z},>"
     def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

vector1 = Vector(1, 2, 3)
vector2 = Vector(1, 2, 3)
print(vector1) #<__main__.Vector object at 0x000001762A36C9B0>
#<Vector: x=1, y=2>
print(vector1 == vector2)
print(Vector.__dict__)
print(vector1.__dict__)
from dataclasses import dataclass

@dataclass
class VectorDataclass:
    x : int
    y : int 
    z : int

print(VectorDataclass.__dict__)
vector10 = VectorDataclass(6, 7, 8)
vector11 = VectorDataclass(6, 7, 8)

print(vector11)
print(vector10 == vector11)