import Model.MyPiece as Piece

class Board:
    def __init__(self, rows, columns):

        self.rows = rows
        self.columns = columns
        self.board = [[None for i in range(rows)] for i in range(columns)]

    def initPieceBoard(self, listPiece):
        for piece in listPiece:
            self.board[piece.x][piece.y] = piece

    def place_piece(self, piece, x, y):
        if x >= 0 and x < self.rows and y >= 0 and y < self.columns:
            self.board[piece.getX()][piece.getY()] = None
            self.board[x][y] = piece
            piece.x = x
            piece.y = y
        else:
            raise ValueError("Invalid coordinates for placing piece")



    def isAllyAt(self, pieces, player, x, y):
        for piece in pieces:
            if piece.getX() == x and piece.getY() == y and piece.getPlayer() == player:
                return True
        return False

    def isOpponentAt(self, pieces, opponnentplayer, x, y):
        for piece in pieces:
            if piece.getX() == x and piece.getY() == y and piece.getPlayer() == opponnentplayer.getName():
                return True
        return False

    def get_PieceAt(self, row, column):
        return self.board[row][column]

    def set_square(self, row, column, value):
        self.board[row][column] = value

    def display(self):
        for row in self.board:
            print(" ".join(str(x) for x in row))

    def getRow(self):
        return self.rows

    def getColumns(self):
        return self.columns