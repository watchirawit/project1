# Game Shoot the fruit
import pgzrun
from random import randint

# define size of the windows
WIDTH = 640
HEIGHT = 480
#ค่าคงที่ต่างๆ
score = 0
missing = 3
game_over = False
# create object
csgoh2 = Actor('csgoh2')
orange = Actor('orange')



# function for display
def draw():
    screen.fill('white')
    csgoh2.draw()
    screen.draw.text('Score     : '+str(score), color='black', topleft=(10, 10))
    screen.draw.text('Missing : '+str(missing), color='black', topleft=(10, 30))
    if game_over or missing == 0:
        screen.fill('black')
        message = 'Final Score : '+str(score) 
        screen.draw.text(message,  topleft=(10, 10), fontsize=50)
        



# function random position of apple
def place_csgoh2():#การสุ่มตำแหน่งการเกิดใหม่
    csgoh2.x = randint(10, 600)
    csgoh2.y = randint(10, 400)
    



# function to get mouse event
def on_mouse_down(pos):
    global score
    global missing
    if score >= 0 or score <= 0: 
        if csgoh2.collidepoint(pos):
            score += 1
            place_csgoh2()
        else:
            if score > 0:
                score -= 1
            
            missing -= 1
def time_up():
    global game_over
    game_over = True           
            
    
    
        
    

clock.schedule(time_up, 30.0)
place_csgoh2()
pgzrun.go()
