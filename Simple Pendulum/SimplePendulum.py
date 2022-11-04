# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 21:17:16 2022

@author: mario
"""

"""
Simulation of Simple pendulum
"""

import numpy as np 
from scipy.integrate import odeint
from matplotlib import pyplot as plt 
import os

"""
Ecuacion diferencial

d2Theta/dt2 + (g/L)*senTheta = 0

Reescribir en dos ecuaciones lineales de primer orden

dTheta/dt = omega 

domega/dt = -(g/L)senTheta

"""


def ecuacionPenduloSimple(y,t):
    theta, omega = y
    
    return [omega, (-g/L)*np.sin(theta)]  # [dtheta/dt, domega/dt]
    
    

#Parametros
g = 9.81
L = 0.5

#Condiciones iniciales
angulo_inicial = 45                 #angulo incial
theta0 = np.radians(angulo_inicial) #grados a radianes
omega0 = 0                          #velocidad inicial

y0 = (theta0, omega0)         

t0 = 0            #tiempo inicial
tf = 10           #tiempo final 
saltos = tf*25    #cantidad de pasos, 25 constante para buena visualizacion


t = np.linspace(t0,tf, saltos)

solucion = odeint(ecuacionPenduloSimple,y0,t)

theta, omega = solucion.T

plt.plot(t, theta, label = "Desplazamiento angular (rad)")
plt.plot(t, omega, label = "Velocidad angular (rad/s)")
plt.title("Pendulo Simple")
plt.xlabel("Tiempo (s)")
plt.ylabel("Desp. Angular (rad) y Vel. Angular (rad/s)")
plt.legend()
plt.show()

#plt.plot(t, theta,"ro", label = "Desplazamiento angular (rad)")

#Simulación
puntos_simulacion = len(t)
l_simulacion =np.arange(0,puntos_simulacion,1)

x_posicion = L*np.sin(theta)
y_posicion = -L*np.cos(theta)


for punto in l_simulacion:
    plt.figure()
    plt.plot(x_posicion[punto],y_posicion[punto],'ro',markersize = 10) #Dibuja pendulo
    plt.plot([0,x_posicion[punto]],[0,y_posicion[punto]])              #Dibuja cadena del pendulo
    plt.xlim(-L-0.5,L+0.5)                                             #Limite de X
    plt.ylim(-L-0.5,L+0.5)                                             #Limite de Y
    plt.xlabel('Direccion X')
    plt.ylabel('Direccion Y')
    filenumber = punto
    filenumber = format(filenumber,"05")
    filename="image{}.png".format(filenumber)
    plt.savefig(filename)
    plt.close()

os.system("ffmpeg -f image2 -r 20 -i image%05d.png -vcodec mpeg4 -y movie.avi")