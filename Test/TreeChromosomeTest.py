import unittest
from Tree.Tree import Tree
from GeneticAlgorithm.TreeChromosome import TreeChromosome


class TreeChromosomeTest(unittest.TestCase):
	def setUp(self):
		tree_1 = Tree(1, None, None)
		tree_2 = Tree(2, None, None)
		tree_3 = Tree(3, None, None)
		tree_4 = Tree(4, None, None)
		
		"arbol -> (((4 + 2) - (3 * 1)) / 3"
		tree_plus = Tree("+", tree_4, tree_2)
		tree_mul = Tree("*", tree_3, tree_1)
		tree_minus = Tree("-", tree_plus, tree_mul)
		tree_test = Tree("/", tree_minus, tree_3)
		self.tree_chromosome_test = TreeChromosome(tree_test)
	
	def test_evaluate_fitness(self):
		self.tree_chromosome_test.evaluate_fitness(1)
		self.assertEqual(self.tree_chromosome_test.score, 0)
		self.tree_chromosome_test.evaluate_fitness(2)
		self.assertEqual(self.tree_chromosome_test.score, 1)


if __name__ == '__main__':
	unittest.main()
