import numpy as np
import matplotlib.animation as mpa
import matplotlib.pyplot as plt


def init(size=(28,28)):
    #cell_grid = np.random.randint(0,2,size=size)
    cell_grid =np.zeros(size)
    for _ in range(80):
        i = np.random.randint(0, 28)
        j = np.random.randint(0, 28)
        cell_grid[i,j] = 1

    print('done')
    return cell_grid

#define the rules of games of life
def update_state(neighbours,cell_state):

    #deines the rules
    #birth due to reproduction
    if cell_state == 0 and neighbours == 3:
        return 1

    #dies due to underpopulation
    elif cell_state == 1 and neighbours < 2:
        return 0

    #dies due to overpopulation
    elif cell_state == 1 and neighbours > 3:
        return 0

    #next generartion,state doest not change
    return cell_state

def neighbours(cell_grid,index):

    count = 0
    i,j = index
    length = cell_grid.shape[0]

    #get neighbours cell indices
    neighbours_index = [[i-1,j],
                        [i-1,j-1],
                        [i-1,j+1],
                        [i,j-1],
                        [i+1,j-1],
                        [i+1,j+1],
                        [i+1,j],
                        [i,j+1]]

    #adjust the indices for cell at the edges
    for idx in range(len(neighbours_index)):

        if neighbours_index[idx][0] == -1:
            neighbours_index[idx][0] = length -1

        if neighbours_index[idx][0] == length:
            neighbours_index[idx][0] = 0

        if neighbours_index[idx][1] == -1:
            neighbours_index[idx][1] = length -1

        if neighbours_index[idx][1] == length:
            neighbours_index[idx][1] = 0


    for ij in neighbours_index:
        count += cell_grid[ij[0],ij[1]]

    return count


def game_of_life(cell_grid):

    length = cell_grid.shape[0]

    for i in range(length):
        for j in range(length):
            cell_grid[i,j] = update_state(neighbours=neighbours(cell_grid, index=(i,j)),
                                            cell_state=cell_grid[i,j])
    return cell_grid

cell_grid = init()

def update(f):

    cell_grid_ = game_of_life(cell_grid)
    plt.imshow(cell_grid_,cmap='gray')

ani = mpa.FuncAnimation(plt.gcf(), update)

plt.show()
