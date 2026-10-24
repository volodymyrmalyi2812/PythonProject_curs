import sys
from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum

import pygame


WIDTH = 960
HEIGHT = 560
TILE = 40
GROUND_Y = 480
LEVEL_WIDTH = 3600
FPS = 60


class GameState(Enum):
    PLAYING = 1
    WON = 2
    LOST = 3


@dataclass
class Point:
    x: int
    y: int


class GameObject(ABC):
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    @abstractmethod
    def draw(self, screen, camera):
        pass


class Platform(GameObject):
    def draw(self, screen, camera):
        r = camera.apply(self.rect)
        pygame.draw.rect(screen, (146, 91, 51), r)
        pygame.draw.rect(screen, (95, 59, 36), r, 2)
        pygame.draw.line(screen, (104, 65, 42), (r.x, r.y + 19), (r.right, r.y + 19), 2)
        pygame.draw.line(screen, (104, 65, 42), (r.centerx, r.y + 19), (r.centerx, r.bottom), 2)
        pygame.draw.rect(screen, (77, 184, 81), (r.x, r.y, r.width, 8))
        pygame.draw.rect(screen, (123, 216, 96), (r.x, r.y, r.width, 3))


class BlockDie(Platform):
    def draw(self, screen, camera):
        r = camera.apply(self.rect)
        pygame.draw.rect(screen, (118, 42, 45), (r.x, r.bottom - 7, r.width, 7))
        for x in range(r.left, r.right, 12):
            pygame.draw.polygon(screen, (234, 73, 70), [
                (x, r.bottom - 7), (min(x + 6, r.right), r.top),
                (min(x + 12, r.right), r.bottom - 7)
            ])


class BlockTeleport(Platform):
    def __init__(self, x, y, target):
        super().__init__(x, y, 36, 60)
        self.target = target

    def draw(self, screen, camera):
        r = camera.apply(self.rect)
        pygame.draw.rect(screen, (43, 84, 150), r, border_radius=10)
        pygame.draw.rect(screen, (99, 232, 241), r, 5, border_radius=10)
        pygame.draw.ellipse(screen, (138, 123, 237), r.inflate(-15, -14))
        pygame.draw.circle(screen, (226, 255, 249), r.center, 6)


class Player(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, 30, 40)
        self.__speed = 5
        self.vy = 0
        self.on_ground = False
        self.previous_bottom = self.rect.bottom
        self.__lives = 3

    @property
    def lives(self):
        return self.__lives

    def hurt(self):
        self.__lives -= 1
        return self.__lives > 0

    def jump(self):
        if self.on_ground:
            self.vy = -14
            self.on_ground = False

    def update(self, keys, platforms):
        self.previous_bottom = self.rect.bottom
        left = keys[pygame.K_LEFT] or keys[pygame.K_a]
        right = keys[pygame.K_RIGHT] or keys[pygame.K_d]
        dx = (int(right) - int(left)) * self.__speed
        self.rect.x += dx
        self.rect.x = max(0, min(self.rect.x, LEVEL_WIDTH - self.rect.width))

        for block in platforms:
            if self.rect.colliderect(block.rect):
                if dx > 0:
                    self.rect.right = block.rect.left
                elif dx < 0:
                    self.rect.left = block.rect.right

        self.vy = min(self.vy + 0.8, 13)
        self.rect.y += round(self.vy)
        self.on_ground = False

        for block in platforms:
            if self.rect.colliderect(block.rect):
                if self.vy > 0:
                    self.rect.bottom = block.rect.top
                    self.vy = 0
                    self.on_ground = True
                elif self.vy < 0:
                    self.rect.top = block.rect.bottom
                    self.vy = 0

    def draw(self, screen, camera):
        r = camera.apply(self.rect)
        pygame.draw.rect(screen, (58, 91, 183), (r.x + 3, r.y + 23, 24, 17))
        pygame.draw.rect(screen, (220, 52, 47), (r.x + 1, r.y + 17, 28, 14))
        pygame.draw.rect(screen, (246, 191, 137), (r.x + 5, r.y + 8, 20, 14))
        pygame.draw.rect(screen, (204, 36, 40), (r.x + 3, r.y + 2, 24, 10))
        pygame.draw.rect(screen, (204, 36, 40), (r.x + 1, r.y + 10, 29, 5))
        pygame.draw.rect(screen, (52, 37, 33), (r.x + 10, r.y + 19, 12, 3))
        pygame.draw.rect(screen, (35, 35, 35), (r.x + 20, r.y + 11, 3, 5))
        pygame.draw.rect(screen, (39, 42, 68), (r.x, r.bottom - 5, 12, 5))
        pygame.draw.rect(screen, (39, 42, 68), (r.x + 18, r.bottom - 5, 12, 5))


