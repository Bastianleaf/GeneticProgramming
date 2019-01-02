from Tree.Tree import Tree
import random


class TreeFactory:
	
	def __init__(self, functions, terminals, depth):
		self.functions = functions
		self.terminals = terminals
		self.max_depth = depth
	
	def select_random_terminal(self):
		return select_random_element(self.terminals)

	def select_random_function(self):
		return select_random_element(self.functions)
	
	def create_random_tree(self, depth=0):
		selector = random.randint(0, 1)
		if (selector == 0 or depth == self.max_depth) and depth > 1:
			return Tree(self.select_random_terminal(), None, None)
		else:
			return Tree(self.select_random_function(), self.create_random_tree(depth + 1), self.create_random_tree(depth + 1))


def select_random_element(elements_list):
	return random.choice(elements_list)

