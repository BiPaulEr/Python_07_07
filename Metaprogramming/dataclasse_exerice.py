from dataclasses import dataclass, field

@dataclass(order=True)
class Produit:
    nom : str = field(compare=False)
    prix : float = field(repr=False)
    categorie : str
    quantite_stock: int = field(init=False)

    def __post_init__(self):
        self.quantite_stock = 0

produit1 = Produit("Produit A", 20.0, "Electronique")
produit2 = Produit("Produit B", 10.0, "Maison")
produit3 = Produit("Produit C", 20.0, "Electronique")

print(produit1)
print(produit1 <  produit2)
print(produit1 == produit3)

