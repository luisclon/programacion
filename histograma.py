import matplotlib.pyplot as plt
import json


archivo = open('histograms.txt','r')

contenido = archivo.read()
#print contenido
histograma = json.loads(contenido)
v_error = histograma["histograms"]["v_error"]
t_error = histograma["histograms"]["t_error"]
print histograma['histograms']['v_error']['ys']
