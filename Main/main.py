from Tree.TreeFactory import TreeFactory
from GeneticAlgorithm import TreeChromosome
from GeneticAlgorithm import TreePopulation

#variables globales

terminales = [1, 2, 3, 4, 5]
funciones = ["+", "-", "*", "/"]
profundidad = 5
tamano_poblacion = 700
solucion = 140
limite_generacional = 20
fabrica_de_arboles = TreeFactory(funciones, terminales, profundidad)
cromosomas = []
for i in range(tamano_poblacion):
	cromosomas.append(TreeChromosome(fabrica_de_arboles.create_random_tree()))
poblacion = TreePopulation(cromosomas, terminales, funciones, limite_generacional, solucion)
poblacion.evolution()

#solucion
print("Terminales : " + str(terminales))
print("Funciones : " + str(funciones))
print("Ecuación: " + str(poblacion.get_best().value))
print("Solución encontrada: " + str(poblacion.get_best().value.evaluate()))