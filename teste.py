import tkinter as tk
from PIL import Image, ImageTk

def afficher_image(nom_fichier):
    root = tk.Tk()
    root.title("Visionneuse d'images")

    # Chemin complet vers l'image, qui se trouve dans le sous-dossier 'output'
    chemin_complet = "output/" + nom_fichier

    # Chargement de l'image en utilisant Pillow
    image = Image.open(chemin_complet)
    photo = ImageTk.PhotoImage(image)

    # Création d'un widget Label pour afficher l'image
    label = tk.Label(root, image=photo)
    label.image = photo  # Garde une référence de l'image
    label.pack()

    # Démarrage de la boucle principale de l'interface graphique
    root.mainloop()

# Nom du fichier image
nom_fichier = "image.jpg"

# Appel de la fonction pour afficher l'image
afficher_image(nom_fichier)
