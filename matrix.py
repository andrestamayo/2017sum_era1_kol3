#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Matrix:

	def __init__(self,*args):
		self.m = []
		for argi in args:
			self.m.extend(argi)
		self.index = 0

	def __repr__(self):
		if not isinstance(self.m,list):
			return str(self.m)
		else:
			out = "\n"
			for i,it in enumerate(self.m):
				out += "|"
				for j,jt in enumerate(self.m[i]):
					out += " " + str(self.m[i][j]) + " "
				out += "|\n"
			return out

	def __add__(self,matrix):
		self.sum = Matrix()
		self.group = []
		if isinstance(matrix, int):
			if not isinstance(self.m,list):
				for i,it in enumerate(self.m):
					self.sum.m.append(it + matrix)
				return self.sum
			else:
				for i,it in enumerate(self.m):
					for j,jt in enumerate(self.m[i]):
						self.group.append(jt + matrix)
					self.sum.m.append(self.group)
					self.group = []
				return self.sum
		elif len(self.m) == len(matrix.m):
			if not isinstance(self.m,list):
				for i,it in enumerate(self.m):
					self.sum.m.append(it + matrix.m[i])
				return self.sum
			else:
				for i,it in enumerate(self.m):
					for j,jt in enumerate(self.m[i]):
						self.group.append(jt + matrix.m[i][j])
					self.sum.m.append(self.group)
					self.group = []
				return self.sum

	def __radd__(self,matrix):
		self.sum = Matrix()
		self.group = []
		if isinstance(matrix, int):
			if not isinstance(self.m,list):
				for i,it in enumerate(self.m):
					self.sum.m.append(it + matrix)
				return self.sum
			else:
				for i,it in enumerate(self.m):
					for j,jt in enumerate(self.m[i]):
						self.group.append(jt + matrix)
					self.sum.m.append(self.group)
					self.group = []
				return self.sum

	def __sub__(self,matrix):
		self.sum = Matrix()
		self.group = []
		if isinstance(matrix, int):
			if not isinstance(self.m,list):
				for i,it in enumerate(self.m):
					self.sum.m.append(it - matrix)
				return self.sum
			else:
				for i,it in enumerate(self.m):
					for j,jt in enumerate(self.m[i]):
						self.group.append(jt - matrix)
					self.sum.m.append(self.group)
					self.group = []
				return self.sum
		elif len(self.m) == len(matrix.m):
			if not isinstance(self.m,list):
				for i,it in enumerate(self.m):
					self.sum.m.append(it - matrix.m[i])
				return self.sum
			else:
				for i,it in enumerate(self.m):
					for j,jt in enumerate(self.m[i]):
						self.group.append(jt - matrix.m[i][j])
					self.sum.m.append(self.group)
					self.group = []
				return self.sum

	def __rsub__(self,matrix):
		self.sum = Matrix()
		self.group = []
		if isinstance(matrix, int):
			if not isinstance(self.m,list):
				for i,it in enumerate(self.m):
					self.sum.m.append(matrix - it)
				return self.sum
			else:
				for i,it in enumerate(self.m):
					for j,jt in enumerate(self.m[i]):
						self.group.append(matrix - jt)
					self.sum.m.append(self.group)
					self.group = []
				return self.sum

	def prod(self,matrix):
		row_self = len(self.m)
		col_self = len(self.m[0])
		row_matrix = len(matrix.m)
		col_matrix = len(matrix.m[0])
		if col_self != row_matrix:
			print "Error"
			return
		self.sum = Matrix([[0 for row in range(col_matrix)] for col in range(row_self)])
		for i in range(row_self):
			for j in range(col_matrix):
				for k in range(col_self):
					self.sum.m[i][j] += self.m[i][k] * matrix.m[k][j]
		return self.sum

	def __iter__(self):
		return self

	def next(self):
		if self.index >= len(self.m):
			raise StopIteration
		else:
			self.index += 1
			return self.m[self.index - 1]
