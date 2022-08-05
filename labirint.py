from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y):
        sprite.Sprite.init(self)
        self.image=transform.scale(image.load(player_image),(size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_x_speed, player_y_speed):
        GameSprite.init(self, player_image, player_x, player_y, size_x, size_y)

        self.x_speed = player_x_speed
        self.y_speed = player_y_speed

    def update(self):
        if packman.rect.x <= win_width-80 and packman.x_speed > 0 or packman.rect.x >= 0 and packman.x_speed < 0:
        self.rect.x += self.x_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.x_speed > 0:
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left)
        elif self .x_speed < 0:
            for p in platforms_touched:
                self.rect.left = min(self.rect.left, p.rect.right)
        if packman.rect.y <= win_width-80 and packman.xy_speed > 0 or packman.rect.y >= 0 and packman.y_speed < 0:
            self.rect.y += self.y_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.y_speed > 0:
            for p in platforms_touched:
                self.y_speed = 0
                if p.rect.top < self.rect.bottom:
                    self.rect.bottom = min(self.rect.bottom, p.rect.top)
        elif self .x_speed < 0:
            for p in platforms_touched:
                self.y_speed = 0
                self.rect.top = max(self.rect.top, p.rect.bottom)
    def fire(self):
        bullet = Bullet('bullet.png',self.rect.right,self.rect.centery, 15, 20, 15)
        bullet.add()


class Enemy(GameSprite):
    side = 'left'
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_x_speed, player_y_speed):
        super().__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed

    def update(self):
        if self.rect.x <= 420:
            self.side = 'right'
        if self.rect.x >= win_widht -85:
            self.side = 'left'
        if self.side == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed


class Bullet(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_x_speed, player_y_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = speed
    def update(self):
        self.rect.x += self.speed
        if self.rect.x > win_width+10:
            self.kill()


win_width = 700
win_height = 500
display.set_caption("Лабиринт")
window = display.set_mode((win_width, win_height))
back = (119, 210, 223)

barriers = sprite.Group()
bullets = sprite.Group()
monsters = sprite.Group()

w1 = GameSprite('bg.jpg',win_width/2 - win_width/3, win_height/2,300,50)
w2 = GameSprite('bg.jpg',370,100,50,400)

barriers.add(w1)
barriers.add(w2)


packman = Player('barackobama.png',5,win_height - 80,80,80,0,0)
final_sprite = GameSprite('boxing.jpg', win_widht - 85, win_height - 100, 80, 80)

monster1 = Enemy('devil.png', win_width - 80, 150, 80, 80, 5)
monster2 = Enemy('devil.png', win_width - 80, 230, 80, 80, 5)

monsters.add(monster1)
monsters.add(monster2)

finish = False
#игровой цикл дарын лох
run = True
while run:
    time.delay(50)

    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type ==KEYDOWN:
            if e.key == K_LEFT:
                packman.x_speed = 5
            elif e.key == :
                packman.x_speed = 5
            elif e.key == :
                packman.x_speed = 5
            elif e.key == :
                packman.x_speed = 5
            elif e.key == :
                packman.x_speed = 5

    if finish != True:
        window.blit(background,(0, 0))
        player,update()
        player.reset()
        final.reset()
        if sprite.collide_rect(player, final):
            finish = True
            window.blit(win, (0, 0))

    barriers.draw(window)
    packman.reset()
    packman.update()
    display.update()
    