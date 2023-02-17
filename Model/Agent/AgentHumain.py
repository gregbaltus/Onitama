import Model.Agent.InterfaceAgent as Agent

class AgentHumain(Agent.Agent):
    def __init__(self, playerName, isFirst):
        super().__init__(playerName, isFirst)

    def choose_card(self, cards):
        chosen_card = None
        while chosen_card is None:
            card_name = input("Choisissez une carte parmi : {}\n".format([card.name for card in cards]))
            for card in cards:
                if card.name == card_name:
                    chosen_card = card
                    break
            if chosen_card is None:
                print("Carte non valide, veuillez réessayer\n")
        return chosen_card


    def choose_piece(self, board, card, pieces_list):
        allowed_pieces = []
        for piece in pieces_list:
            allowed_move = piece.allowed_moves1card(board, card)
            if piece.getAlive() and piece.getPlayer() ==  self.playerName and allowed_move:
                allowed_pieces +=[piece.getName()]
        while True:
            print("The allowed pieces are : ", allowed_pieces)
            piece_name = input("Enter the name of the piece: ")
            for piece in pieces_list:
                allowed_move = piece.allowed_moves1card(board, card)
                if piece.getName() == piece_name and piece.getAlive() and piece.getPlayer() == self.playerName and allowed_move:
                    return piece
            print("Invalid piece name, please try again.")

    def choose_move(self, board, pieces, piece, card):
        while True:
            allowed_moves = []
            allowed_movesCard = piece.allowed_moves1card(board, card)
            for (mx,my) in  allowed_movesCard:
                if board.isAllyAt(pieces, piece.player, mx, my) == False:
                    allowed_moves += [(mx, my)]
            print("The allowed move are ", allowed_moves)
            x, y = map(int, input("Enter the coordinates for the move: ").split())
            if (x, y) in allowed_moves:
                return (x, y)
            print("Invalid move, please try again.")

    def setCard1(self, card):
        self.card1 = card

    def setCard2(self, card):
        self.card2 = card

    def getName(self):
        return self.playerName

    def getCard1(self):
        return self.card1

    def getCard2(self):
        return self.card2
