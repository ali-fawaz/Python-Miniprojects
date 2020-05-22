import random
import time
import pygame


def create_grid(width, height):
    return [[0 for x in range(width)] for y in range(height)]


def init_grid(grid, chance_born):
    width = len(grid[0])
    height = len(grid)

    for row in range(height):
        for column in range(width):
            if random.random() <= chance_born:
                grid[row][column] = 1


def count_alive_neighbors(grid, x, y):
    width = len(grid[0])
    height = len(grid)

    alive_count = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            neighbor_x = x + i
            neighbor_y = y + j

            if i == 0 and j == 0:
                continue
            elif neighbor_x < 0 or neighbor_y < 0 or neighbor_y >= height or neighbor_x >= width:
                alive_count += 1
            elif grid[neighbor_y][neighbor_x] == 1:
                alive_count += 1

    return alive_count


def next_step(grid):
    width = len(grid[0])
    height = len(grid)

    new_grid = create_grid(width, height)

    for x in range(width):
        for y in range(height):
            alive_neighbors = count_alive_neighbors(grid, x, y)

            if grid[y][x] == 1:
                if alive_neighbors in [2, 3]:
                    new_grid[y][x] = 1
                else:
                    new_grid[y][x] = 0
            else:
                if alive_neighbors == 3:
                    new_grid[y][x] = 1
                else:
                    new_grid[y][x] = 0

    return new_grid


width, height = 60, 30
grid = create_grid(width, height)
init_grid(grid, 0.2)

num_steps = 15
birth_limit, death_limit = 3, 3

screen_width, screen_height = width * 16, height * 16
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.init()


def draw_grid(grid):
    width = len(grid[0])
    height = len(grid)

    grass = pygame.image.load('./tiles/grass.png')
    wall = pygame.image.load('./tiles/wall.png')

    for x in range(width):
        for y in range(height):
            if grid[y][x] == 1:
                screen.blit(grass, (x * 16, y * 16))
            elif grid[y][x] == 0:
                # screen.blit(wall, (x * 16, y * 16))
                pass

    pygame.display.flip()


print('Enter number of steps to be taken')
num_steps = int(input())
game_ended = False
while not game_ended:
    draw_grid(grid)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                game_ended = True
        if event.type == pygame.KEYDOWN:
            for i in range(num_steps):
                grid = next_step(grid)
                draw_grid(grid)
                time.sleep(0.1)
                game_ended = True

    pygame.display.flip()

input()