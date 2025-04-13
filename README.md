# Traveling Salesman Problem (TSP) using Simulated Annealing

**Ardit Shabani**  
**University for Business and Technology, 10000 Prishtinë, Kosovo**  
**as53656@ubt-uni.net**

## 1   Introduction
The Traveling Salesman wants to visit each of the set of cities exactly once, starting from and returning to his home city. The problem is to find the shortest road path for this trip. The TSP problem is part of the NP-hard problems which are problematic to solve and computationally challenging as the number of the cities increases.
TSP has application in logistic, supply chain management, circuit design and operations research. Efficient solutions can optimize delivery routes, reduce operational costs, and improve performance in scheduling and resource allocation. 
The main objectives of this project are to implement the Simulated Annealing algorithm to solve the TSP, analyze its effectiveness in obtaining near-optimal solutions, and compare its computational efficiency with traditional approaches.

## 2   Literature Review

The Traveling Salesman Problem is wildly studied in the domain of the combinatorial optimization. Its goal is simple to state: find the shortest possible route that visits each city once and returns to the origin city. However, solving it efficiently for large datasets remains a challenge due to its complexity.

Approaches like Brute Force, Dynamic Programming (Held-Karp Algorithm), and Branch and Bound provide optimal solutions but are computationally expensive. They guarantees optimal solutions but are impractical with large TSP. 
Methods such as Heuristics Algorithms are simple and fast. These algorithms starts from a city and repeatedly visits the nearest unvisited city. They are fast and easy to implement but often far from optimal and highly demanded on the starting city. 
Genetic Algorithms (GA), Simulated Annealing (SA), Ant Colony Optimization (ACO) they all aim to find the near-optimal solution by simulating natural processes. These algorithms can find high-quality solutions for large instances, but to not guarantee the optimal solution. 

## 3   Problem Definition and Formulation

Lets consider a complete graph. A round-trip of the cities corresponds to some subset of the lines, and is called a tour or a Hamiltonian cycle in graph theory. The length of a tour is the sum of the lengths of the lines in the roundtrip. 
Given:

	+ G=(V,E) be a complete, weighted, undirected graph.
	+ V={v1,v2,...,vn} be the set of n cities (nodes).
	+ dij be the distance (or cost) between city i and city j where dij = dji and dii = 0.
	+ Let xij be a binary decision variable such that:
  
```math
xij={\left(\frac{\text{1 if the tour goes directly from city i to j}}{otherwise}\right)}
```
Our objective function is to find the of the path that its cost function is the lowest.


```math
minimize \sum_{i=1}^n \sum_{j=1}^n dij × xij
```


## 4   Algorithm Design
This paper will describe the use of Simulated Annealing algorithm for solving the TSP problem. Simulated Annealing is an probabilistic method which is used for finding the global minimum of a cost function which can include some local minima (Bertsimas & Tsitsiklis, 1993). It is based on metallurgy, it works while emulating an physical process where a solid is cooled in a slowed way until eventually it’s structure is cooled entirely, this process is realized with a minimal configuration of the energy. 

The following pseudocode will explain it’s flow:
```
M = number of moves to attempt
T = current temperature
S = current solution
    ∆E= total cost of S

for m = 1 to M {
	
Generate a random move ,try a new route between       two nodes
	Evaluate the change in energy (cost), ∆E;
	Decrease the temperature

	if (∆E  < 0)
		accept this move and update the configuration;

else 
	accept with the probability P=e^(-∆E/T)
	update the configuration if accepted

  end of loop

  return the best solution
```
Simulated Annealing is very effective when it comes to a large and complex problem. For a large and complex TSP simulated annealing works fast while finding not an the ideal solution but a very optimal one that can be accepted as a very good solution. While the brute force algorithm would find the ideal solution it will take enormous time comparing to simulated annealing algorithm especially when it comes to large TSP. The key part of the simulated annealing algorithm which does make it a very good algorithm for large and complex TSPs is that while searching for minimums it does sometimes accepts the route with the worst cost between two nodes but while optimizing the cost of the overall route.

## References
- Bertsimas, D., & Tsitsiklis, J. (1993). Simulated annealing. Statistical science, 8(1), 10-15. 


