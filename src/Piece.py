class Piece(object):
    def __init__(self, name, species, clas, cost, tier):
        self._name = name
        self._species = species
        self._clas = clas
        self._cost = cost
        self._tier = tier
        self._star = 1
    
    @property
    def name(self):
        return self._name
    
    @property
    def species(self):
        return self._species

    @property
    def clas(self):
        return self._clas

    @property
    def cost(self):
        return self._cost
    
    @property
    def tier(self):
        return self._tier
    
    @property
    def star(self):
        return self._star
    
    @star.setter
    def star(self, star):
        self._star = star