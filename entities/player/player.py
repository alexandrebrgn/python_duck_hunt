class Player(object):
    gold: int # Argent accumulé
    kills: int # Canards touchés par le joueur
    chances : int # Nombre de fautes restantes
    firing_rate: int # Frames entre chaque tir

    def __init__(self):
        self.gold=0
        self.kills=0
        self.chances=5
        self.firing_rate=20
