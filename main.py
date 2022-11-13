import pygame
import math
import random

screen_width = 605
screen_height = 390

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Destroy the Socks!")



# background
background = pygame.image.load("Moxie Background.png")

pygame.init()

# player
playerimg = pygame.image.load('New Piskel-1.png.png')
playerX = 100
playerY = 200
playerX_change = 0

# enemy
enemyimg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyimg.append(pygame.image.load('Sock-1.png.png'))
    enemyX.append(random.randint(0, 599))
    enemyY.append(random.randint(50, 100))
    enemyX_change.append(1)
    enemyY_change.append(40)

# Bullet

bulletimg = pygame.image.load('poop-1.png.png')
bulletX = 0
bulletY = 210
bulletY_change = 5
bullet_state = "ready"


score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

over_font =pygame.font.Font('freesansbold.ttf', 64)



def show_score(x, y):
    score = font.render("Score :" + str(score_value), True, (0, 0, 0))
    screen.blit(score, (x, y))

def game_over_text(x, y):
    over_text = over_font.render("Game Over", True, (0, 0, 0))
    screen.blit(over_text, (210, 270))

def player(x, y):
    screen.blit(playerimg, (x, y))

def enemy (x, y, i):
    screen.blit(enemyimg[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX, 2)) + (math.pow(enemyY-bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False



run = True
while run:

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1
            if event.key == pygame.K_RIGHT:
                playerX_change = 1
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change

    if playerX <= -25:
        playerX = -25
    elif playerX >= 480:
        playerX = 480

    for i in range(num_of_enemies):

        if enemyY[i] > 210:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text(200, 270)
            break

        enemyX[i] += enemyX_change[i]

        if enemyX[i] <= -10:
            enemyX_change[i] = 1.5
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 600:
            enemyX_change[i] = -1.5
            enemyY[i] += enemyY_change[i]

        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 210
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 599)
            enemyY[i] = random.randint(50, 100)

        enemy(enemyX[i], enemyY[i], i)

    if bulletY <= 0:
        bulletY = 210
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change



    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()



