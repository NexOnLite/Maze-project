from random import shuffle, choice
from config import WALL, EMPTY,PATH, Coord, State

class MazeGenerator:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def generate(self) -> tuple[list[list[int]], Coord, Coord]:
        # on crée une grille vide
        grid = [[WALL for _ in range(self.width)] for _ in range(self.height)]
        
        def randomly_choose_bottom_or_top_wall(self) -> Coord:
            """
            Cette fonction choisit une position 
            aléatoire sur le mur du bas ou du haut
            """
            y = choice([0, self.height - 1])
            x = choice(range(1, self.width - 1, 2))  #On incrémente de 2 de sorte à toujours tomber sur une cellule impaire (résérvées aux chemins)
            return (x, y)

        def randomly_choose_left_or_right_wall(self) -> Coord:
            """
            Cette fonction choisit une position 
            aléatoire sur le mur droit ou gauche
            """
            y = choice(range(1, self.height - 1, 2))  #On incrémente de 2 de sorte à toujours tomber sur une cellule impaire (résérvées aux chemins)
            x = choice([0, self.width - 1])
            return (x, y)

        def path(coord: Coord):
            """
            Cette fonction permet de marquer
            une case comme un chemin, c.a.d, "EMPTY"
            """
            x, y = coord
            grid[y][x] = EMPTY

        def are_coords_valid(self, coord: Coord) -> State:
            """
            Cette fonction vérifie qu'une case
            est située à l'intérieur du labyrinthe
            et sur un mur
            """
            x, y = coord
            return 0 < x < self.width - 1 and 0 < y < self.height - 1 and grid[y][x] == WALL

        start_coords = choice([randomly_choose_bottom_or_top_wall(self), randomly_choose_left_or_right_wall(self)])
        finish_coords = choice([randomly_choose_bottom_or_top_wall(self), randomly_choose_left_or_right_wall(self)])

        #On "marque" l'entrée et de la sortie sur le labyrinthe, respectivement par "S" pour "start" et "F" pour "finish"
        grid[start_coords[1]][start_coords[0]] = EMPTY
        grid[finish_coords[1]][finish_coords[0]] = EMPTY

        # Implémentationn ici
        coords_list = [(1,1)]
        path((1,1))

        #On définit les directions possibles (c.a.d., droite, gauche, haut et bas)
        direction_list = [(2, 0), (-2, 0), (0, -2), (0, 2)]

        while coords_list:
            
            current_x, current_y  = coords_list[-1]

            #On mélange les directions pour obtenir un labyrinthe aléatoire
            shuffle(direction_list)
            has_a_path_been_found = False

            for direction_coords in direction_list:
                direction_x, direction_y = direction_coords
                next_coords = (current_x + direction_x, current_y + direction_y)

                if are_coords_valid(self, next_coords):
                    #On trace un chemin en deux étapes (entre la case actuelle et la suivante)
                    path((current_x + direction_x // 2, current_y + direction_y // 2))
                    path(next_coords)

                    #On ajoute la case suivante à la liste
                    coords_list.append(next_coords)
                    has_a_path_been_found  = True
                    break
            
            #Et si aucune direction n'est valide, alors on revient en arrière
            if not has_a_path_been_found:
                x, y = coords_list[-1]
                grid[y][x] = EMPTY
                coords_list.pop()
    
        return grid, start_coords, finish_coords