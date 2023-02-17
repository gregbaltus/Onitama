import Model.Board as Board
import Model.MyPiece as Piece
import Model.Agent.AgentHumain as AgentHumain
import Model.Agent.AgentRandomIA as AgentRandomIA
import View.View as View



class Game:
    def __init__(self, cardList, mode):
        self.board = Board.Board(5, 5)

        #first = bool(random.getrandbits(1))
        self.namePlayer1 = 'R'
        self.namePlayer2 = 'B'

        if mode == "2players":
            self.redPlayer = AgentHumain.AgentHumain(self.namePlayer1, True)
            self.bluePlayer = AgentHumain.AgentHumain(self.namePlayer2, False)
        if mode == "vsRandomIA":
            self.redPlayer = AgentHumain.AgentHumain(self.namePlayer1, True)
            self.bluePlayer = AgentRandomIA.AgentRandomIA(self.namePlayer2, False)

        self.kingJ1 = Piece.King(0, 2, self.namePlayer1, 'Rk', True)
        self.pawn1J1 = Piece.Pawn(0, 0, self.namePlayer1, 'Rp1', True)
        self.pawn2J1 = Piece.Pawn(0, 1, self.namePlayer1, 'Rp2', True)
        self.pawn3J1 = Piece.Pawn(0, 3, self.namePlayer1, 'Rp3', True)
        self.pawn4J1 = Piece.Pawn(0, 4, self.namePlayer1, 'Rp4', True)
        self.kingJ2 = Piece.King(4, 2, self.namePlayer2, 'Bk', True)
        self.pawn1J2 = Piece.Pawn(4, 0, self.namePlayer2, 'Bp1', True)
        self.pawn2J2 = Piece.Pawn(4, 1, self.namePlayer2, 'Bp2', True)
        self.pawn3J2 = Piece.Pawn(4, 3, self.namePlayer2, 'Bp3', True)
        self.pawn4J2 = Piece.Pawn(4, 4, self.namePlayer2, 'Bp4', True)

        self.pieces = [self.kingJ1, self.pawn1J1, self.pawn2J1, self.pawn3J1, self.pawn4J1,
                       self.kingJ2, self.pawn1J2, self.pawn2J2, self.pawn3J2, self.pawn4J2]

        self.board.initPieceBoard(self.pieces)
        self.cardList = cardList
        self.cardNeutre = self.cardList[4]

        self.redPlayer.setCard1(self.cardList[0])
        self.redPlayer.setCard2(self.cardList[1])
        self.bluePlayer.setCard1(self.cardList[2])
        self.bluePlayer.setCard2(self.cardList[3])

        self.view = View.View(self.board)


    def getOpponenent(self, player):
        if player == self.redPlayer:
            return self.bluePlayer
        if player == self.bluePlayer:
            return self.redPlayer

    def MovePiece(self, player, piece, card1, x, y):
        allowed_moves = piece.allowed_moves1card(self.board, card1)
        if ((x, y) in allowed_moves) and piece.alive and self.board.isAllyAt(self.pieces, piece.player, x, y) == False:
            if self.board.isOpponentAt(self.pieces, self.getOpponenent(player), x, y):
                self.board.get_PieceAt(x, y).killPeace()
            self.board.place_piece(piece, x, y)
        else:
            print("Move not allowed, choose another destination.")

    def playAMove(self, tour):
        if tour%2==0:
            player = self.redPlayer
            oppenentPlayer = self.bluePlayer
        else:
            player = self.bluePlayer
            oppenentPlayer = self.redPlayer

        self.display_BoardCards(tour,  player, oppenentPlayer)

        print("Player", player.getName(), "Choose a card :")
        selectedCard = player.choose_card(self.board, self.pieces, [player.getCard1(), player.getCard2()])
        print("Player", player.getName(), "Choose piece :")
        selectedPiece = player.choose_piece(self.board, selectedCard, self.pieces)
        print("Player", player.getName(), "Choose a move (coordonate x,y) :")
        selectedMove = player.choose_move(self.board, self.pieces, selectedPiece, selectedCard)
        self.MovePiece(player, selectedPiece, selectedCard, selectedMove[0], selectedMove[1])

        tampon = self.cardNeutre
        self.cardNeutre = selectedCard
        if selectedCard == player.getCard1():
            player.setCard1(tampon)
        elif selectedCard == player.getCard2():
            player.setCard2(tampon)


    def display_BoardCards(self, tour, player, oppenentPlayer):
        print("Tour ", tour)
        print("Player", player.getName(), "Choose a piece :")
        print(f'{oppenentPlayer.getName()} cards')
        self.view.display_card(oppenentPlayer.getCard1())
        self.view.display_card(oppenentPlayer.getCard2())
        print("The neutral card")
        self.view.display_card(self.cardNeutre)
        print("The board")
        self.view.displayBoard()
        print(f"{player.getName()} cards")
        self.view.display_card(player.getCard1())
        self.view.display_card(player.getCard2())


    def isGameOver(self):
        if (self.kingJ1.getAlive() == False) or (self.kingJ2.getX() == 0 and self.kingJ2.getY() == 2):
            print("Player 2 win")
            return True
        if (self.kingJ2.getAlive() == False) or (self.kingJ1.getX() == 4 and self.kingJ1.getY() == 2):
            print("Player 1 win")
            return True
        return False