import random
from Tree.Tree import Tree

class TreeChromosome:
	
	def __init__(self, value):
		self.value = value
		self.mutation_rate = 0.1
		self.score = 0
		
	def evaluate_fitness(self, solution):
		evaluation = self.value.evaluate()
		self.score = max(evaluation, solution) - min(evaluation, solution)
		
	def set_mutation_rate(self, rate):
		"""
		Modifica el ratio de mutacion
		:param rate: nuevo ratio de mutacion
		"""
		self.mutation_rate = rate
	
	def mutation(self):
		if random.uniform(0, 1) < self.mutation_rate:
			index = random.randint(0, len(self.value) - 1)
			self.value[index].mutate()
			self.value = self.value[:index] + [self.value[index]] + self.value[index + 1:]
	
	def reproduction(self, gen, solution, functions):
		self.evaluate_fitness(solution)
		gen.evaluate_fitness(solution)
		best = self
		tree_a_nodes = [self.value.copy_tree(), self.value.left.copy_tree(), self.value.right.copy_tree()]
		tree_b_nodes = [gen.value.copy_tree(), gen.value.left.copy_tree(), gen.value.right.copy_tree()]
		for fun in functions:
			for a_node in tree_a_nodes:
				for b_node in tree_b_nodes:
					new_tree = TreeChromosome(Tree(fun, a_node, b_node))
					new_tree.evaluate_fitness(solution)
					if new_tree.score < best.score:
						best = new_tree
		return best

