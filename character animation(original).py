import pygame
pygame.init()

win_width=700
win_height=550

win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Jumping man")

walk_right = [pygame.image.load('assets/R1.png'), pygame.image.load('assets/R2.png'), pygame.image.load('assets/R3.png'), pygame.image.load('assets/R4.png'), pygame.image.load('assets/R5.png'), pygame.image.load('assets/R6.png'), pygame.image.load('assets/R7.png'), pygame.image.load('assets/R8.png'), pygame.image.load('assets/R9.png')]
walk_left = [pygame.image.load('assets/L1.png'), pygame.image.load('assets/L2.png'), pygame.image.load('assets/L3.png'), pygame.image.load('assets/L4.png'), pygame.image.load('assets/L5.png'), pygame.image.load('assets/L6.png'), pygame.image.load('assets/L7.png'), pygame.image.load('assets/L8.png'), pygame.image.load('assets/L9.png')]
char_still = pygame.image.load('assets/standing.png')

bg = pygame.image.load('assets/game background.png')
bg = pygame.transform.scale(bg, (win_width, win_height))


class player():
    def __init__(self, x, y, height, width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.vel = 5
        self.jump = False
        self.jump_count = 7
        self.left = False
        self.right = False
        self.walk_count = 0

    def draw(self):
        if self.walk_count >= 18:
            self.walk_count = 0

        if self.left:
            win.blit(walk_left [self.walk_count // 2], (self.x, self.y))
            self.walk_count += 1
        elif self.right:
            win.blit(walk_right [self.walk_count // 2], (self.x, self.y))
            self.walk_count += 1
        else:
            win.blit(char_still, (self.x, self.y))

       
        

def redrawGameWin():
    win.blit(bg, (0, 0))
    man.draw()
        
    pygame.display.update()
    

man = player(100, 317, 64, 64)

run = True
while run:
    pygame.time.delay(35)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
    elif keys[pygame.K_RIGHT] and man.x < win_width - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
    else:
        man.right = False
        man.left = False
        man.walk_count = 0

    if not(man.jump):
        if keys[pygame.K_UP]:
            man.jump = True
            
    else:
        if man.jump_count >= -7:
            neg = 1
            if man.jump_count < 0:
                neg = -1
            man.y -= (man.jump_count ** 2)* neg
            man.jump_count -= 1
        else:
            man.jump = False
            man.jump_count = 7

    redrawGameWin()
    
pygame.quit()

