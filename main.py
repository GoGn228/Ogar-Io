import pygame
import os
import sys
import random

pygame.init()
current_path=os.path.dirname(__file__)
os.chdir(current_path)
WIDTH=1200
HEIGHT=800
FPS=60
#pygame.mixer.music.load('sound/mario.mp3')
#pygame.mixer.music.play(-1)
sc=pygame.display.set_mode((WIDTH, HEIGHT))
clock=pygame.time.Clock()

from load import *

def game_lvl():
    sc.fill((128, 128, 128))
    food_group.update()
    food_group.draw(sc)
    blue_group.update()
    blue_group.draw(sc)
    red_group.update()
    red_group.draw(sc)
    player_group.update()
    player_group.draw(sc)
    spawn.update()
    pygame.display.update()


class Blue(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.timer_move = 0
        self.speed_x = random.randint(-5, 5)
        self.speed_y = random.randint(-5, 5)
    def update(self):
        self.pos = self.rect.center
        self.timer_move += 1
        if self.timer_move / FPS > 3:
            self.speed_x = random.randint(-5, 5)
            self.speed_y = random.randint(-5, 5)
            self.timer_move = 0
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.right > WIDTH:
            self.speed_x *= -1
        if self.rect.left < 0:
            self.speed_x *= -1
        if self.rect.top < 0:
            self.speed_y *= -1
        if self.rect.bottom > HEIGHT:
            self.speed_y *= -1

        if pygame.sprite.spritecollide(self, food_group, True):
            self.image = pygame.transform.rotozoom(self.image, 0, 1.05)
            self.rect = self.image.get_rect()
            self.rect.center = self.pos
        if pygame.sprite.spritecollide(self, red_group, False):
            red = pygame.sprite.spritecollide(self, red_group, False)[0]
            if red.image.get_height() < self.image.get_height():
                pygame.sprite.spritecollide(self, red_group, False)[0].kill()
                self.image = pygame.transform.rotozoom(self.image, 0, 1.15)
                self.rect = self.image.get_rect()
                self.rect.center = self.pos
        if pygame.sprite.spritecollide(self, player_group, False):
            player = pygame.sprite.spritecollide(self, player_group, False)[0]
            if player.image.get_height() < self.image.get_height():
                pygame.sprite.spritecollide(self, player_group, False)[0].kill()
                self.image = pygame.transform.rotozoom(self.image, 0, 1.15)
                self.rect = self.image.get_rect()
                self.rect.center = self.pos

class Red(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.timer_move = 0
        self.speed_x = random.randint(-5, 5)
        self.speed_y = random.randint(-5, 5)

    def update(self):
        self.pos = self.rect.center
        self.timer_move += 1
        if self.timer_move / FPS > 3:
            self.speed_x = random.randint(-5, 5)
            self.speed_y = random.randint(-5, 5)
            self.timer_move = 0
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.right > WIDTH:
            self.speed_x *= -1
        if self.rect.left < 0:
            self.speed_x *= -1
        if self.rect.top < 0:
            self.speed_y *= -1
        if self.rect.bottom > HEIGHT:
            self.speed_y *= -1

        if pygame.sprite.spritecollide(self, food_group, True):
            self.image = pygame.transform.rotozoom(self.image, 0, 1.05)
            self.rect = self.image.get_rect()
            self.rect.center = self.pos
        if pygame.sprite.spritecollide(self, player_group, False):
            player = pygame.sprite.spritecollide(self, player_group, False)[0]
            if player.image.get_height() < self.image.get_height():
                pygame.sprite.spritecollide(self, player_group, False)[0].kill()
                self.image = pygame.transform.rotozoom(self.image, 0, 1.15)
                self.rect = self.image.get_rect()
                self.rect.center = self.pos
        if pygame.sprite.spritecollide(self, blue_group, False):
            blue = pygame.sprite.spritecollide(self, blue_group, False)[0]
            if blue.image.get_height() < self.image.get_height():
                pygame.sprite.spritecollide(self, blue_group, False)[0].kill()
                self.image = pygame.transform.rotozoom(self.image, 0, 1.15)
                self.rect = self.image.get_rect()
                self.rect.center = self.pos

class Food(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
    #def update(self):

class Player(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.speed = 5
        self.dir = "right"
    def update(self):
        self.pos = self.rect.center
        key = pygame.key.get_pressed()
        if key[pygame.K_d]:
            self.dir = "right"
            self.rect.x += self.speed
        if key[pygame.K_a]:
            self.dir = "left"
            self.rect.x -= self.speed
        if key[pygame.K_s]:
            self.dir = "down"
            self.rect.y += self.speed
        if key[pygame.K_w]:
            self.dir = "up"
            self.rect.y -= self.speed
        if pygame.sprite.spritecollide(self, food_group, True):
            self.image = pygame.transform.rotozoom(self.image, 0, 1.05)
            self.rect = self.image.get_rect()
            self.rect.center = self.pos
        if pygame.sprite.spritecollide(self, blue_group, False):
            blue = pygame.sprite.spritecollide(self, blue_group, False)[0]
            if blue.image.get_height() < self.image.get_height():
                pygame.sprite.spritecollide(self, blue_group, False)[0].kill()
                self.image = pygame.transform.rotozoom(self.image, 0, 1.15)
                self.rect = self.image.get_rect()
                self.rect.center = self.pos
        if pygame.sprite.spritecollide(self, red_group, False):
            red = pygame.sprite.spritecollide(self, red_group, False)[0]
            if red.image.get_height() < self.image.get_height():
                pygame.sprite.spritecollide(self, red_group, False)[0].kill()
                self.image = pygame.transform.rotozoom(self.image, 0, 1.15)
                self.rect = self.image.get_rect()
                self.rect.center = self.pos

class Spawn():
    def __init__(self):
        self.timer = 0

    def update(self):
        if len(food_group) < 20:
            pos = (random.randint(100, WIDTH - 100)), random.randint(100, HEIGHT - 100)
            food = Food(food_image, pos)
            food_group.add(food)
        if len(blue_group) < 5:
            pos = (random.randint(100, WIDTH - 100)), random.randint(100, HEIGHT - 100)
            blue =Blue(blue_image, pos)
            blue_group.add(blue)
        if len(red_group) < 5:
            pos = (random.randint(100, WIDTH - 100)), random.randint(100, HEIGHT - 100)
            red =Red(red_image, pos)
            red_group.add(red)

def restart():
    global blue_group, red_group, food_group, player_group
    global spawn
    blue_group = pygame.sprite.Group()
    red_group = pygame.sprite.Group()
    food_group = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    player = Player(player_image, (0, 0))
    player_group.add(player)
    spawn = Spawn()


restart()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    game_lvl()
    clock.tick(FPS)