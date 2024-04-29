from pysat.formula import CNF
from pysat.solvers import Solver
from itertools import combinations
import os

# function to convert 2D position to flatten position
def convert_to_flatten(pos, size):
    num_r, num_c = size
    r, c = pos
    return (r*num_c + c + 1)

# function to convert flatten position to 2D position
def convert_to_2D(flat, size):
    num_r, num_c = size
    c = (flat-1) % num_c
    r = (flat-1) // num_c
    return r,c

# function to generate around position of a position
def generate_around(pos):
    r, c = pos
    for i in range(-1, 2):
        for j in range(-1, 2):
            yield r + i, c + j

# function to check if a position is valid
def is_valid(pos, grid, size):
    num_r, num_c = size
    r, c = pos 
    return 0 <= r < num_r and 0 <= c < num_c and grid[r][c] == '_'  

# function to generate all combinations of k elements from n elements
def list_combination(n, k):
    comb_list = list(combinations(range(1, n + 1), k))
    return comb_list

# function to generate CNF clauses for a position
def generate_CNF(pos, grid, size):
    if grid[pos[0]][pos[1]] == '_':
        return []
    
    list_cells = []
    for new_pos in generate_around(pos):
        if is_valid(new_pos, grid, size):
            list_cells.append(convert_to_flatten(new_pos, size))
    
    
    number = grid[pos[0]][pos[1]]
    num_valid = len(list_cells)
    clauses = []
    
    first_comb = list_combination(num_valid, number + 1)
    
    for comb in first_comb:
        clause = []
        for index in comb:
            clause.append(-list_cells[index - 1])
        clauses.append(clause)
    
    second_comb = list_combination(num_valid, num_valid - number + 1)
    for comb in second_comb:
        clause = []
        for index in comb:
            clause.append(list_cells[index - 1])
        clauses.append(clause)
    
    return clauses

# function to solve the SAT problem
def solve_by_pysat(grid, size):
    num_r, num_c = size
    clauses = [generate_CNF((r, c), grid, size) for r in range(num_r) for c in range(num_c)]

    cnf = CNF()
    for clause in clauses:
        cnf.extend(clause)

    with Solver(bootstrap_with=cnf) as solver:
        # Solve the SAT problem
        if solver.solve():
            # If satisfiable, get the satisfying assignment
            satisfying_assignment = solver.get_model()
            #print('Formula is satisfiable')
            return satisfying_assignment
        else:
            # If unsatisfiable
            #print('Formula is unsatisfiable')
            return None  # Or handle the unsatisfiable case accordingly

# function to output the result
def output(list_result, grid, size):
    output = grid.copy()
    num_r, num_c = size
    for r in range(num_r):
        for c in range(num_c):
            if output[r][c] != '_':
                continue
            index = r * num_c + c
            if index < len(list_result) and list_result[index] > 0:
                output[r][c] = 'T'
            else:
                output[r][c] = 'G'
    return output


# Function to read the input data from the input txt file
def read_input(input_file):
    with open(input_file, 'r') as f:
        size = tuple(map(int, f.readline().split()))
    # Read the grid, seperated by new line, split by comma
        grid = [line.strip().split(',') for line in f]
    #convert numbers in grid to int
    for i in range(size[0]):
        for j in range(size[1]):
            if grid[i][j] != '_' :
                grid[i][j] = int(grid[i][j])
    return size,grid

# Function to generate clauses for the SAT problem
def generate_clauses(size, grid):
    num_r, num_c = size
    clauses = [generate_CNF((r, c), grid, size) for r in range(num_r) for c in range(num_c)]
    # for clause in clauses:
    #     print(clause)
    return clauses

# Function to print the clauses
def print_clauses(clauses):
    for clause in clauses:
        print(clause)

# Function to generate the solution from the satisfying assignment of the SAT problem
def generate_solution(size, grid):
    result = output(solve_by_pysat(grid,size), grid,size)
    # for row in result:
    #     print(row)
    return result

# Function to write the output to the output txt file
def write_output(output_file, result):
    # If the result is None, write 'UNSAT' to the output file
    if result is None:
        with open(output_file, 'w') as f:
            f.write('UNSAT')
    else: # Otherwise, write the result to the output file
        with open(output_file, 'w') as f:
            for row in result:
                row = [str(x) for x in row]
                f.write(','.join(row) + '\n')

# Main function
def main():
    text_case_number = len([name for name in os.listdir('inputs') if os.path.isfile(os.path.join('inputs', name))])
    
    for i in range(1, text_case_number + 1):
        input_file = "inputs/input" + str(i) + ".txt"
        output_file = "outputs/output" + str(i) + ".txt"
        
        size, grid = read_input(input_file)
        
        # clause = generate_clauses(size, grid)
        # print_clauses(clause)
        # print('-'*40)
        
        solution = generate_solution(size, grid)
        write_output(output_file, solution)
        
    print(f"All {text_case_number} testcases are solved!")
    

if __name__ == '__main__':
    main()