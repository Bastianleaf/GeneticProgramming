import copy


class Tree:

	def __init__(self, value, left, right):
		self.value = value
		self.left = left
		self.right = right
		
	def __str__(self):
		"""
		Reescribe print para arboles
		:return: string del arbol
		"""
		info = str(self.value)
		if self.left is None:
			left = ""
		else:
			left = self.left
		if self.right is None:
			right = ""
		else:
			right = self.right
		if left == "" and right == "":
			return info
		else:
			return "(" + left.__str__() + info + right.__str__() + ")"

	def evaluate(self):
		"""
		Retorna la evaluacion del arbol
		:return: resultado de la evaluacion del abrol
		"""
		if self.value == "+":
			return self.left.evaluate() + self.right.evaluate()
		elif self.value == "-":
			return self.left.evaluate() - self.right.evaluate()
		elif self.value == "*":
			return self.left.evaluate() * self.right.evaluate()
		elif self.value == "/":
			try:
				sol = self.left.evaluate() / self.right.evaluate()
			except ZeroDivisionError:
				sol = 0
			return sol
		else:
			return self.value

	def get_depth(self, count=0):
		if self.right is None and self.left is None:
			return count + 1
		else:
			return max(self.left.get_depth(count + 1), self.right.get_depth(count + 1))
		
	def copy_tree(self):
		return copy.deepcopy(self)

