import os
from PIL import Image

def listeImages(dossier):
    for fichier in os.listdir(dossier):
        if fichier.endswith((".png", ".jpg")):
            yield os.path.join(dossier, fichier)

def loadImages(dossier):
    for path in listeImages(dossier):
        yield Image.open(path)

def loadImagesToList(dossier):
    liste = []
    for path in listeImages(dossier):
        liste.append(Image.open(path))
    return liste

dossier = "C:/Users/PaulE/Documents/DataSet/AbstractArt"
for index, img in enumerate(loadImagesToList(dossier)):
    img.save(os.path.join(dossier, "test", f"{index}.jpg"))