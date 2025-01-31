from maze_generator import MazeGenerator
from maze import Maze

def main() -> None:
    maze_list = []
    user_choice = "1"

    print(
        "\n" + "#" * 61 + "\n"
        "Bienvenue dans le résolveur de labyrinthes made in TW3 labs !" + "\n" +
        "#" * 61 + "\n"
        )

    while user_choice:
        width, height = map(int, input("\nVeuillez saisir la largeur et la hauteur du labyrinthe (impair - x,y) : ").split(","))

        maze_generator = MazeGenerator(width, height)
        grid, start, finish = maze_generator.generate()
        maze = Maze(grid, start, finish)
        print(maze)

        maze_list.append(maze)

        user_choice = True if input("\nSouhaitez-vous continuer (1) ou arrêter le programme (0) ? ") == "1" else False

if __name__ == "__main__":
    main()