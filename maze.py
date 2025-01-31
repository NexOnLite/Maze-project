from config import State, Coord, EMPTY, WALL

class Maze:
    def __init__(self, grid: list[list[int]], start: Coord, finish: Coord):
        self.grid = grid
        self.start = start
        self.finish = finish
        self.width = len(grid[0])  # Largeur du labyrinthe
        self.height = len(grid)    # Longueur du labyrinthe

    def is_valid_coord(self, coord: Coord) -> State:
        x, y = coord
        return 0 <= x < self.width and 0 <= y < self.height and self.grid[y][x] == EMPTY

    def print(self) -> None:
        # Affichage du labyrinthe
        for row in self.grid:
            print(''.join(['██' if cell == WALL else '  ' if cell == EMPTY else "S" for cell in row]))
            
    def __str__(self) -> str:
        res = ""
        for row in self.grid:
            res += ''.join(['██' if cell == WALL else '  ' if cell == EMPTY else "S" for cell in row]) + '\n'
        return res[:-1]
    
    def __add__(self, other: "Maze") -> "Maze":
        return Maze(self.grid + other.grid, self.start, self.finish)
        
