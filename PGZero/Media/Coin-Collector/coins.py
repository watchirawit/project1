# Game Coins Collector
import pgzrun
from random import randint
# define window size
WIDTH = 800
HEIGHT = 600

# define variable
score = 0
game_over = False


# Create object
alien = Actor('alien')
alien.pos = 100, 100
coin = Actor('coin')
coin.pos = 200, 200


def draw():
    screen.fill('black')
    alien.draw()
    coin.draw()
    screen.draw.text('Score : '+str(score), color='white', topleft=(10, 10))#topleft=(10 , 10) topleft คือ ตำแหน่งการว่างข้อความ  fontsizeคือขนาดของฟอนต์
    if game_over:
        screen.fill('pink')
        message = 'Final Score : '+str(score)
        screen.draw.text(message, topleft=(10, 10), fontsize=50)#topleft=(10 , 10) fontsize=50


def place_coin():
    coin.x = randint(20, (WIDTH - 20))
    coin.y = randint(20, (HEIGHT - 20))


def update():#ความเร็วของตัวละคร
    global score
    if keyboard.left:
        alien.x = alien.x - 15 #simple is 4
    elif keyboard.right:
        alien.x = alien.x + 15
    elif keyboard.up:
        alien.y = alien.y - 15
    elif keyboard.down:
        alien.y = alien.y + 15

    coin_collected = alien.colliderect(coin)
    if coin_collected:
        place_coin()
        score += 1


def time_up():
    global game_over
    game_over = True


clock.schedule(time_up, 60.0)
place_coin()
pgzrun.go()
