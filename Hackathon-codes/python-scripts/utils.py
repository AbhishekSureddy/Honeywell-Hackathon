# libraries
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

# utility functions
def next_generation(padded_population_grid, n):
    offsprings = np.zeros((n,n))
    # summ_vals = np.zeros((n,n))
    for i in range(1,n+1):
        for j in range(1,n+1):
            summ = np.sum(padded_population_grid[i-1:i+2,j-1:j+2])
            # if cell is alive
            if padded_population_grid[i,j]==1:
                if (summ ==3 or summ==4):
                    offsprings[i-1,j-1] = 1
            else:
                if summ==3:
                    offsprings[i-1,j-1] = 1
    #         summ_vals[i-1,j-1] = summ
    return offsprings

def padd_population(population_grid,n):
	padded_population_grid = np.zeros((n+2,n+2))
	padded_population_grid[1:n+1,1:n+1] = population_grid
	return padded_population_grid

def plot_population(population_grid, title = "Initial Population"):
    plt.figure(figsize=(10,10))
    plt.imshow(population_grid,cmap='gray')
    plt.xticks([]), plt.yticks([])
    plt.title(title)
    plt.show()