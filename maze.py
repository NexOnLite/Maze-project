from random import *

"""
    Notes : ce programme génère un labyrinthe
    où chaque mur est représenté par un "█" et
    chaque chemin est représenté par un "". La gestion
    des erreurs d'entrée n'est pas encore prise en charge
    au même titre que l'algorithme de résolution du labyrinthe.
"""

def mazeGenerator(width, height):
    #On crée le labyrinthe à l'aide d'"une liste de listes" - on se contente au départ d'un labyrinthe composé de "█"
    maze = [["█" for i in range(width)] for j in range(height)]

    #On génère les coordonnées de l'entrée et de la sortie du labyrinthe
    def topBottomWall():
        YCoord = choice([0, height - 1])
        XCoord = choice(range(1, width - 1, 2))  #Toujours sur une cellule impaire
        return XCoord, YCoord

    def leftRightWall():
        YCoord = choice(range(1, height - 1, 2))  #Toujours sur une cellule impaire
        XCoord = choice([0, width - 1])
        return XCoord, YCoord

    entryCoords = choice([topBottomWall(), leftRightWall()])
    exitCoords = choice([topBottomWall(), leftRightWall()])

    # Marquer l'entrée et la sortie
    maze[entryCoords[1]][entryCoords[0]] = "E"
    maze[exitCoords[1]][exitCoords[0]] = "S"

    return maze, entryCoords

def pathGenerator(maze):
    #On récupère les dimensions du labyrinthe
    width, height = len(maze[0]), len(maze)

    #On marque une cellule comme chemin
    def path(x, y):
        maze[y][x] = " "

    #On vérifie que la cellule n'est pas située sur les bordures (on évite donc d'avoir différentes ouvertures au niveau des bods)
    def notInBorders(x, y):
        return 0 < x < width - 1 and 0 < y < height - 1 and maze[y][x] == "█"

    #On initialise la liste des cases visitées avec une case de départ
    startXCoord, startYCoord = 1, 1
    CoordsList = [(startXCoord, startYCoord)]
    path(startXCoord, startYCoord)

    #On définit les directions possibles (c.a.d., droite, gauche, haut et bas)
    directionList = [(2, 0), (-2, 0), (0, -2), (0, 2)]

    while CoordsList:
        currentXCoord, currentYCoord = CoordsList[-1]

        #On mélange les directions pour un labyrinthe aléatoire
        shuffle(directionList)
        foundPath = False

        for directionXCoord, directionYCoord in directionList:
            nextX, nextY = currentXCoord + directionXCoord, currentYCoord + directionYCoord

            if notInBorders(nextX, nextY):
                #On creuse un chemin en deux étapes (entre la case actuelle et la suivante)
                path(currentXCoord + directionXCoord // 2, currentYCoord + directionYCoord // 2)
                path(nextX, nextY)

                #On ajoute la case suivante à la liste
                CoordsList.append((nextX, nextY))
                foundPath = True
                break

        #Et si aucune direction n'est valide, alors on revient en arrière
        if not foundPath:
            CoordsList.pop()

#On affiche un message de bienvenue
print("\n" + "#" * 71)
print("Bienvenue dans le résolveur de labyrinthes made in TW3 labs !")
print("#" * 71, "\n")

#On demande les dimensions à l'utilisateur
widthUserChoice, heightUserChoice = input("Veuillez saisir la largeur et la hauteur du labyrinthe (impair - x,y) : ").split(",")

#On génère et affiche le labyrinthe
maze, entryCoords = mazeGenerator(int(widthUserChoice), int(heightUserChoice))
pathGenerator(maze)

print("\nAffichage du labyrinthe : \n")
for line in maze:
    print("".join(line))
