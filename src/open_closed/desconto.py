from abc import ABC, abstractmethod

class Desconto: 
    @abstractmethod
    def calcular(self, valor):
        pass