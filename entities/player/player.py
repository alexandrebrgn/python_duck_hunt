class Player(object):
    gold: int # Argent accumulé
    kills: int # Canards touchés par le joueur
    chances : int # Nombre de fautes restantes

    def __init__(self):
        self.gold=0
        self.kills=0
        self.chances=5
