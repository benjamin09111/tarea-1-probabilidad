from random import randint
from numpy import random
from matplotlib import pyplot as plt


#iniciar arreglo en 0

resultados = []
for i in range (0,51):
    resultados.append(0)

#aumentar valores segun resultados

j = 0
for j in range (0,10000):
    data = 0

    a = randint(1,6)
    b = randint(1,6)
    c = randint(1,6)
    d = randint(1,6)
    e = randint(1,6)
    f = randint(1,6)
    g = randint(1,6)
    h = randint(1,6)
    i = randint(1,6)
    j = randint(1,6)

    data = a+b+c+d+e+f+g+h+i+j

    if data == 10:
        resultados[0] += 1
    if data == 11:
        resultados[1] += 1
    if data == 12:
        resultados[2] += 1
    if data == 13:
        resultados[3] += 1
    if data == 14:
        resultados[4] += 1
    if data == 15:
        resultados[5] += 1
    if data == 16:
        resultados[6] += 1
    if data == 17:
        resultados[7] += 1
    if data == 18:
        resultados[8] += 1
    if data == 19:
        resultados[9] += 1
    if data == 20:
        resultados[10] += 1
    if data == 21:
        resultados[11] += 1
    if data == 22:
        resultados[12] += 1
    if data == 23:
        resultados[13] += 1
    if data == 24:
        resultados[14] += 1
    if data == 25:
        resultados[15] += 1
    if data == 26:
        resultados[16] += 1
    if data == 27:
        resultados[17] += 1
    if data == 28:
        resultados[18] += 1
    if data == 29:
        resultados[19] += 1
    if data == 30:
        resultados[20] += 1
    if data == 31:
        resultados[21] += 1
    if data == 32:
        resultados[22] += 1
    if data == 33:
        resultados[23] += 1
    if data == 34:
        resultados[24] += 1
    if data == 35:
        resultados[25] += 1
    if data == 36:
        resultados[26] += 1
    if data == 37:
        resultados[27] += 1
    if data == 38:
        resultados[28] += 1
    if data == 39:
        resultados[29] += 1
    if data == 40:
        resultados[30] += 1
    if data == 41:
        resultados[31] += 1
    if data == 42:
        resultados[32] += 1
    if data == 43:
        resultados[33] += 1
    if data == 44:
        resultados[34] += 1
    if data == 45:
        resultados[35] += 1
    if data == 46:
        resultados[36] += 1
    if data == 47:
        resultados[37] += 1
    if data == 48:
        resultados[38] += 1
    if data == 49:
        resultados[39] += 1
    if data == 50:
        resultados[40] += 1
    if data == 51:
        resultados[41] += 1
    if data == 52:
        resultados[42] += 1
    if data == 53:
        resultados[43] += 1
    if data == 54:
        resultados[44] += 1
    if data == 55:
        resultados[45] += 1
    if data == 56:
        resultados[46] += 1
    if data == 57:
        resultados[47] += 1
    if data == 58:
        resultados[48] += 1
    if data == 59:
        resultados[49] += 1
    if data == 60:
        resultados[50] += 1  

#imprimir datos especificos

var = 10

for n in range(0,51):
    print("\n",var," = ",resultados[n])
    var += 1

#realizar grafica 1

x = ["10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30",
    "31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51",
    "52","53","54","55","56","57","58","59","60"]

#plt.bar(x,height=resultados,width=5.0)
#plt.xlabel('Suma de cada número de los 10 dados')
#plt.ylabel('Frecuencia de cada res