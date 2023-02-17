class Piece:
    def __init__(self, x, y, player, name, alive):
        self.x = x
        self.y = y
        self.player = player
        self.name = name
        self.alive = alive

    def allowed_moves2cards(self, board, card1, card2):
        allowed_moves = []
        for dx, dy in card1.moves + card2.moves:
            new_x, new_y = self.x + dx, self.y + dy
            if 0 <= new_x < board.rows and 0 <= new_y < board.columns:
                allowed_moves.append((new_x, new_y))
        return allowed_moves

    def allowed_moves1card(self, board, card1):
        allowed_moves = []
        for dx, dy in card1.moves:
            new_x, new_y = self.x + dx, self.y + dy
            if 0 <= new_x < board.rows and 0 <= new_y < board.columns:
                allowed_moves.append((new_x, new_y))
        return allowed_moves

    def killPeace(self):
        self.alive = False
    
    def move(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getPlayer(self):
        return self.player

    def getName(self):
        return self.name

    def getAlive(self):
        return self.alive

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

class King(Piece):
    def __init__(self, x, y, player, name, alive):
        super().__init__(x, y, player, name, alive)

class Pawn(Piece):
    def __init__(self, x, y, player, name, alive):
        super().__init__(x, y, player, name, alive)

