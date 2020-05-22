def grid_walk(grid, x, y):
    if grid[x][y] == 2:
        print(f'found at {x, y}')
        return True
    elif grid[x][y] == 1:
        print(f'wall at {x, y}')
        return False
    elif grid[x][y] == 3:
        print(f'already visited at {x, y}')
        return False
    
    print(f'visiting {x, y}')
    grid[x][y] = 3

    width = len(grid) - 1
    height = len(grid[0]) - 1
    if x < width and grid_walk(grid, x + 1, y):
        return True
    elif y > 0 and grid_walk(grid, x, y - 1):
        return True
    elif x > 0 and grid_walk(grid, x - 1, y):
        return True
    elif y < height and grid_walk(grid, x, y + 1):
        return True
    
    return False


grid = [[0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 0],
        [0, 1, 1, 0, 0, 1],
        [0, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 2]]


grid_walk(grid, 0, 0)