import bola

class Balanza:
    def __init__(self, veces_usado = 0):
        self.veces_usado = veces_usado

    def pesar(self, bolas1, bolas2):

        peso1 = sum(bola.peso for bola in bolas1)
        peso2 = sum(bola.peso for bola in bolas2)
        self.veces_usado += 1

        if peso1 > peso2:
            return 1
        elif peso1 < peso2:
            return -1
        else:
            return 0

    def emaitza(self, bola):

        if(bola.peso > 1):
            return "Has acertado la bola con mas peso en " + str(self.veces_usado) + " veces"
        else:
            return "Has fallado"