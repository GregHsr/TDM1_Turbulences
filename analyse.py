import os
import numpy as np
import matplotlib.pyplot as plt

# Fonction 

def integ_rectangle(x,y):
    integ = 0
    for i in range(len(x)-1):
        integ += (x[i+1]-x[i])*y[i]
    return integ

# Liste données

ydelta = []
yplus = []
U = []
dudy = []
W = []
P = []
uu = []
vv = []
ww = []
uv = []
uw = []
vw = []
k = []
prod = []
turb_trans = []
vis_trans = []
pressure_strain = []
pressure_trans  = []
visc_dissip = []
balance = []

# Lire les données

data = open("LM_Channel_5200_prof.txt", 'r')

for line in data:
    line = line.split()
    if line[0][0] != "%":
        ydelta.append(float(line[0]))
        yplus.append(float(line[1]))
        U.append(float(line[2]))
        dudy.append(float(line[3]))
        W.append(float(line[4]))
        P.append(float(line[5]))
        uu.append(float(line[6]))
        vv.append(float(line[7]))
        ww.append(float(line[8]))
        uv.append(float(line[9]))
        uw.append(float(line[10]))
        vw.append(float(line[11]))
        k.append(float(line[12]))
        prod.append(float(line[13]))
        turb_trans.append(float(line[14]))
        pressure_strain.append(float(line[15]))
        pressure_trans.append(float(line[16]))
        visc_dissip.append(float(line[17]))
        balance.append(float(line[18]))

data.close()

# Calculs

# Vitesse débitante
Ud = integ_rectangle(yplus,U)/yplus[-1]
print(Ud)

Um = Ud * 0.78

Re_d = Um * 0.1 / 1.5e-5
print(Re_d)

plt.figure(1)
plt.plot(ydelta, U, label = "U")

plt.show()

