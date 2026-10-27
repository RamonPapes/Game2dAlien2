from desconto_normal import DescontoNormal
from desconto_vip import DescontoVip
from desconto_premium import DescontoPremium

def main():
    m_normal = DescontoNormal()
    m_premium = DescontoPremium()
    m_vip = DescontoVip()

    valor = 100


    print("Valor de Desconto cliente Normal: ", m_normal.calcular(valor))
    print("Valor de Desconto cliente Normal: ", m_vip.calcular(valor))
    print("Valor de Desconto cliente Normal: ", m_premium.calcular(valor))

main()  