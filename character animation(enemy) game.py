import pygame
pygame.init()

win_width=700
win_height=550

win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Jumping man")

clock = pygame.time.Clock()

bg = pygame.image.load('assets/game background.png')
bg = pygame.transform.scale(bg, (win_width, win_height))

score = 0

class player():
    walk_right = [pygame.image.load('assets/R1.png'), pygame.image.load('assets/R2.png'), pygame.image.load('assets/R3.png'), pygame.image.load('assets/R4.png'), pygame.image.load('assets/R5.png'), pygame.image.load('assets/R6.png'), pygame.image.load('assets/R7.png'), pygame.image.load('assets/R8.png'), pygame.image.load('assets/R9.png')]
    walk_left = [pygame.image.load('assets/L1.png'), pygame.image.load('assets/L2.png'), pygame.image.load('assets/L3.png'), pygame.image.load('assets/L4.png'), pygame.image.load('assets/L5.png'), pygame.image.load('assets/L6.png'), pygame.image.load('assets/L7.png'), pygame.image.load('assets/L8.png'), pygame.image.load('assets/L9.png')]
    char_still = pygame.image.load('assets/standing.png')

    def __init__(self, x, y, height, width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.vel = 5
        self.jump = False
        self.jump_count = 8
        self.left = False
        self.right = False
        self.walk_count = 0
        self.stand = False
        self.alive = True
        self.hitbox = (self.x + 14, self.y + 8, 34, 56)
        self.health = 100

    def draw(self, win):
        if self.alive:

            if self.walk_count >= 27:
                self.walk_count = 0

            if self.left:
                win.blit(self.walk_left [self.walk_count // 3], (self.x, self.y))
                self.walk_count += 1
            elif self.right:
                win.blit(self.walk_right [self.walk_count // 3], (self.x, self.y))
                self.walk_count += 1
            elif self.stand:
                win.blit(self.char_still, (self.x, self.y))
            
            else:
                if self.right:
                    win.blit(self.walk_right[0], (self.x, self.y))
                else:
                    win.blit(self.walk_right[0], (self.x, self.y))

            self.hitbox = (self.x + 14, self.y + 8, 34, 56)
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

        playerHealth = font2.render('Player Health: ', 1, (0, 0, 0))
        win.blit(playerHealth, (win_width - 690, win_height - 527))

        pygame.draw.rect(win, (255, 0, 0), (win_width - 546, win_height - 528 , 102, 22), 2)
        pygame.draw.rect(win, (0, 255, 0), (win_width - 545, win_height - 527 , self.health, 20))

    def hit(self):
        global score
        self.health -= 10

        if self.health < 0:
            score -= 10
            self.jump = False
            self.x = 50
            self.y = 319
            self.walk_count = 0
            self.health = 100
            i = 0
 
            
            #to show death message
            deadMessage = font3.render('You Died (Score -10)', 1, (255, 0, 0))
            win.blit(deadMessage, ((win_width//2) - (deadMessage.get_width()//2), (win_height//2) - (deadMessage.get_height()//2)))
            pygame.display.update()

            #to play death message for longer
            while i < 100:
                pygame.time.delay(10)
                i += 1


class projectile():
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 10 * facing

    def draw(self, win):
        pygame.draw.circle(win, (0, 0, 0), (self.x, self.y), 6)


class enemy():
    walk_right = [pygame.image.load('assets/GR1.png'), pygame.image.load('assets/GR2.png'), pygame.image.load('assets/GR3.png'), pygame.image.load('assets/GR4.png'), pygame.image.load('assets/GR5.png'), pygame.image.load('assets/GR6.png'), pygame.image.load('assets/GR7.png'), pygame.image.load('assets/GR8.png'), pygame.image.load('assets/GR9.png'), pygame.image.load('assets/GR10.png'), pygame.image.load('assets/GR11.png')]
    walk_left = [pygame.image.load('assets/GL1.png'), pygame.image.load('assets/GL2.png'), pygame.image.load('assets/GL3.png'), pygame.image.load('assets/GL4.png'), pygame.image.load('assets/GL5.png'), pygame.image.load('assets/GL6.png'), pygame.image.load('assets/GL7.png'), pygame.image.load('assets/GL8.png'), pygame.image.load('assets/GL9.png'), pygame.image.load('assets/GL10.png'), pygame.image.load('assets/GL11.png')]
    stand = pygame.image.load('assets/GStand.png')
    fall = [pygame.image.load('assets/GC1.png'), pygame.image.load('assets/GC2.png'), pygame.image.load('assets/GC3.png'),]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.vel = 4
        self.walk_count = 0
        self.hit_count = 0
        self.alive = True
        self.hitbox = (self.x + 10, self.y, 47, 58)

    def draw(self, win):
        if self.alive:

            self.move()

            if self.walk_count >= 33:
                self.walk_count = 0

            if self.vel > 0:
                win.blit(self.walk_right[self.walk_count//3], (self.x, self.y))
                self.walk_count += 1
            else:
                win.blit(self.walk_left[self.walk_count//3], (self.x, self.y))
                self.walk_count += 1

            pygame.draw.rect(win, (0, 255, 0), (self.x + 1, self.y - 12, 50, 10))
            pygame.draw.rect(win, (255, 0, 0), (self.x + 1, self.y - 12, 50 - (self.hit_count * 10), 10))
            self.hitbox = (self.x + 10, self.y, 47, 58)
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def move(self):
        if self.vel > 0:
            if self.x < self.path[1]:
                self.x += self.vel
            
            else:
                self.vel = self.vel * -1
                self.walk_count = 0

        else:
            if self.x > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walk_count = 0

    def hit(self):
        global score
        self.hit_count += 1
        score += 1
        hitIndicator = font4.render('+1', 1, (0, 0, 0))
        i = 0
        while i < 50:
            win.blit(hitIndicator, (self.x - 20, self.y - 10 ))
            pygame.display.update()
            i += 1
        

        if self.hit_count >= 5:

            score += 5
            self.hit_count = 0
            self.walk_count = 0
            self.alive = False

 
            

def redrawGameWin():
    win.blit(bg, (0, 0))
    man.draw(win)
    goblin.draw(win)
    scoreText = font.render('Score: '+ str(score), 1, (0, 0, 0))
    win.blit(scoreText, (win_width - 150, win_height - 530))
    #pygame.draw.rect(win, (0, 0, 0), (210, 222, 50, 1), 1)

    for bullet in bullets:
        bullet.draw(win)
        
    pygame.display.update()
    

font = pygame.font.SysFont('comicsans', 30, True)
font2 = pygame.font.SysFont('comicsans', 27, True)
font3 = pygame.font.SysFont('comicsans', 50, True)
font4 = pygame.font.SysFont('comicsans', 20, True)


man = player(50, 319, 64, 64)
goblin = enemy(100, 325, 64, 64, 620)
bullets = []
bullet_loop = 0

#mainloop
run = True
while run:
    clock.tick(27)

    #checking for man collision with goblin   
    if goblin.alive:
        
        if man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin.hitbox[1]:
            if man.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2] and man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0]:
                man.hit()


    if bullet_loop > 0:
        bullet_loop += 1
    if bullet_loop > 8:
        bullet_loop = 0


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    for bullet in bullets:
        if goblin.alive:

            if bullet.y > goblin.hitbox[1] and bullet.y < goblin.hitbox[1] + goblin.hitbox[3]:
                if bullet.x > goblin.hitbox[0] and bullet.x < goblin.hitbox[0] + goblin.hitbox[2]:
                    goblin.hit()
                    bullets.pop(bullets.index(bullet))

        
        if bullet.x < win_width and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()
    

    if keys[pygame.K_SPACE] and bullet_loop == 0:
        if man.left:
            facing = -1
        else:
            facing = 1

        if len(bullets) < 6 and not(man.stand):
            bullets.append(projectile(round(man.x + man.width // 2), round(man.y + man.height // 2), 6, (0, 0, 0), facing))
            bullet_loop = 1

    if keys[pygame.K_DOWN]:
        man.stand = True
        man.left = False
        man.right = False

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.stand = False
    elif keys[pygame.K_RIGHT] and man.x < win_width - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
        man.stand = False
    else:
        man.walk_count = 0

    if not(man.jump):
        if keys[pygame.K_UP]:
            man.jump = True

    else:
        if man.jump_count >= -8:
            neg = 1
            if man.jump_count < 0:
                neg = -1
            man.y -= (man.jump_count ** 2)* neg
            man.jump_count -= 1
        else:
            man.jump = False
            man.jump_count = 8

    if keys[pygame.K_r]:
        goblin.alive = True


    redrawGameWin()
    
pygame.quit()
