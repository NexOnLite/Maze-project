"""
  Notes :
  Le programme génère pour l'instant un labyrinthe "vide"
  et positionne son entrée ainsi que sa sortie, respectivement
  indiquées par "E" et "S".
"""

from random import choice, randint

def mazeGenerator(width, height):
    
    #Création du labyrinthe
    maze = [[" " for i in range(width)] for i in range(height)]

    #Génération des murs
    for i in range(height):
        maze[i][0] = "#" #Création du mur gauche
        maze[i][width - 1] = "#" #Création du mur droit

    for j in range(width):
        maze[0][j] = "#" #Création du mur du haut
        maze[height - 1][j] = "#" #Création du mur du bas

    #Génération des coordonnées de l'entrée et de la sortie du labyrinthe
    def topBottomWall():
        YCoord = choice([0, height - 1])
        XCoord = randint(1, width - 2)
        return XCoord, YCoord

    def leftRightWall():
        YCoord = randint(1, height - 2)
        XCoord = choice([0, width - 1])
        return XCoord, YCoord

    entryXCoord, entryYCoord = choice([topBottomWall(), leftRightWall()])
    exitXCoord, exitYCoord = choice([topBottomWall(), leftRightWall()])

    #Affichage de l'entrée et de la sortie sur le labyrinthe
    maze[entryYCoord][entryXCoord] = "E"
    maze[exitYCoord][exitXCoord] = "S"

    #Affichage du labyrinthe
    for line in maze:
        print("".join(line))

#Demande des dimensions à l'utilisateur
widthUserChoice = int(input("Veuillez saisir la largeur du labyrinthe : "))
heightUserChoice = int(input("Veuillez saisir la hauteur du labyrinthe : "))

mazeGenerator(widthUserChoice, heightUserChoice)
