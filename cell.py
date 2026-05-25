class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.bomb = False
        self.neighbors = []
        self.adjacent_bombs = 0
        self.flagged = False
        self.opened = False
        self.symbol = "-"
        self.update_symbol()

    def open(self):
        if self.bomb:
            return False
        self.opened = True
        for neighbor in self.neighbors:
            neighbor.update()
        self.update()
        return True

    def set_bomb(self):
        self.bomb = True

    def is_bomb(self):
        return self.bomb

    def flag(self):
        self.flagged = True
        self.update_symbol()

    def unflag(self):
        self.flagged = False

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def count_adjacent_bombs(self):
        self.adjacent_bombs = sum(1 for n in self.neighbors if n.is_bomb())

    def has_opened_neighbor(self):
        return any(n.is_opened() for n in self.neighbors)

    def is_opened(self):
        return self.opened

    def get_symbol(self):
        return self.symbol

    def update_symbol(self):
        if self.flagged:
            self.symbol = "¤"
        elif self.opened and not self.bomb:
            self.symbol = f"{self.adjacent_bombs}"
        elif self.has_opened_neighbor() and not self.bomb:
            self.symbol = f"{self.adjacent_bombs}"
        else:
            self.symbol = "-"

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def update(self):
        self.count_adjacent_bombs()
        self.update_symbol()

    def get_neighbors(self):
        return self.neighbors

    def __str__(self):
        return f"{self.x},{self.y}"
