import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib import colors

manzanas = [20,10,25,30]
nombres = ["Ana","Juan","Diana","Catalina"]

normdata = colors.Normalize(min(manzanas), max(manzanas))
colormap = cm.get_cmap("Blues")
colores =colormap(normdata(manzanas))

plt.pie(manzanas, labels=nombres, autopct="%0.1f %%", colors=colores)
plt.axis("equal")
plt.show()
