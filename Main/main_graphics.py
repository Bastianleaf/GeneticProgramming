from time import time
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

#arreglos de medicion
data_score = []
data_generations = []
data_time = []

outputs_array = range(50, 500, 50)

for n in outputs_array:
	tamano_poblacion = n
	limite_generacional = 20
	cromosomas = []
	for i in range(tamano_poblacion):
		cromosomas.append(TreeChromosome(fabrica_de_arboles.create_random_tree()))
	poblacion = TreePopulation(cromosomas, terminales, funciones, limite_generacional, solucion)

	# Algoritmo Principal
	start_time = time()
	while not poblacion.optimal:
		poblacion.evolution()
	elapsed_time = time() - start_time
	
	# Impresion de informacion
	print("##################  " + str(n) + "  ##################")
	print("Generacion: " + str(poblacion.generation))
	optimal = poblacion.get_best()
	print("Ecuacion optima: " + str(optimal.value))
	print("Solucion de ecuacion: " + str(optimal.value.evaluate()))
	print("Tiempo demorado: %.10f segundos." % elapsed_time)
	data_score.append(round(optimal.score, 2))
	data_time.append(elapsed_time)
	data_generations.append(poblacion.generation)
	
plt.subplot(3, 1, 1)
plt.grid(True)
#plt.axis([3, max(outputs_array) + 1, min(data_score) , max(data_score) ])
plt.plot(outputs_array, data_score)
plt.title('Búsqueda de Número según Tamaño de Población')
plt.ylabel('Diferencia [sol]')
plt.subplot(3, 1, 2)
plt.grid(True)
plt.plot(outputs_array, data_generations)
plt.ylabel('Generaciones')
plt.subplot(3, 1, 3)
plt.grid(True)
plt.plot(outputs_array, data_time)
plt.ylabel('Tiempo[s]')
plt.xlabel('Tamaño de Población')
plt.show()


