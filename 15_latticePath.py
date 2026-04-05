import pprint


#create empty grid
grid = [[0] * 21 for _ in range(21)]

#fill top row
for i in range(21):
    grid[0][i] = 1
    grid[i][0] = 1 #left column

#fill the rest
for r in range(1,21):
    for c in range(1,21):
        grid[r][c] = grid[r-1][c] + grid[r][c-1]

pprint.pprint(grid[20][20])


