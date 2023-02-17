import random
import Model.Agent.InterfaceAgent as Agent

class AgentRandomIA(Agent.Agent):
    def init(self, playerName, isFirst):
        super().init(playerName, isFirst)

    def choose_card(self, board, pieces_list, cards):
        allowed_cards = []
        for card in cards:
            allowed_move = []
            for piece in pieces_list:
                allowed_move += piece.allowed_moves1card(board, card)
            if allowed_move:
                allowed_cards += [card]
        return random.choice(allowed_cards)

    def choose_piece(self, board, card, pieces_list):
        allowed_pieces = []
        for piece in pieces_list:
            allowed_move = piece.allowed_moves1card(board, card)
            if piece.getAlive() and piece.getPlayer() == self.playerName and allowed_move:
                allowed_pieces += [piece]
        return random.choice(allowed_pieces)

    def choose_move(self, board, pieces, piece, card):
        allowed_moves = []
        allowed_movesCard = piece.allowed_moves1card(board, card)
        for (mx, my) in allowed_movesCard:
            if board.isAllyAt(pieces, piece.player, mx, my) == False:
                allowed_moves += [(mx, my)]
        return random.choice(allowed_moves)

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



