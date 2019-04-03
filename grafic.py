import matplotlib.pyplot as plt
from matplotlib import pyplot
import json


archivo = open('histograms.txt','r')

contenido = archivo.read()
#print contenido
histograma = json.loads(contenido)
v_error = histograma["histograms"]["v_error"]
t_error = histograma["histograms"]["t_error"]
print histograma['histograms']['v_error']['ys']

plt.plot(v_error['xs'],v_error['ys'])
plt.plot(t_error['xs'],t_error['ys'])

pyplot.title('Reprecentacion de Histograma de Errores')
plt.xlabel('Iteraciones')
plt.ylabel('Valor del error')
plt.legend(['Error de validacio','Error de Entrenamiento'])
plt.show()
