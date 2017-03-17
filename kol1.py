#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Veli Cihan Gökkaya"
__copyright__ = "Copyright 2007, AGH University of Science and Technology"

from my_matrix import Matrix

matrix_1 = Matrix(4,5,6,7)
matrix_2 = Matrix(2,2,2,1)

matrix_3 = matrix_2.add(matrix_1)

print matrix_3
