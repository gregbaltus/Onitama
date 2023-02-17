import Model.Board as Board

class View:
    def __init__(self, board):
        self.board = board

    def displayBoard(self):
        print(" ", end=" ")
        for i in range(self.board.getColumns()):
            print(f' {i} ' , end=" ")
        print("")

        for i in range(self.board.getRow()):
            print(i, end=" ")
            for j in range(self.board.getColumns()):
                piece = self.board.get_PieceAt(i, j)
                if piece is None:
                    print(" - ", end=" ")
                else:
                    print(piece.getName(), end=" ")
            print("\n")

    def display_card(self, card):
        moves = card.moves
        board = [['-' for i in range(5)] for j in range(5)]
        board[2][2] = 'P'
        for move in moves:
            x, y = move
            board[2 + x][2 + y] = 'O'
        print(f"{card.getName()}")
        for row in board:
            print(" ".join(row))
        print("\n")