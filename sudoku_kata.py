import numpy as np

class Sudoku():
	#The code goes here
	def __init__(self, list_of_lists):
		self.list_of_lists = list_of_lists
		#self.list_of_lists = np.array(self.list_of_lists)

	def kontrola_suctu(self):
		self.list_of_lists = np.array(self.list_of_lists)
		sucet1 = self.list_of_lists.sum(axis=0)
		sucet2 = self .list_of_lists.sum(axis=1)
		zhoda = sucet1 == sucet2

		print(sucet1)
		print(sucet2)
		print(zhoda)

		if False in zhoda:
			return False
		else:
			return True

	def jedinecne(self):


'''
	def is_valid(self):
		matica = self.object
'''

goodSudoku = Sudoku([[1, 2, 3], [2, 1, 3], [1, 1, 2]])
print(goodSudoku.kontrola_suctu())