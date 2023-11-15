import os
import numpy as np
import matplotlib.pyplot as plt

# Fonction longueur de mélange

def u_moy_long_mel(u_et,l_et,y,h,Re_et):
    return u_et*(((np.log(y/h)+np.log(Re_et))/kappa) +5)

def visco_turb_mel(y, du_dy):
    return kappa*kappa*y*y*du_dy

def du_dy_mel(y):
    return np.sqrt(tau0)/(kappa*y)

def uxuy(y,du_dy):
    return -kappa*kappa*y*y*du_dy

# Variables

kappa = 0.384
l_et = 1.92*10**(-5)
u_et = 0.78
tau0 = 0.75 
nu = 15*10**(-6)

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
#plt.figure(1)
#plt.plot(mag_vel_fluent,y_vel_fluent, label="Fluent "+r"$K-\epsilon$")
#plt.plot(mag_vel_star,y_vel_star, label="Star-CCM+ "+r"$K-\epsilon$")
#plt.plot(u_effectif,y_effectif,label="DNS")
#plt.ylabel("y (m)")
#plt.xlabel("Vitesse (m/s)")
#plt.legend()

# avec yplus

#plt.figure(3)
#plt.subplot(121)
#plt.plot(mag_vel_fluent,[k/l_et for k in y_vel_fluent], label="Fluent "+r"$K-\epsilon$")
#plt.plot(mag_vel_star,[k/l_et for k in y_vel_star], label="Star-CCM+ "+r"$K-\epsilon$")
#plt.plot(u_effectif,yplus,label="DNS")
#plt.plot([u_moy_long_mel(u_et,l_et,y,0.1,5200) for y in y_effectif],yplus,label="Longueur de mélange")
#plt.ylabel("y+")
#plt.xlabel("Vitesse (m/s)")
#plt.legend()
#plt.subplot(122)
#plt.plot(mag_vel_fluent,[k/l_et for k in y_vel_fluent], label="Fluent "+r"$K-\epsilon$")
#plt.plot(mag_vel_star,[k/l_et for k in y_vel_star], label="Star-CCM+ "+r"$K-\epsilon$")
#plt.plot(u_effectif,yplus,label="DNS")
#plt.plot([u_moy_long_mel(u_et,l_et,y,0.1,5200) for y in y_effectif],yplus,label="Longueur de mélange")
#plt.ylabel("y+")
#plt.xlabel("Vitesse (m/s)")
#plt.legend()
#plt.yscale('log')
#plt.grid(which='both')

# Profils avec y+ et u+

#plt.figure(6)
#plt.subplot(121)
#plt.plot([k/u_et for k in mag_vel_fluent],[k/l_et for k in y_vel_fluent], label="Fluent "+r"$K-\epsilon$")
#plt.plot([k/u_et for k in mag_vel_star],[k/l_et for k in y_vel_star], label="Star-CCM+ "+r"$K-\epsilon$")
#plt.plot([k/u_et for k in U],yplus,label="DNS")
#plt.plot([k/u_et for k in [u_moy_long_mel(u_et,l_et,y,0.1,5200) for y in y_effectif]],yplus,label="Longueur de mélange")
#plt.ylabel("y+")
#plt.xlabel("u+")
#plt.legend()
#plt.subplot(122)
#plt.plot([k/u_et for k in mag_vel_fluent],[k/l_et for k in y_vel_fluent], label="Fluent "+r"$K-\epsilon$")
#plt.plot([k/u_et for k in mag_vel_star],[k/l_et for k in y_vel_star], label="Star-CCM+ "+r"$K-\epsilon$")
#plt.plot(U,yplus,label="DNS")
#plt.plot([k/u_et for k in [u_moy_long_mel(u_et,l_et,y,0.1,5200) for y in y_effectif]],yplus,label="Longueur de mélange")
#plt.ylabel("y+")
#plt.xlabel("u+")
#plt.legend()
#plt.yscale('log')
#plt.grid(which='both')

# Etablissment de la vitesse

