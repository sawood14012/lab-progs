from tsp_solver.greedy import solve_tsp

D = [[],
     [1.0],
     [2.0, 3.0]]

path = solve_tsp( D )

#will print [1,0,2], path with total length of 3.0 units
print(path)
