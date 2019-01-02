import unittest
from Tree.Tree import Tree


class TreeTest(unittest.TestCase):
	def setUp(self):
		tree_a = Tree(1, None, None)
		tree_b = Tree(2, None, None)
		self.tree_a = tree_a
		self.tree_c = Tree("+", tree_a, tree_b)
		self.tree_plus = Tree("+", tree_a, tree_b)
		self.tree_minus = Tree("-", tree_a, tree_b)
		self.tree_mul = Tree("*", tree_a, tree_b)
		self.tree_div = Tree("/", tree_a, tree_b)

		
		
		
	def test_print(self):
		"""
		Prueba que la impresion del arbol sea correcta
		"""
		self.assertEqual("(1+2)", self.tree_c.__str__())
	
	def test_evaluate(self):
		"""
		Prueba la evaluacion del arbol para las cuatro operaciones
		"""
		self.assertEqual(3, self.tree_plus.evaluate())
		self.assertEqual(-1, self.tree_minus.evaluate())
		self.assertEqual(2, self.tree_mul.evaluate())
		self.assertEqual(0.5, self.tree_div.evaluate())
		
	def test_get_depth(self):
		self.assertEqual(2, self.tree_c.get_depth())
		self.assertEqual(1, self.tree_a.get_depth())

	

if __name__ == '__main__':
	unittest.main()
