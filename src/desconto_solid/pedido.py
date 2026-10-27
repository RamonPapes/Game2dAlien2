from desconto import Desconto, IDesconto

class CalculadoraDesconto:
    def __init__(self, desconto: Desconto):
        self.desconto = desconto

    def calcular_desconto(self, valor):
        return valor - self.desconto.calcular(valor)

class Pedido:
    def __init__(self, desconto: IDesconto):
        self.desconto = desconto

    def total(self, valor):
        return valor - self.desconto.calcular(valor)