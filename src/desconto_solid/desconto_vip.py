from desconto import IDesconto, ICupom, IVIP

class DescontoVIP(IDesconto, ICupom, IVIP):
    def calcular(self, valor):
        return valor * 0.2  # 20% de desconto

    def aplicar_cupom(self, codigo):
        return True

    def validar_usuario_vip(self, usuario):
        return usuario == "vip"