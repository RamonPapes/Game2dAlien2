from src.desconto_solid.desconto import IDesconto

class StubSemDesconto(IDesconto):
    def calcular(self, valor):
        return 0
