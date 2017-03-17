#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Veli Cihan Gökkaya"
__copyright__ = "Copyright 2007, AGH University of Science and Technology"

class Matrix:

	def __init__(self,*args):
		self.m = (args)

	def __repr__(self):
		return str(self.m)

	def __getitem__(self,(i)):
		return self.m[i]

	def add(self,matrix):
		sum = ()
		for i,item in enumerate(self):
			sum = sum + ((item + matrix[i]),)
		return sum
