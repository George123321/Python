from Class_Numeric import Numeric
from Class_Matrix import Matrix

A = Matrix(3)
A.write_matrix()
#A.invert_matrix().print()
A.gauss().print()
A.gauss_trans().gauss().print()

