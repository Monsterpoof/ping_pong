from pygame import *
from random import randint

mixer.init()
mixer.music.load('mus.mp3')
mixer.music.play()

img_hero = "ball.png"


class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
       super().__init__()
       self.image = transform.scale(image.load("platf.psd"), (55,55)) #вместе 55,55 - параметры
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
 
class Player(GameSprite):
   def update_r(self):
       keys = key.get_pressed()
       if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y < win_height - 80:
           self.rect.y += self.speed
   def update_l(self):
       keys = key.get_pressed()
       if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_s] and self.rect.y < win_height - 80:
           self.rect.y += self.speed

ball = GameSprite('boll', 200, 200, 4, 50, 50)

win_width = 700
win_height = 500
display.set_caption("Ping pong")
window = display.set_mode((700, 500))
background = transform.scale(image.load('images.jpg'), (700, 500))

speed_x = 3
speed_y = 3

font.init()
font1 = font.Font(None, 35)
lose1 = font1.render(
    'PLAYER 1 LOSE!', True, (180, 0, 0))

font1 = font.Font(None, 35)
lose2 = font1.render(
    'PLAYER 2 LOSE!', True, (180, 0, 0))

finish = False

game = True


while game:
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y

    if ball.rect.y > win_height-50 or ball.rect.y < 0:
        speed_y *= -1

    if sprite.collade_rect(recket1, ball) or sprire.collide_rect(racket2, ball):
        speed_x *= -1

    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (200, 200))

    if ball.rect.x < 0:
        finish = True
        window.blit(lose2, (200, 200))
      