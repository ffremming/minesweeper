from random import randint

from cell import Cell


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.bomb_count = 0
        self.grid = self._build()
        self._link_neighbors()
        self.score = 0
        self.game_over = False

    def _build(self):
        rows = []
        for y in range(self.height):
            row = []
            for x in range(self.width):
                cell = Cell(x, y)
                if randint(0, 2) == 1:
                    cell.set_bomb()
                    self.bomb_count += 1
                row.append(cell)
            rows.append(row)
        return rows

    def _link_neighbors(self):
        for row in self.grid:
            for cell in row:
                self._attach_neighbors(cell)

    def _attach_neighbors(self, cell):
        x, y = cell.get_x(), cell.get_y()
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    cell.add_neighbor(self.get_cell(nx, ny))

    def get_cell(self, x, y):
        return self.grid[y][x]

    def draw(self):
        print("\n\n\n\n\n")
        print("score:", self.score)
        print("  ", end="")
        for x in range(self.width):
            print(f"{x:02}", end="  ")
        print("\n")
        for y, row in enumerate(self.grid):
            print(y, end=" ")
            for cell in row:
                print(cell.get_symbol(), end="   ")
            print("\n")

    def guess(self, x, y):
        cell = self.grid[y][x]
        if not cell.is_opened():
            self.score += 1
        if not cell.open():
            self.game_over = True

    def flag(self, x, y):
        self.grid[y][x].flag()

    def is_game_over(self):
        return self.game_over

    def end_game(self):
        self.game_over = True
        self.score = self.bomb_count

    def get_score(self):
        return self.score

    def all_bombs_flagged(self):
        for row in self.grid:
            for cell in row:
                if cell.is_bomb() and cell.get_symbol() != "¤":
                    return False
        return True
