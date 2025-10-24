#import required libraries
import pygame, sys, random, time

#initialize pygame
pygame.init() 

#Pre-defined Values
WIDTH, HEIGHT = 750, 750
player_x=345
player_y=660
player_speed=1
light= ["GREEN", 'RED', 'NONE']
current_light=random.choice(light)
switch=random.randint(2,4)  #light will switch every 2-5 seconds
last_switch = time.time()  #tracks when lights last switched
sound_played=False
game_over=False

#fonts
font = pygame.font.Font(None, 50)

#images used
player_still=pygame.image.load(r'C:\Users\janha\OneDrive\Desktop\GAME CS1101\Assets\player_still.png')
player_still=pygame.transform.scale(player_still, (70, 90))
player_run=pygame.image.load(r'C:\Users\janha\OneDrive\Desktop\GAME CS1101\Assets\player_run.png')
player_run=pygame.transform.scale(player_run, (70, 90))
doll_front=pygame.image.load(r'C:\Users\janha\OneDrive\Desktop\GAME CS1101\Assets\doll_front.png')
doll_front=pygame.transform.scale(doll_front, (70, 90))
doll_back=pygame.image.load(r'C:\Users\janha\OneDrive\Desktop\GAME CS1101\Assets\doll_back.png')
doll_back=pygame.transform.scale(doll_back, (70, 90))
ground=pygame.image.load(r'C:\Users\janha\OneDrive\Desktop\GAME CS1101\Assets\Playground.png')
ground_green=pygame.image.load(r'C:\Users\janha\OneDrive\Desktop\GAME CS1101\Assets\ground_green.png')
ground_red=pygame.image.load(r'C:\Users\janha\OneDrive\Desktop\GAME CS1101\Assets\ground_red.png')
eliminated=pygame.image.load(r'C:\Users\janha\OneDrive\Desktop\GAME CS1101\Assets\eliminated.png')
win=pygame.image.load(r'C:\Users\janha\OneDrive\Desktop\GAME CS1101\Assets\WIn.png')

#sounds
red_light=pygame.mixer.Sound(r'C:\Users\janha\OneDrive\Desktop\GAME CS1101\Assets\Red Light.mp3')
green_light=pygame.mixer.Sound(r'C:\Users\janha\OneDrive\Desktop\GAME CS1101\Assets\Green light.mp3')
doll_song=pygame.mixer.Sound(r'C:\Users\janha\OneDrive\Desktop\GAME CS1101\Assets\RLGL song.mp3')

#screen setup
screen=pygame.display.set_mode((WIDTH, HEIGHT))
caption=pygame.display.set_caption("Red Light, Green Light")
screen.blit(ground, (0,0))
pygame.display.update()

#player setup
screen.blit(player_still, (player_x, player_y))
pygame.display.update()

# Clock for controlling FPS
clock = pygame.time.Clock()

#Main Game Loop
while True:
    #For quitting the game using red cross icon
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

    #light switching
    if time.time()-last_switch > switch:
        current_light=random.choice(light) #randomly chooses a colour option from light list
        last_switch=time.time()
        sound_played=False

    #sound on lights
    if not sound_played:
        if current_light=="RED":
            red_light.play()
        elif current_light=="GREEN":
             green_light.play()
        sound_played=True



    #player movement using keyboard inputs
    keys=pygame.key.get_pressed()
    movement=False
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        player_y-=player_speed
        movement=True
    
    #Redraw 
    screen.blit(ground, (0,0))
    screen.blit(player_run if keys[pygame.K_w] or keys[pygame.K_UP] else player_still, (player_x, player_y))

    #doll setup
    if current_light=="RED":
        screen.blit(doll_front, (345,0))
    else:
        screen.blit(doll_back, (345, 0))

    if current_light=="RED":
        screen.blit(doll_front, (345, 0))
        doll_song.stop()
    else:
        if not pygame.mixer.get_busy():
            doll_song.play(-1)

    #Update Display
    pygame.display.flip()
    clock.tick(60)

    #Conditions for winning and losing
    if current_light=="RED" and movement:
        screen.blit(eliminated, (140,100))
        pygame.display.update()
        pygame.time.delay(2000)  #  elimination screen
        pygame.quit()
        sys.exit()

    if player_y==20:
        screen.blit(win, (140,100))
        pygame.display.update()
        pygame.time.delay(3000)  #winning screen
        pygame.quit()
        sys.exit()