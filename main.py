from tsp import simulated_annealing
from utils import generate_cities, compute_distance_matrix

if __name__ == "__main__":
    num_cities = int(input("Enter number of cities: "))
    cities = generate_cities(num_cities)
    distance_matrix = compute_distance_matrix(cities)

    print("Running simulated annealing with 3D visualization...")
    final_tour, final_cost = simulated_annealing(cities, distance_matrix)

    print("Final tour:", final_tour)
    print(f"Total distance: {final_cost:.2f}")
