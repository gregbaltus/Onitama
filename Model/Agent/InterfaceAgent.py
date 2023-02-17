from abc import abstractmethod


class Agent:
    def __init__(self, playerName, isFirst):
        self.playerName = playerName
        self.isFirst = isFirst
        self.card1 = None
        self.card2 = None

    @abstractmethod
    def choose_piece(self, pieces_list):
        pass

    @abstractmethod
    def choose_card(self, cards):
        pass

    @abstractmethod
    def choose_move(self, piece, board, card):
        pass

    @abstractmethod
    def setCard1(self, card):
        pass

    @abstractmethod
    def setCard2(self, card):
        pass

    @abstractmethod
    def getName(self):
        pass

    @abstractmethod
    def getCard1(self):
        pass

    @abstractmethod
    def getCard2(self):
        pass