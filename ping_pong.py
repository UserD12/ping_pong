from pygame import *

window = display.set_mode((700, 500))#создай окно игры
display.set_caption('Пинг понг')
background = transform.scale(image.load('background.png'), (700, 500))

clock = time.Clock()
FPS = 60

game = True
finish = False

win_height = 500
speed_x = 3
speed_y = 3
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_width, player_height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
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
        if keys[K_DOWN] and self.rect.y < win_height - 155:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 155:
            self.rect.y += self.speed


ball = GameSprite('shar.png',325,250,5,50,50)
player1 = Player('raketka.png', 30, 200, 4, 20, 150)
player2 = Player('raketka.png', 650, 200, 4, 20, 150)

font.init()
font1 = font.SysFont('Arial', 36)
text_lose = font1.render('Игрок 1 выиграл',True, (255, 255, 255))
text_win = font1.render('Игрок 2 выиграл',True, (255, 255, 255))

while game:
    window.blit(background, (0,0))

    for e in event.get():
        if e.type == QUIT:
            game = False#задай фон сцены
    if finish != True:
        player1.update_l()
        player1.reset()
        ball.reset()
        player2.update_r()
        player2.reset()
        ball.rect.x += speed_x
        ball.rect.y +=speed_y

    if ball.rect.y > win_height - 50 or ball.rect.y < 0:
        speed_y *= -1


    if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
        speed_x *= -1
        ball.speed += 100

    if ball.rect.x < 0:
        finish = True
        window.blit(text_win, (200,200))
    if ball.rect.x > 700:
        finish = True
        window.blit(text_lose, (200,200))

    display.update()
    clock.tick(FPS)
