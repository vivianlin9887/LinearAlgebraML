# Basic matrix manipulation

import numpy as np
import sympy as sym

A = np.array([[2, 1], [3, 0], [0, 4]])
B = np.array([[1, 2], [-3, 1], [1, 2]])
C = np.array([[3, 0], [1, 5]])
D = np.array([[5, 3], [2, 4]])
E = np.arange(9).reshape(3, 3)


def main():
    print(f"Matrix A is a 3x2 matrix: \n{A}")
    print(f"Matrix B is a 3x2 matrix: \n{B}")
    print(f"Basic operation - Addition: A + B = \n{A+B} or \n{np.add(A, B)}")
    print(f"Basic operation - Multiplication by scalar: B * 2 = \n{2*B} or \n{np.multiply(2, B)}")
    print(f"Basic operation - Dot product: A x C = \n{np.dot(A, C)}")
    print(f"Basic operation - Dot product: A x C = \n{A@C}")
    print("=" * 40)

    print(f"Creating identity matrix 3x3: \n{np.identity(3)}")
    print(f"Transpose of matrix A: \n{A.T}")
    print(f"Inverse of matrix C: \n{np.linalg.inv(C)}")
    print(f"Find the determinant of matrix C: (3*5 - 0*1) = {np.linalg.det(C)}")
    print(f"Properties of Det: det(C.T) = det(C) {np.linalg.det(C.T) == np.linalg.det(C)}")
    print(f"Properties of Det: det(CD) = det(C)det(D) {np.linalg.det(C@D) == np.linalg.det(C) * np.linalg.det(D)}")
    print(f"Properties of Det: det(C+D) != det(C) + det(D) {np.linalg.det(C+D) == np.linalg.det(C) + np.linalg.det(D)}")
    print(f"Properties of Det: det(I) = {np.linalg.det(np.identity(2))}")
    print("=" * 40)

    print(f"Finding RREF of Matrix with Sympy: \n{sym.Matrix(A).rref()}")
    print(f"Get the diagonal values of matrix E: \n{np.diag(E)}")
    print(f"Construct diagonal array from that extracted: \n{np.diag(np.diag(E))}")


if __name__ == '__main__':
    main()
