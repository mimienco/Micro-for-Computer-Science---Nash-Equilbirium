import numpy as np

#A function to print the matrix of a single player
def print_matrix(matrix):
    n = matrix.shape[0]
    for i in range(n):
        for j in range(n):
            print(f"{matrix[i, j]}", end="\t")
        print()

# A function to print the combined payoff matrix
def print_matrices(A, B):
    n = A.shape[0]
    print("\t\tPlayer 2")
    print("\t", end="")
    for j in range(n):
        print(f"\ts{j+1}", end="")
    print()
    for i in range(n):
        print(f"Player 1 s{i+1}", end="")
        for j in range(n):
            print(f"\t{A[i, j]},{B[i, j]}", end="")
        print()

# A function to find Nash Equilibria from the payoff matrix
def NashEquilibrium(A, B):
    n = A.shape[0]
    max_value_in_cols_A = np.max(A, axis=0)
    max_value_in_rows_B = np.max(B, axis=1)
    equilibria = []

    for i in range(n):
        for j in range(n):
            if A[i, j] == max_value_in_cols_A[j] and B[i, j] == max_value_in_rows_B[i]:
                equilibria.append((i + 1, j + 1))  

    return equilibria

# Variable to change the matrix size
n = 4  

# Generate and fill in the payoff matrices for Player 1 (A) and Player 2 (B) with integer values between 1 and 10
np.random.seed(41) 
A = np.random.randint(1, 11, size=(n, n))  
B = np.random.randint(1, 11, size=(n, n))

#Print the single matrices
print("\nMatrix A:")
print_matrix(A)
print("\nMatrix B:")
print_matrix(B)

# Print the results in the terminal
print("\nCombined Payoff Matrices for Player 1 and Player 2:")
print_matrices(A, B)

# Decide if there is a Nash Equilibrium and print it else print that there is no pure strategy equilibrium
equilibria = NashEquilibrium(A, B)
if equilibria:
    print("\nNash Equilibria:")
    for eq in equilibria:
        print(f"The action profile {eq} is a Nash equilibrium.")
        print(f"\nThat means: Player 1 plays s{eq[0]} and Player 2 plays s{eq[1]}.")
else:
    print("Unfortunately, no pure strategy equilibrium exists.")
