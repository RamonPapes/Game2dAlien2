from desconto import Desconto

class DescontoPremium(Desconto):
    def calcular(self, valor):
        return valor * 0.3