bibliotheque = {"arbre" : 3, "oiseau" : "Gateur"}

import pickle, os

with open(os.path.join(os.path.dirname(__file__),"biblio.stock"), "wb") as file:
    pickle.dump(bibliotheque, file)
