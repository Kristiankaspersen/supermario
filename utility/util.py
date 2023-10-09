from pygame import Rect
from pygame.rect import RectType

from models.character import Player
from models.objects import Object


def collide_with_object(player: Player, object: Object) -> None:
    if player.rect.colliderect(object.x, object.y, object.width, object.height):
        player.rect.y = object.y - player.rect.height  # Set player on top of the platform
        player.jumping = False  # Reset jumping state
        player.vertical_velocity = 0  # Reset vertical velocity

def after_collision(player: Rect | RectType, object: Object) -> None:
    """
    :param player:
    :param object:
    :return:
    Set player on top of platform
    Resets jumping state
    Reset vertical velocity
    """
    player.y = object.y - player.height


