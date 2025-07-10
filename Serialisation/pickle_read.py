import pickle, os

with open(os.path.join(os.path.dirname(__file__),"biblio.stock"), "rb") as file:
    bibliotheque = pickle.load(file)
print(bibliotheque)
