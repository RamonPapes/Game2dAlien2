from desconto import IDesconto

class DescontoNormal(IDesconto):
    def calcular(self, valor):
        return valor * 0.1  # 10% de desconto