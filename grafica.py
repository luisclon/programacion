from matplotlib import pyplot

lenguajes = ('Python','c','Java','Go','Js')
slices = (100, 130, 90, 80, 128)
colores = ('red','blue','green','#DD98AA','#18492D')
valores = (0.1, 0, 0, 0, 0)

pyplot.rcParams['tolbar' = 'None']

_,_, texto = pyplot.pie(slices, colors=colores, labels=lenguajes, autopct='%1.1f%%',
						explode=valores,
						startangle=90)

for tex i n texto:
	tex.set_color('white')

pyplot.axis('equal')
pyplot.title('grafica de lenguajes de programacion')
#pyplot.legend(labels=lenguajes)
#pyplot.show()
pyplot.savefig('lenguajes.png')
 
