# Eigenvectors and eigenvalues

import numpy as np

A = np.array([[7, -15], [2, -4]])
print(f"Eigenvalues and eigenvectors for square matrix A: \n{np.linalg.eig(A)}")
print(f"Eigenvalues only: \n{np.linalg.eigvals(A)}")

# SciPy has similar syntax
