
class Matrix:
    def __init__(self):
        self.name = ""
        self.values = []
        self.lignes = 0
        self.colonnes = 0
        
        
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, v):
        self._name  =  v
        

    @property
    def lignes(self):
        return self._lignes

    @lignes.setter
    def lignes(self, v):
        self._lignes  =  v
        
        
    @property
    def colonnes(self):
        return self._colonnes

    @colonnes.setter
    def colonnes(self, v):
        self._colonnes  =  v
        
        
    @property
    def values(self):
        return self._values

    @values.setter
    def values(self, v):
        self._values  =  v
    
            
    def __str__(self):
        affichage = self.name + " =\n"

        for ligne in self.values:
            affichage += "| "
            
            for valeur in ligne:
                affichage += str(valeur) + " "
            
            affichage += "|\n"

        return affichage