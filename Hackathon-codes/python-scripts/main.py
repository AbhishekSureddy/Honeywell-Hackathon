from utils import *

# grid size
n = 100
population_grid = np.random.randint(0, 2,size = (n,n))
# population_grid

# animation
padded_population_grid = padd_population(population_grid,n)
fig = plt.figure(figsize=(10,10))
im = plt.imshow(population_grid, cmap='gray',animated=True)
i = 1
def updatefig(*args):
    global padded_population_grid, n, population_grid, i
    padded_population_grid = padd_population(population_grid,n)
    offsprings = next_generation(padded_population_grid, n)
    population_grid = offsprings
    plt.xticks([]), plt.yticks([])
    plt.title(f"Offspring generation : {i +1}")
    im = plt.imshow(population_grid,cmap='gray', animated=True)
    i+=1
    time.sleep(1)
    return [im]

# %matplotlib notebook
ani = animation.FuncAnimation(fig, updatefig, interval=500, blit=True)
plt.show()