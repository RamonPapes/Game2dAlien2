from abc import ABC, abstractmethod

class Desconto(ABC):
    @abstractmethod
    def calcular(self, valor):
        pass

class IDesconto:
    def calcular(self, valor):
        raise NotImplementedError
    
class ICupom:
    def aplicar_cupom(self, codigo):
        raise NotImplementedError
    
class IVIP:
    def validar_usuario_vip(self, usuario):
        raise NotImplementedError