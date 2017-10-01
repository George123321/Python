from Class_Numeric import Numeric
from Class_Matrix import Matrix
from Class_Matrix import Identity_Matrix

A = Matrix(3)
A.write_matrix()
A.invert_matrix().print()
B = A.clip(Identity_Matrix(A.n))
B.gauss()
B.print()