class Monster(GameObject):
    def __init__(self, x, y, distance=60):
        super().__init__(x, y, 32, 32)
        self.start_x = x
        self.distance = distance
        self.direction = 1
        self.alive = True

    def update(self):
        self.rect.x += self.direction * 2
        if abs(self.rect.x - self.start_x) >= self.distance:
            self.direction *= -1

    def draw(self, screen, camera):
        if not self.alive:
            return
        r = camera.apply(self.rect)
        pygame.draw.ellipse(screen, (127, 80, 58), r)
        pygame.draw.rect(screen, (94, 52, 42), (r.x + 2, r.y + 19, 28, 13))
        pygame.draw.rect(screen, (255, 249, 223), (r.x + 7, r.y + 10, 7, 10))
        pygame.draw.rect(screen, (255, 249, 223), (r.x + 20, r.y + 10, 7, 10))
        pygame.draw.rect(screen, (35, 29, 27), (r.x + 11, r.y + 12, 3, 6))
        pygame.draw.rect(screen, (35, 29, 27), (r.x + 20, r.y + 12, 3, 6))
        pygame.draw.rect(screen, (57, 36, 33), (r.x, r.bottom - 4, 12, 4))
        pygame.draw.rect(screen, (57, 36, 33), (r.x + 20, r.bottom - 4, 12, 4))


class Princess(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, 36, 54)

    def draw(self, screen, camera):
        r = camera.apply(self.rect)
        pygame.draw.polygon(screen, (255, 121, 181), [
            (r.centerx, r.y + 23), (r.x + 2, r.bottom), (r.right - 2, r.bottom)
        ])
        pygame.draw.rect(screen, (243, 204, 110), (r.x + 8, r.y + 9, 20, 21))
        pygame.draw.ellipse(screen, (255, 210, 169), (r.x + 11, r.y + 13, 15, 17))
        pygame.draw.polygon(screen, (255, 216, 62), [
            (r.x + 10, r.y + 11), (r.x + 10, r.y + 1),
            (r.x + 16, r.y + 6), (r.x + 22, r.y),
            (r.x + 27, r.y + 11)
        ])
        pygame.draw.circle(screen, (38, 41, 49), (r.x + 22, r.y + 20), 2)


