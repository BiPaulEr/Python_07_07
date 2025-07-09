from dataclasses import dataclass, field

@dataclass(order=True)
class VectorDataclass:
    x : int = field(compare=False, repr=False)
    y : int
    z : int = field(default = 60)
    somme: int = field(init =  False)

    def __post_init__(self):
        self.somme = self.x + self.y + self.z


vector10 = VectorDataclass(9, 7)
vector11 = VectorDataclass(6, 8)
vector12 = VectorDataclass(12, -5)
print(vector10 < vector12 )
print(vector10)