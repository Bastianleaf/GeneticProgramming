from time import time
import numpy
import matplotlib.pyplot as plt
from Tree.TreeFactory import TreeFactory
from GeneticAlgorithm import TreeChromosome
from GeneticAlgorithm import TreePopulation

#variables globales

terminales = [1, 2, 3, 4]
funciones = ["+", "-", "*", "/"]
profundidad = 5
solucion = 140
fabrica_de_arboles = TreeFactory(funciones, terminales, profundidad)
tamano_poblacion = 400
limite_generacional = 5
cromosomas = []
for i in range(tamano_poblacion):
	cromosomas.append(TreeChromosome(fabrica_de_arboles.create_random_tree()))
poblacion = TreePopulation(cromosomas, terminales, funciones, limite_generacional, solucion)
start_time = time()
count = 0
data_x = []
data_y = []
while not poblacion.optimal:
	poblacion.evolution()
	data_x.append(count)
	data_y.append(numpy.mean(list(map(lambda x: x.score, poblacion.population))))
	
	count += 1
elapsed_time = time() - start_time
print(data_y)

plt.grid(True)
plt.plot(data_x, data_y)
plt.title('Puntaje según generación. ')
plt.xlabel("Generacion de la poblacion")
plt.show()