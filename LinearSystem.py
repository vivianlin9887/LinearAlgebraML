# Solving linear systems Ax = B

import numpy as np

# Example:
# 4x + 3y + 2z = 25
# -2x + 2y + 3z = -10
# 3x -5y + 2z = -4

A = np.array([[4, 3, 2], [-2, 2, 3], [3, -5, 2]])
B = np.array([25, -10, -4])
X = np.linalg.inv(A).dot(B)
Y = np.linalg.solve(A, B)
print(f"X = {X}, so x = {X[0]}, y = {X[1]}, z = {X[2]}")
print(f"X = {Y}, so x = {Y[0]}, y = {Y[1]}, z = {Y[2]}")
