import pygame
import random


from project.models.board import Board

HEIGHT = 30
WIDTH = 60
SIZE = 20
NUMBER_INIT_CELL = 300
CELL_COLOR = (0, 0, 0)
FPS = 5

game = Board(HEIGHT, WIDTH)

random_positions = random.sample([[row, col] for row in range(HEIGHT - 1) for col in range(WIDTH -1 ) ], NUMBER_INIT_CELL)
game.set_initial_grid(tuple(random_positions))

pygame.init()

screen = pygame.display.set_mode((WIDTH * SIZE, SIZE * HEIGHT))
pygame.display.set_caption("Jeu de la vie - baudrysouvignet.fr")



def draw_rect():
    grid = game.grid
    coordinate = [
        (cell.x, cell.y)
        for row in grid
        for cell in row
        if cell.state
    ]

    for block in coordinate:
        pygame.draw.rect(screen, CELL_COLOR, (block[0]*SIZE, block[1]*SIZE, SIZE, SIZE))




clock = pygame.time.Clock()
running = True
paused = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused

    screen.fill((255, 255, 255))

    draw_rect()
    pygame.display.flip()

    if not paused:
        game.next_grid()
    clock.tick(FPS)