x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12 = read_csv("section_velocity(1).csv", 12)
#plt.figure(2)
#plt.plot(x1,x2,'o', label="x=0m")
#plt.plot(x3,x4,'o', label="x=4m")
#plt.plot(x5,x6,'o', label="x=6m")
#plt.plot(x7,x8,'o', label="x=7m")
#plt.plot(x11,x12,'o', label="x=7.5m")
#plt.plot(x9,x10,'o', label="x=8m")
#plt.ylabel("y (m)") 
#plt.xlabel("Vitesse (m/s)")
#plt.legend()


# Energie cinétique turbulente

mag_k_fluent,y_k_fluent = read_xy("nrj_cin_turb.xy")
mag_k_star,y_k_star = read_csv("turbulent_kinetic_energy.csv", 2)

# Energie cinétique turbulente vec y+

y_plus_k_fluent = [y/(1.92*10**(-5)) for y in y_k_fluent]
y_plus_k_star = [y/(1.92*10**(-5)) for y in y_k_star]

#plt.figure(4)
#plt.plot(mag_k_fluent,y_plus_k_fluent, label="Fluent")
#plt.plot(mag_k_star,y_plus_k_star, label="Star-CCM+")
#plt.plot([0.5*k for k in uu],yplus,label="DNS")
#plt.ylabel("y+")
#plt.xlabel("Energie cinétique turbulente (m²/s²)")
#plt.legend()

# Ylog
#plt.figure(5)
#plt.plot(mag_k_fluent,y_plus_k_fluent, label="Fluent")
#plt.plot(mag_k_star,y_plus_k_star, label="Star-CCM+")
#plt.plot([0.5*k for k in uu],yplus,label="DNS")
#plt.ylabel("y+")
#plt.xlabel("Energie cinétique turbulente (m²/s²)")
#plt.legend()
#plt.yscale('log')
#plt.grid(which='both')

# Viscosité turbulente 
uxuymel = [-(kappa*kappa*y*y*du_dy_mel(y)) for y in yplus]
dudymel = [du_dy_mel(y) for y in yplus]

visco_k_fluent,y_k_fluent = read_xy("visc_turb.xy")
visco_k_star,y_k_star = read_csv("turbulent_viscosity.csv", 2)


plt.figure(10)
plt.plot([k/nu for k in visco_k_fluent],y_plus_k_fluent, label="Fluent "+r"$K-\epsilon$")
plt.plot([k/nu for k in visco_k_star],y_plus_k_star, label="Star-CCM+ "+r"$K-\epsilon$")
plt.plot([kappa*y/l_et for y in y_effectif],yplus,label="Longueur de mélange")
plt.legend()
plt.ylabel("y+")
plt.xlabel("Viscosité turbulente (m²/s)")
plt.loglog()
plt.grid(which='both')


# Dissipation et production d'énergie cinétique turbulente

dissip_k_fluent,y_k_fluent = read_xy("taux_dissipation.xy")
dissip_k_star,y_k_star = read_csv("turbulent_dissipation_rate.csv", 2)

prod_k_fluent,y_k_fluent = read_xy("taux_production.xy")

# Production

plt.figure(6)
plt.plot(prod_k_fluent,y_plus_k_fluent, label="Fluent "+r"$K-\epsilon$")
plt.plot([k*l_et/(u_et*u_et) for k in prod],yplus,label="DNS")
plt.plot([uxuymel[k]*dudymel[k] for k in range(len(uxuymel))],yplus,label="Longueur de mélange")
plt.ylabel("y+")
plt.xlabel("Production")
plt.loglog()
plt.legend()

# Energie cinétique turbulente avec y+

y_plus_k_fluent = [y/(1.92*10**(-5)) for y in y_k_fluent]
y_plus_k_star = [y/(1.92*10**(-5)) for y in y_k_star]

#plt.figure(7)
#plt.plot(visco_k_fluent,y_plus_k_fluent, label="Fluent "+r"$K-\epsilon$")
#plt.plot(visco_k_star,y_plus_k_star, label="Star-CCM+ "+r"$K-\epsilon$")
#plt.plot(visc_dissip,yplus,label="DNS")
#plt.ylabel("y+")
#plt.xlabel("Viscosité turbulente (m²/s)")
#plt.legend()

plt.show()