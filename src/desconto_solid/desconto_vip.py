from desconto import Desconto

class DescontoVip(Desconto):
    def calcular(self, valor):
        return valor * 0.2