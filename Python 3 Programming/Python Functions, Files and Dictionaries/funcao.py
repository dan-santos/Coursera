from random import random
import matplotlib.pyplot as plt

cX = list()
cY = list()

def funcaoQ(axisX):
    cX.append(axisX)
    axisY = pow(axisX, 2)
    cY.append(axisY)


while True:
    valor = random()
    if f'{valor:.2f}' != '0.00':
        funcaoQ(valor)
    else:
        break

plt.plot(cX, cY)
plt.savefig('grafico.png')
