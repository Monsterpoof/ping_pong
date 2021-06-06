from pygame import *
from random import randint
#подгружаем отдельно функции для работы со шрифтом
font.init()
font1 = font.SysFont('Arial', 60)
win = font1.render('YOU WIN!', True, (255, 255, 255))
lose = font1.render('YOU LOSE!', True, (180, 0, 0))
 
font2 = font.SysFont('Arial', 60)
 
#фоновая музыка
mixer.init()
mixer.music.load('backmus.mp3.mp3')
mixer.music.play() 
#создаём окошко
win_width = 700
win_height = 500
display.set_caption('Ping-Ping')
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))
#создаём спрайты
ship = Player(img_hero, 5, win_height - 100, 80, 100, 10)


#нам нужны такие картинки:
img_back = "background.png" #фон игры
img_rockets = "platform.png" #герой
img_ball = "ball.png" #враг
#класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
 #конструктор класса
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       #вызываем конструктор класса (Sprite):
       sprite.Sprite.__init__(self)
 
       #каждый спрайт должен хранить свойство image - изображение
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed
 
       #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 #метод, отрисовывающий героя на окне
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
 
#класс главного игрока
class Player(GameSprite):
   #метод для управления спрайтом стрелками клавиатуры
   def update(self):
       keys = key.get_pressed()
       if keys[K_LEFT] and self.rect.x > 5:
           self.rect.x -= self.speed
       if keys[K_RIGHT] and self.rect.x < win_width - 80:
           self.rect.x += self.speed
 #метод "выстрел" (используем место игрока, чтобы создать там пулю)
   def fire(self):
       bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 15, 20, -15)
       bullets.add(bullet)
 

class Enemy(GameSprite):
   #движение врага
   def update(self):
       self.rect.y += self.speed
       global lost
       #исчезает, если дойдёт до края экрана
       if self.rect.y > win_height:
           self.rect.x = randint(80, win_width - 80)
           self.rect.y = 0


player = sprite.Group()
#переменная "игра закончилась": как только там True, в основном цикле перестают работать спрайты
finish = False
#основной цикл игры:
run = True #флаг сбрасывается кнопкой закрытия окна
while run:
   #событие нажатия на кнопку Закрыть
   for e in event.get():
       if e.type == QUIT:
           run = False

 #сама игра: действия спрайтов, проверка правил игры, перерисовка
   if not finish:
       #обновляем фон
       window.blit(background,(0,0))
 
       #производим движения спрайтов
       ship.update()
       monsters.update()
       assteroids.update()
       bullets.update()
 
       #обновляем их в новом местоположении при каждой итерации цикла
       ship.reset()
       ball.draw(window)

 
       #пишем текст на экране
       text = font2.render("Left: W-up S-down ", (255, 255, 255))
       window.blit(text, (10, 20))
 
       text_lose = font2.render("Right: Button_down - down Button_up - up" , (255, 255, 255))
       window.blit(text_lose, (10, 50))
 
       display.update()


 
   time.delay(20)