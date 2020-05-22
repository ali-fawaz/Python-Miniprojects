import pygame
import itertools
import random


grid = [[0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 1, 0, 0],
        [0, 1, 1, 1, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0]]

treasure_x, treasure_y = 0, 0
treasure_location = False
while not treasure_location:
    treasure_x = random.randint(0, len(grid) - 1)
    treasure_y = random.randint(0, len(grid[0]) - 1)

    if grid[treasure_x][treasure_y] == 0:
        if not (treasure_x == 0 and treasure_y == 0):
            treasure_location = True

grid[treasure_x][treasure_y] = 2


def move(grid, origin, direction):
    x, y = origin
    width = len(grid[0])
    height = len(grid)

    if direction == 'up' and x > 0:
        if grid[x - 1][y] != 1:
            return x - 1, y
        else:
            return x, y
    elif direction == 'down' and x < width:
        if grid[x + 1][y] != 1:
            return x + 1, y
        else:
            return x, y
    elif direction == 'left' and y > 0:
        if grid[x][y - 1] != 1:
            return x, y - 1
        else:
            return x, y
    elif direction == 'right' and y < height:
        if grid[x][y + 1] != 1:
            return x, y + 1
        else:
            return x, y
    else:
        return x, y


width = len(grid[0])
height = len(grid)


GAME_WIDTH, GAME_HEIGHT = width * 16, height * 16
screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.init()


def draw_grid(grid, player):
    player = pygame.image.load('./tiles/player.png')
    grass = pygame.image.load('./tiles/grass.png')
    wall = pygame.image.load('./tiles/wall.png')
    treasure = pygame.image.load('./tiles/treasure.png')

    for x, y in itertools.product(range(0, width), range(0, height)):
        if grid[y][x] in [0, 2]:
            screen.blit(grass, (x * 16, y * 16))
        elif grid[y][x] == 1:
            screen.blit(wall, (x * 16, y * 16))
    
    screen.blit(treasure, (treasure_y * 16, treasure_x * 16))
    screen.blit(player, (player_y * 16, player_x * 16))


player_x, player_y = 0, 0

game_ended = False
while not game_ended:
    draw_grid(grid, (player_x, player_y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                game_ended = True
        elif event.type == pygame.KEYDOWN:
            direction = 'none'
            if event.key == pygame.K_UP:
                direction = 'up'
            elif event.key == pygame.K_DOWN:
                direction = 'down'
            elif event.key == pygame.K_LEFT:
                direction = 'left'
            elif event.key == pygame.K_RIGHT:
                direction = 'right'
            else:
                direction = 'none'
    
            player_x, player_y = move(grid, (player_x, player_y), direction)

            if (player_x, player_y) == (treasure_x, treasure_y):
                game_ended = True

    pygame.display.flip()

print('You won the game')
