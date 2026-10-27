import pygame

from src.bullet import Bullet
from src.bullet_manager import BulletManager
from src.game_events import GameEventHandler
from src.game_renderer import GameRenderer
from tests.doubles import StubSettings, StubShip


# ---------- STUBS ----------

def test_bullet_sobe_com_stub():
    settings = StubSettings()  # Stub com bullet_speed fixo em 5
    ship = StubShip()  # Stub que só fornece o rect da nave

    bullet = Bullet(None, settings, ship)  # A tela não é usada no update
    y_inicial = bullet.y

    bullet.update()

    assert bullet.y == y_inicial - 5  # O projétil sobe exatamente bullet_speed


def test_bullet_manager_respeita_limite_com_stub():
    settings = StubSettings(bullet_allowed=2)  # Stub permitindo só 2 projéteis
    manager = BulletManager(None, settings, StubShip())

    manager._fire_bullet()
    manager._fire_bullet()
    manager._fire_bullet()  # Terceiro disparo deve ser ignorado

    assert len(manager.bullets) == 2


# ---------- MOCKS ----------

def test_tecla_espaco_dispara_projetil_com_mock(mocker):
    mock_ship = mocker.Mock()  # Criar mock da nave
    mock_bullet_manager = mocker.Mock()  # Criar mock do gerenciador de projéteis
    evento = mocker.Mock(key=pygame.K_SPACE)  # Simular evento da tecla espaço

    handler = GameEventHandler(mock_ship, mock_bullet_manager)
    handler._handle_keydown(evento)

    mock_bullet_manager._fire_bullet.assert_called_once()  # verifica se disparou uma única vez


def test_tecla_direita_move_nave_sem_disparar_com_mock(mocker):
    mock_ship = mocker.Mock()
    mock_bullet_manager = mocker.Mock()
    evento = mocker.Mock(key=pygame.K_RIGHT)  # Simular evento da seta para a direita

    handler = GameEventHandler(mock_ship, mock_bullet_manager)
    handler._handle_keydown(evento)

    assert mock_ship.moving_right is True  # verifica se a nave foi marcada para mover
    mock_bullet_manager._fire_bullet.assert_not_called()  # verifica que não houve disparo


def test_renderer_desenha_elementos_com_mock(mocker):
    mock_flip = mocker.patch("src.game_renderer.pygame.display.flip")  # Evita abrir janela
    mock_screen = mocker.Mock()
    mock_ship = mocker.Mock()
    mock_aliens = mocker.Mock()
    mock_bullet = mocker.Mock()
    mock_bullets = mocker.Mock()
    mock_bullets.sprites.return_value = [mock_bullet, mock_bullet]  # Dois projéteis na tela

    renderer = GameRenderer(mock_screen, (230, 230, 230), mock_ship, mock_bullets, mock_aliens)
    renderer._render_screen()

    mock_screen.fill.assert_called_once_with((230, 230, 230))  # verifica se pintou o fundo
    mock_ship.blitme.assert_called_once()  # verifica se desenhou a nave
    mock_aliens.draw.assert_called_once_with(mock_screen)  # verifica se desenhou os aliens
    assert mock_bullet.draw_bullet.call_count == 2  # verifica se desenhou cada projétil
    mock_flip.assert_called_once()  # verifica se atualizou a tela
