class Card:
    def __init__(self, pathName, name):
        self.pathName = pathName
        self.name = name
        self.moves = []
        with open(f"{pathName}") as f:
            for line in f:
                x, y = map(int, line.strip().split())
                self.moves.append((x, y))

    def __repr__(self):
        return self.name

    def getName(self):
        return self.name