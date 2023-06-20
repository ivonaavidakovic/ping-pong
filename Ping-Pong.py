from pygame import*

class GameSprite (sprite.Sprite):
    def __init__ (self, player_image, player_x, player_y, width, height, player_speed):
        super().__init__()
        self.image = transform.scale (image.load (player_image), (width, height))
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
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

win_width = 600
win_height = 500

back = (200, 255, 255)
window = display.set_mode((win_width, win_height))

platform_l = Player("racket.png", 50, 250, 30, 80, 15)
platform_r = Player("racket.png", 520, 250, 30, 80, 15)

ball = GameSprite("tenis_ball.png", 200, 200, 50, 50, 5)

clock =  time.Clock()
FPS = 60
game = True
finish = False

speed_x = 3
speed_y = 3

font.init()
font1 = font.Font(None, 38)
player1_W = font1.render("Player 1 win!", True, (180, 0, 0))
player2_W = font1.render("Player 2 win!", True, (180, 0, 0))

player1 = font1.render("Player 1", True, (180, 0, 0))
player2 = font1.render("Player 2", True, (180, 0, 0))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False


    if finish != True:

        window.fill(back)
        platform_l.update_l()
        platform_r.update_r()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        platform_l.reset()
        platform_r.reset()

        ball.reset()

        if sprite.collide_rect(platform_r, ball) or sprite.collide_rect(platform_l, ball):
            speed_x *= -1
            speed_y *= 1

        if ball.rect.y > win_height -50 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x > win_width:
            finish = True
            window.blit(player1_W, (200, 200))

        if ball.rect.x < 0:
            finish = True
            window.blit(player2_W, (200, 200))

        window.blit(player1, (50, 10))
        window.blit(player2, (450, 10))

    display.update()
    clock.tick(FPS)