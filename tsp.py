import math
import random
import matplotlib.pyplot as plt
import numpy as np

# Function to calculate the total distance (energy) of the tour
def total_distance(tour, distance_matrix):
    return sum(
        distance_matrix[tour[i]][tour[(i + 1) % len(tour)]]
        for i in range(len(tour))
    )

# Function to swap two cities in the tour (used for generating neighbors)
def swap_two(tour):
    a, b = random.sample(range(len(tour)), 2)
    tour[a], tour[b] = tour[b], tour[a]
    return tour

# Function to plot the 2D tour with real-time updates
def plot_tour_2d(tour, cities, ax, iteration, distance_matrix, temperature, energy):
    ax.clear()
    
    # Plot all possible edges (Complete Graph) - every pair of cities is connected
    for i in range(len(cities)):
        for j in range(i+1, len(cities)):  # Plot edges once
            x_vals = [cities[i][0], cities[j][0]]
            y_vals = [cities[i][1], cities[j][1]]
    
    # Plot the tour path (ensure it closes by connecting the last city back to the first one)
    xs = [cities[i][0] for i in tour] + [cities[tour[0]][0]]
    ys = [cities[i][1] for i in tour] + [cities[tour[0]][1]]
    
    ax.plot(xs, ys, 'o-', label=f"Iteration {iteration}", color='blue')  # Blue for the current tour path
    ax.set_title(f"Simulated Annealing TSP\nTemp: {temperature:.2f} | Energy: {energy:.2f}")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")

    # Plot weights (distances) on the edges in red
    for i in range(len(tour)):
        start = tour[i]
        end = tour[(i + 1) % len(tour)]
        x_mid = (cities[start][0] + cities[end][0]) / 2
        y_mid = (cities[start][1] + cities[end][1]) / 2
        weight = distance_matrix[start][end]
        ax.text(x_mid, y_mid, f"{weight:.1f}", fontsize=8, color='red')

    # Plot nodes with alphabetic labels (A, B, C, ..., T)
    for i, (x, y) in enumerate(cities):
        ax.text(x, y, f'{chr(65 + i)}', fontsize=12, ha='center', color='black')

    plt.draw()
    plt.pause(0.001)

# Simulated Annealing Algorithm to solve the TSP
def simulated_annealing(cities, distance_matrix, T=10000, alpha=0.995, stop_T=1e-8):
    current_tour = list(range(len(cities)))
    random.shuffle(current_tour)  # Randomly shuffle the cities to start with
    current_cost = total_distance(current_tour, distance_matrix)
    best_tour = current_tour[:]
    best_cost = current_cost

    fig, ax = plt.subplots()  # 2D plotting
    iteration = 0

    while T > stop_T:
        # Generate a new tour by swapping two cities
        candidate_tour = swap_two(current_tour[:])
        candidate_cost = total_distance(candidate_tour, distance_matrix)

        # Accept the candidate tour if it's better, or probabilistically if worse
        if candidate_cost < current_cost or random.random() < math.exp((current_cost - candidate_cost) / T):
            current_tour = candidate_tour
            current_cost = candidate_cost

            if candidate_cost < best_cost:
                best_tour = candidate_tour
                best_cost = candidate_cost

        T *= alpha  # Cooling the temperature
        iteration += 1
        plot_tour_2d(current_tour, cities, ax, iteration, distance_matrix, T, current_cost)

    plt.close(fig)  # Close the plot after the simulation ends
    return best_tour, best_cost


# Function to generate random cities in a 2D plane
def generate_random_cities(n):
    return [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(n)]

# Function to calculate the distance matrix based on Euclidean distance
def calculate_distance_matrix(cities):
    n = len(cities)
    distance_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = cities[i]
            x2, y2 = cities[j]
            distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            distance_matrix[i][j] = distance_matrix[j][i] = distance
    return distance_matrix


# Generate 20 random cities and calculate the distance matrix
cities = generate_random_cities(20)
distance_matrix = calculate_distance_matrix(cities)

# Call the simulated annealing function
best_tour, best_cost = simulated_annealing(cities, distance_matrix)

# Print the result
print(f"Best tour: {best_tour}")
print(f"Best cost: {best_cost}")
