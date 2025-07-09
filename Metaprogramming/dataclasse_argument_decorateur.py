from dataclasses import dataclass, field

@dataclass(frozen=True, order=True)
class VectorDataclass:
    x : int
    y : int
    z : int = field(default = 60)

print(VectorDataclass.__dict__)
vector10 = VectorDataclass(9, 7)
print(vector10) #VectorDataclass(x=9, y=7, z=60)
vector11 = VectorDataclass(6, 7, 8)
vector12 = VectorDataclass(8, 7, 8)

print(vector11)

print(vector10 <  vector12)