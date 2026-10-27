from desconto import IDesconto, ICupom
from desconto_normal import DescontoNormal
from desconto_vip import DescontoVIP
from desconto_premium import DescontoPremium
from pedido import Pedido

def aplicar_desconto(desconto: IDesconto, valor: float) -> float:
    return desconto.calcular(valor)

def aplicar_cupom(cupom: ICupom, codigo: str) -> bool:
    return cupom.aplicar_cupom(codigo)

def main():
    valor = 100

    normal = DescontoNormal()
    vip = DescontoVIP()
    premium = DescontoPremium()

    print("Desconto Normal:", aplicar_desconto(normal, valor))
    print("Desconto VIP:", aplicar_desconto(vip, valor))
    print("Cupom VIP:", aplicar_cupom(vip, "DESC123"))

    pedido_normal = Pedido(normal)
    pedido_vip = Pedido(vip)

    print("Total Pedido Normal:", pedido_normal.total(valor))
    print("Total Pedido VIP:", pedido_vip.total(valor))

if __name__ == "__main__":
    main()