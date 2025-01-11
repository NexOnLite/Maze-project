from random import *

"""
    Notes : ce programme génère un labyrinthe
    où chaque mur est représenté par un "█" et
    chaque chemin est représenté par un "". La gestion
    des erreurs d'entrée n'est pas encore prise en charge
    au même titre que l'algorithme de résolution du labyrinthe.

    MAJ : introduction d'une classe "Maze" qui permet ainsi
    la génération d'autant de labyrinthes que le désire
    l'utilisateur.
"""

class Maze:
    """
    Classe "Maze" permettant la génération et l'affichage d'un labyrinthe. 
    Chaque mur est représenté par un "█" et chaque chemin par un " ".
    Prochaine MAJ : ajout d'une fonction "resolution" permettant la résolution du labyrinthe
    """

    def __init__(self, width, height, id):
        self.width = width
        self.height = height
        self.id = id
        #On crée le labyrinthe à l'aide d'"une liste de listes" - on se contente au départ d'un labyrinthe composé de "█"
        self.maze = [["█" for i in range(width)] for j in range(height)]  
        self.entryCoords = None
        self.exitCoords = None

    #On génère des coordonnées aléatoires d'une cellule placée sur un des 4 murs
    def topBottomWall(self):
        YCoord = choice([0, self.height - 1])
        XCoord = choice(range(1, self.width - 1, 2))  #On incrémente de 2 de sorte à toujours tomber sur une cellule impaire (résérvées aux chemins)
        return XCoord, YCoord

    def leftRightWall(self):
        YCoord = choice(range(1, self.height - 1, 2))  #On incrémente de 2 de sorte à toujours tomber sur une cellule impaire (résérvées aux chemins)
        XCoord = choice([0, self.width - 1])
        return XCoord, YCoord

    def generateMaze(self):

        """
        Cette fonction génère le "corps" du
        labyrinthe avec l'attribution aléatoire 
        d'une entrée et d'une sortie.
        """

        #On génère les coordonnées de l'entrée et de la sortie
        self.entryCoords = choice([self.topBottomWall(), self.leftRightWall()])
        self.exitCoords = choice([self.topBottomWall(), self.leftRightWall()])

        #On "marque" l'entrée et de la sortie sur le labyrinthe, respectivement par "E" et "S"
        self.maze[self.entryCoords[1]][self.entryCoords[0]] = "E"
        self.maze[self.exitCoords[1]][self.exitCoords[0]] = "S"

    def pathGenerator(self):

        """
        Cette fonction permet, comme son nom l'indique,
        de générer les chemins du labyrinthe.
        """

        #On récupère les dimensions du labyrinthe
        width, height = self.width, self.height

        
        def path(x, y):
            """
            Cette fonction permet de marquer
            une cellule comme un chemin, c.a.d, " ".
            """
            self.maze[y][x] = " "

        def notInBorders(x, y):
            """
            Cette fonction vérifie que la cellule n'est pas 
            située sur les bordures (on évite donc d'avoir 
            différentes ouvertures au niveau des bords)
            """
            return 0 < x < width - 1 and 0 < y < height - 1 and self.maze[y][x] == "█"

        #On initialise la liste des cases visitées avec une case de départ
        startXCoord, startYCoord = 1, 1
        CoordsList = [(startXCoord, startYCoord)]
        path(startXCoord, startYCoord)

        #On définit les directions possibles (c.a.d., droite, gauche, haut et bas)
        directionList = [(2, 0), (-2, 0), (0, -2), (0, 2)]

        while CoordsList:
            currentXCoord, currentYCoord = CoordsList[-1]

            #On mélange les directions pour obtenir un labyrinthe aléatoire
            shuffle(directionList)
            foundPath = False

            for directionXCoord, directionYCoord in directionList:
                nextX, nextY = currentXCoord + directionXCoord, currentYCoord + directionYCoord

                if notInBorders(nextX, nextY):
                    #On trace un chemin en deux étapes (entre la case actuelle et la suivante)
                    path(currentXCoord + directionXCoord // 2, currentYCoord + directionYCoord // 2)
                    path(nextX, nextY)

                    #On ajoute la case suivante à la liste
                    CoordsList.append((nextX, nextY))
                    foundPath = True
                    break
            
            #Et si aucune direction n'est valide, alors on revient en arrière
            if not foundPath:
                CoordsList.pop()

    def display(self):

        """
        Cette fonction permet 
        l'affichage du labyrinthe.
        """

        print(f"\nAffichage du labyrinthe n°{self.id}: \n")
        for line in self.maze:
            print("".join(line))

#On affiche d'un message de bienvenue
print("\n" + "#" * 61)
print("Bienvenue dans le résolveur de labyrinthes made in TW3 labs !")
print("#" * 61)

#On initialise quelques variables de base
userChoice = "1"
id = 1

#On crée une (ou de plusieurs) instance(s) de la classe Maze et on génère le labyrinthe
while userChoice == "1":
    widthUserChoice, heightUserChoice = input("\nVeuillez saisir la largeur et la hauteur du labyrinthe (impair - x,y) : ").split(",")
    maze = Maze(int(widthUserChoice), int(heightUserChoice), id)
    maze.generateMaze()
    maze.pathGenerator()
    maze.display()
    print("\n(On suppose que la résolution du labyrinthe a été effectuée.)")
    userChoice = input("\nSouhaitez-vous continuer (1) ou arrêter le programme (0) ? ")
    id += 1
