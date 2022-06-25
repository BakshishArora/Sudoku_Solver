import numpy as np

grid=[[5,3,0,0,7,0,0,0,0],
      [6,0,0,1,9,5,0,0,0],
      [0,9,8,0,0,0,0,6,0],
      [8,0,0,0,6,0,0,0,3],
      [4,0,0,8,0,3,0,0,1],
      [7,0,0,0,2,0,0,0,6],
      [0,6,0,0,0,0,2,8,0],
      [0,0,0,4,1,9,0,0,5],
      [0,0,0,0,8,0,0,0,0]]

def possible(row, coloumn, number):
    global grid

    for i in range (0,9):
        if grid[row][i] == number:
            return False
    for j in range(0,9):
        if grid[j][coloumn]== number:
            return False
    x0=(coloumn//3)*3
    y0=(row//3)*3

    for i in range (0,3):
        for j in range (0,3):
            if grid[y0+i][x0+j] == number:
                return False

    return True

def solve():
    global grid
    for row in range (0,9):
        for coloumn in range (0,9):
            if grid[row][coloumn] == 0:
                for number in range (1,10):
                    if possible(row,coloumn,number):
                        grid[row][coloumn]= number
                        solve()
                        grid[row][coloumn]=0
                return
            
    print(np.matrix(grid))
    input('more possible solutions')
solve()
