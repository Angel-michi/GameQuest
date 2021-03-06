import pygame 
import random 

WIDTH = 480 
HEIGHT = 600 
FPS = 60
SCORE = 0

#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#initialize pygame and start window 
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GOTHAM'S DEFENDER")
clock= pygame.time.Clock()

#player sprite 
class Player(pygame.sprite.Sprite):
    def __init__(self): 
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0 
#defines how the player will move
    def update(self):
        self.speedx = 0 
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.speedx = -5
        if keystate[pygame.K_d]:
            self.speedx = 5
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
             self.rect.right = WIDTH
        if self.rect.left < 0:
             self.rect.left = 0
#enemy mobs 
class Mob(pygame.sprite.Sprite):
    def __init__(self): 
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30,40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1,5)

    def update(self):
        self.rect.y += self.speedy
        if rect.top > HEIGHT + 10: 
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1,5)
#load in sprites
all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
#determines the number of mobs that spawn in 
for i in range (8):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

#Game loop
running = True 
while running:
    #keep loop running at the right speed
    clock.tick (FPS)
    #Process input (events)
    for event in pygame.event.get():
        #check for closing window 
        if event.type == pygame.QUIT: 
            running = False

    #update 
    all_sprites.update()

    #Draw / render 
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # after drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
