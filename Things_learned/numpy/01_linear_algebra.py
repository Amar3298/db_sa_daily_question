"""
linalg.det
The linalg.det tool computes the determinant of an array.
"""
import numpy
print(numpy.linalg.det([[1 , 2], [2, 1]]))
"""
linalg.eig

The linalg.eig computes the eigenvalues and right eigenvectors of a square array.
"""
import numpy
vals, vecs = numpy.linalg.eig([[1 , 2], [2, 1]])
print(vals)
print(vecs)
"""
linalg.inv

The linalg.inv tool computes the (multiplicative) inverse of a matrix.
"""
import numpy
print(numpy.linalg.inv([[1 , 2], [2, 1]]))