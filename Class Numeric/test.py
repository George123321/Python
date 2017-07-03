from Class_Numeric import Numeric
from Class_Matrix import Matrix
from Class_Matrix import Identity_Matrix

A = Matrix(3)
A.write_matrix()
B = A.clip(Identity_Matrix(A.n))
B.print()
print(B.n, B.m)
B.gauss()
B.print()
A.gauss()
A.print()