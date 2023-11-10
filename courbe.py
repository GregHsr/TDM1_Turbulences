import os
import numpy as np
import matplotlib.pyplot as plt

### Lecture des fichiers csv et xy

def read_xy(filename):
    data = open(filename, 'r')
    x = []
    y = []
    for line in data:
        line = line.split()
        if line[0][0] != "(" and line[0][0] != ")":
            x.append(float(line[0]))
            y.append(float(line[1]))
    return x, y

def read_csv(filename, nb_colonne):
    if nb_colonne == 2:
        data = open(filename, 'r')
        x = []
        y = []
        for line in data:
            line = line.split(",")
            if line[0][0] != "%" and line[0][0] != str('"'):
                x.append(float(line[0]))
                y.append(float(line[1]))
        return x, y
    if nb_colonne == 12:
        data = open(filename, 'r')
        x1 = []
        x2 = []
        x3 = []
        x4 = []
        x5 = []
        x6 = []
        x7 = []
        x8 = []
        x9 = []
        x10 = []
        x11 = []
        x12 = []
        for line in data:
            line = line.split(",")
            if line[0][0] != str('"'):
                if line[0] != "null":
                    x1.append(float(line[0]))
                    x2.append(float(line[1]))
                    x3.append(float(line[2]))
                    x4.append(float(line[3]))
                    x5.append(float(line[4]))
                    x6.append(float(line[5]))
                    x7.append(float(line[6]))
                    x8.append(float(line[7]))
                x9.append(float(line[8]))
                x10.append(float(line[9]))
                if line[0] != "null":
                    x11.append(float(line[10]))
                    x12.append(float(line[11]))
        return x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12

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

y_effectif = [y*1.92*10**(-5) for y in yplus]
u_effectif = [u_fichier*0.78 for u_fichier in U]

### Courbes

# Vitesse section sortie

mag_vel_fluent,y_vel_fluent = read_xy("vitesse_moyenne.xy")
mag_vel_star,y_vel_star = read_csv("ux.csv", 2) 
plt.figure(1)
plt.plot(mag_vel_fluent,y_vel_fluent, label="Fluent")
plt.plot(mag_vel_star,y_vel_star, label="Star-CCM+")
plt.plot(U,y_effectif,label="DNS")
plt.ylabel("y (m)")
plt.xlabel("Vitesse (m/s)")
plt.legend()

# Etablissment de la vitesse

x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12 = read_csv("section_velocity(1).csv", 12)
plt.figure(2)
plt.plot(x1,x2,'o', label="x=0m")
plt.plot(x3,x4,'o', label="x=4m")
plt.plot(x5,x6,'o', label="x=6m")
plt.plot(x7,x8,'o', label="x=7m")
plt.plot(x11,x12,'o', label="x=7.5m")
plt.plot(x9,x10,'o', label="x=8m")
plt.ylabel("y (m)") 
plt.xlabel("Vitesse (m/s)")
plt.legend()


# Energie cinétique turbulente

mag_k_fluent,y_k_fluent = read_xy("nrj_cin_turb.xy")
mag_k_star,y_k_star = read_csv("turbulent_kinetic_energy.csv", 2)
plt.figure(3)
plt.plot(mag_k_fluent,y_k_fluent, label="Fluent")
plt.plot(mag_k_star,y_k_star, label="Star-CCM+")
plt.plot(k,y_effectif,label="DNS")
plt.ylabel("y (m)")
plt.xlabel("Energie cinétique turbulente (m²/s²)")
plt.legend()


plt.show()