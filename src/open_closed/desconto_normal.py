from desconto import Desconto

class DescontoNormal(Desconto):
    def calcular(self, valor):
        return valor * 0.1