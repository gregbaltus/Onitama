import random
import Model.Game as Game
import os
import Model.Card as Cards

class App:
    def start(self):
        cardPath = "Model/Cards/"
        possibleMode = ["2players", "vsRandomIA"]
        mode = self.chooseMode(possibleMode)
        cardsList = self.select5RandomCard(cardPath)
        game = Game.Game(cardsList, mode)
        tour = 0

        while(not game.isGameOver()):
            game.playAMove(tour)
            tour += 1


    def select5cardsName(self, cardPath):
        txt_files = [f for f in os.listdir(cardPath) if f.endswith(".txt")]
        selected_files = random.sample(txt_files, 5)
        return selected_files

    def select5RandomCard(self, cardPath):
        cardtxt = self.select5cardsName(cardPath)
        cardList = []
        for cardName in cardtxt:
            cardList += [Cards.Card(cardPath + cardName, cardName)]
        return cardList

    def select1Card(self, name, cardPath):
        return [Cards.Card(cardPath + name)]

    def chooseMode(self, options):
        while True:
            choice = input("Choisissez une option parmi : " + ", ".join(options))
            if choice in options:
                return choice
            else:
                print("Entrée non valide. Veuillez saisir une option valide.")