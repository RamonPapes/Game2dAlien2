import pytest

from src.desconto_solid.desconto_normal import DescontoNormal
from src.desconto_solid.desconto_vip import DescontoVIP
from src.desconto_solid.desconto_premium import DescontoPremium

@pytest.mark.parametrize("valor, esperado", [
    (100, 30),
    (200, 60),
    (300, 90),
])
def test_desconto_premium(valor, esperado):
    desconto = DescontoPremium()
    assert desconto.calcular(valor) == esperado

def test_desconto_normal():
    desconto = DescontoNormal()
    resultado = desconto.calcular(100)
    assert resultado == 10, f"Esperado 10, mas obteve {resultado}"

@pytest.fixture
def desconto_vip():
    return DescontoVIP()

def test_desconto_vip_100(desconto_vip):
    assert desconto_vip.calcular(100) == 20

def test_desconto_vip_200(desconto_vip):
    assert desconto_vip.calcular(200) == 40