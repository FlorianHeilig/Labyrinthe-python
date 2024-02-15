# Example file showing a circle moving on screen
import pygame
import random
from utils import Pos
# pygame setup
pygame.init()

#constantes
tilesize = 32 # taille d'une tuile IG
size = (20, 10) # taille du monde
fps = 30 # fps du jeu
snake_speed = 150 # vitesse du joueur
next_move = 0 #tic avant déplacement
fruit_pos = Pos(random.randint(0, size[0] - 1), random.randint(0, size[1] - 1))
score = 0
snake_pos = Pos(0,1)
snake_body = [(snake_pos.x, snake_pos.y)] 

# color
ground_color = "#EDDACF"
grid_color = "#7F513D"
snake_color = "#9F715D"
fruit_color = "#10015D"


screen = pygame.display.set_mode((size[0]*tilesize, size[1]*tilesize))
clock = pygame.time.Clock()
running = True
dt = 0
show_grid = True
show_pos = False

direction = "UP"

snake_pos = pygame.Vector2(round(size[0]/8), round(size[1]/2))

#tour de boucle, pour chaque FPS
while running:
    screen.fill(ground_color)

    # lecture clavier / souris
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z or event.key == pygame.K_UP:
                direction = 'UP'
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                direction = 'DOWN'
            if event.key == pygame.K_q or event.key == pygame.K_LEFT:
                direction = 'LEFT'
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                direction = 'RIGHT'

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print("mouse_pos:", pos)
    


    next_move += dt
    # gestion des déplacements
    if next_move>0:
        if direction == 'UP':
            snake_pos.y -= 1
            next_move = -snake_speed
        elif direction == 'DOWN':
            snake_pos.y += 1
            next_move = -snake_speed
        elif direction == 'LEFT':
            snake_pos.x -= 1
            next_move = -snake_speed
        elif direction == 'RIGHT':
            snake_pos.x += 1
            next_move = -snake_speed

        # vérification du déplacement du joueur
        if snake_pos.y < 0:
            snake_pos.y = 0
        if snake_pos.y >= size[1]:
            snake_pos.y = size[1]-1
        if snake_pos.x < 0:
            snake_pos.x = 0
        if snake_pos.x > size[0]-1:
            snake_pos.x = size[0]-1

        if show_pos:
            print("pos: ",snake_pos)


    # affichage des différents composants
    if show_grid:
        for i in range(1,size[0]):
            pygame.draw.line(screen,grid_color, (tilesize*i, 0), (tilesize*i, tilesize*size[0]) )
        for i in range(0,size[1]):
            pygame.draw.line(screen,grid_color, (0, tilesize*i), (tilesize*size[0], tilesize*i) )

    #affichage du joueur
    pygame.draw.rect(screen, snake_color, pygame.Rect(snake_pos.x*tilesize, snake_pos.y*tilesize, tilesize, tilesize))
    pygame.draw.rect(screen, fruit_color, pygame.Rect(fruit_pos.x*tilesize, fruit_pos.y*tilesize, tilesize, tilesize))
    pygame.display.flip()
    dt = clock.tick(fps)

pygame.quit()