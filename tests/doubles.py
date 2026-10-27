import pygame

from src.desconto_solid.desconto import IDesconto

class StubSemDesconto(IDesconto):
    def calcular(self, valor):
        return 0


class StubSettings:
    """Stub das configurações do jogo com valores fixos e previsíveis."""
    def __init__(self, bullet_allowed=2):
        self.bullet_speed = 5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0, 0, 0)
        self.bullet_allowed = bullet_allowed


class StubShip:
    """Stub da nave: só fornece o rect usado para posicionar o projétil."""
    def __init__(self):
        self.rect = pygame.Rect(100, 500, 60, 48)
