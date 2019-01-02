from Tree.TreeFactory import TreeFactory
from GeneticAlgorithm import TreeChromosome
from GeneticAlgorithm import TreePopulation

#variables globales

terminales = [1, 2, 3, 4, 3]
funciones = ["+", "-", "*", "/"]
profundidad = 5
tamano_poblacion = 500
solucion = 140
limite_generacional = 5
fabrica_de_arboles = TreeFactory(funciones, terminales, profundidad)
cromosomas = []
for i in range(tamano_poblacion):
	cromosomas.append(TreeChromosome(fabrica_de_arboles.create_random_tree()))
poblacion = TreePopulation(cromosomas, terminales, funciones, limite_generacional, solucion)
poblacion.evolution()

#solucion
print(poblacion.get_best().value)
print("valor: " + str(poblacion.get_best().value.evaluate()))