class Camera:
    def __init__(self):
        self.x = 0

    def update(self, player_rect):
        target = player_rect.centerx - WIDTH // 2
        target = max(0, min(target, LEVEL_WIDTH - WIDTH))
        self.x += (target - self.x) * 0.15

    def snap(self, player_rect):
        self.x = max(0, min(player_rect.centerx - WIDTH // 2, LEVEL_WIDTH - WIDTH))

    def apply(self, rect):
        return rect.move(-int(self.x), 0)


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Mini Mario")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 29)
        self.big_font = pygame.font.Font(None, 65)
        self.small_font = pygame.font.Font(None, 24)
        self.camera = Camera()
        self.restart()

    def restart(self):
        self.state = GameState.PLAYING
        self.player = Player(70, GROUND_Y - 40)
        self.camera.snap(self.player.rect)
        self.checkpoint = Point(70, GROUND_Y - 40)
        self.platforms = []
        for start, end in [(0, 18), (20, 39), (42, 61), (63, 90)]:
            for i in range(start, end):
                self.platforms.append(Platform(i * TILE, GROUND_Y, TILE, TILE))

        for x, y, count in [(260, 385, 5), (1010, 375, 5),
                            (1790, 380, 5), (2750, 380, 5)]:
            for i in range(count):
                self.platforms.append(Platform(x + i * TILE, y, TILE, 20))

        self.hazards = [BlockDie(x, GROUND_Y - 24, 36, 24)
                        for x in (570, 1140, 2040, 3050)]
        self.monsters = [Monster(x, GROUND_Y - 32, 48)
                         for x in (430, 1430, 2220, 3250)]
        self.portals = [
            BlockTeleport(920, GROUND_Y - 60, Point(2680, GROUND_Y - 40)),
            BlockTeleport(2630, GROUND_Y - 60, Point(990, GROUND_Y - 40))
        ]
        self.princess = Princess(3510, GROUND_Y - 54)

    def use_portal(self):
        for portal in self.portals:
            if self.player.rect.colliderect(portal.rect):
                self.player.rect.topleft = (portal.target.x, portal.target.y)
                self.player.vy = 0
                self.player.on_ground = False
                self.checkpoint = Point(portal.target.x, portal.target.y)
                self.camera.snap(self.player.rect)
                return

    def lose_life(self):
        if self.player.hurt():
            self.player.rect.topleft = (self.checkpoint.x, self.checkpoint.y)
            self.player.vy = 0
            self.player.on_ground = False
            self.camera.snap(self.player.rect)
        else:
            self.state = GameState.LOST

    def check_collisions(self):
        if self.player.rect.top > HEIGHT + 50:
            self.lose_life()
            return

        for block in self.hazards:
            if self.player.rect.colliderect(block.rect):
                self.lose_life()
                return

        for monster in self.monsters[:]:
            if self.player.rect.colliderect(monster.rect):
                if self.player.vy > 0 and self.player.previous_bottom <= monster.rect.top + 10:
                    self.monsters.remove(monster)
                    monster.alive = False
                    self.player.vy = -10
                else:
                    self.lose_life()
                    return

        if self.player.rect.colliderect(self.princess.rect):
            self.state = GameState.WON

    def update(self):
        keys = pygame.key.get_pressed()
        self.player.update(keys, self.platforms)
        for monster in self.monsters:
            monster.update()
        self.check_collisions()
        self.camera.update(self.player.rect)

    def draw_background(self):
        self.screen.fill((132, 206, 246))
        for x in range(130, LEVEL_WIDTH, 430):
            px = x - int(self.camera.x * 0.35)
            if -100 < px < WIDTH + 100:
                pygame.draw.ellipse(self.screen, (243, 251, 255), (px, 92, 115, 36))
                pygame.draw.ellipse(self.screen, (243, 251, 255), (px + 25, 76, 65, 45))
        for x in range(0, LEVEL_WIDTH, 360):
            px = x - int(self.camera.x * 0.65)
            if -160 < px < WIDTH + 160:
                pygame.draw.ellipse(self.screen, (93, 184, 124), (px, 405, 240, 185))
                pygame.draw.ellipse(self.screen, (117, 204, 136), (px + 70, 427, 200, 158))

    def draw(self):
        self.draw_background()
        for thing in self.platforms + self.hazards + self.portals + self.monsters:
            thing.draw(self.screen, self.camera)
        self.princess.draw(self.screen, self.camera)
        self.player.draw(self.screen, self.camera)

        pygame.draw.rect(self.screen, (29, 43, 67), (0, 0, WIDTH, 54))
        title = self.font.render("MINI MARIO", True, (255, 239, 184))
        lives = self.font.render(f"LIVES: {self.player.lives}", True, (255, 255, 255))
        help_text = self.small_font.render("A/D MOVE   SPACE JUMP   E PORTAL   R RESTART", True, (228, 238, 250))
        self.screen.blit(title, (18, 14))
        self.screen.blit(lives, (192, 14))
        self.screen.blit(help_text, (347, 14))

        if self.state != GameState.PLAYING:
            shade = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            shade.fill((15, 21, 35, 190))
            self.screen.blit(shade, (0, 0))
            if self.state == GameState.WON:
                message = "YOU SAVED THE PRINCESS!"
                color = (255, 236, 127)
            else:
                message = "GAME OVER"
                color = (252, 117, 124)
            headline = self.big_font.render(message, True, color)
            hint = self.font.render("Press R to play again or ESC to exit", True, (255, 255, 255))
            self.screen.blit(headline, headline.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 35)))
            self.screen.blit(hint, hint.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 35)))

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.K_r:
                        self.restart()
                    elif self.state == GameState.PLAYING:
                        if event.key in (pygame.K_SPACE, pygame.K_UP, pygame.K_w):
                            self.player.jump()
                        elif event.key == pygame.K_e:
                            self.use_portal()

            if self.state == GameState.PLAYING:
                self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(FPS)
        pygame.quit()


def run_tests():
    player = Player(100, 100)
    assert player.lives == 3
    assert player.hurt() and player.lives == 2
    player.on_ground = True
    player.jump()
    assert player.vy == -14 and not player.on_ground
    camera = Camera()
    camera.snap(pygame.Rect(2000, 100, 30, 40))
    assert camera.x > 0
    spike = BlockDie(0, 0, 36, 24)
    assert isinstance(spike, Platform)
    portal = BlockTeleport(20, 20, Point(200, 400))
    assert portal.target == Point(200, 400)
    enemy = Monster(100, 100, 10)
    initial_x = enemy.rect.x
    enemy.update()
    assert enemy.rect.x != initial_x
    print("All 6 checks passed!")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        run_tests()
    else:
        Game().run()
