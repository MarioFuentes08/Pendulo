# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 21:19:23 2022

@author: mario
"""
from tkinter import *
import math
import numpy as np
import scipy
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import os

"""
###################################################################################
FUNCIONES PARA RESOLVER ECUACIONES DIFERENCIALES
###################################################################################
"""
def sim_pen_eq(t,theta_S):
    g_S = float(gravedadS_string.get())        # Acceleration due to gravity (m/s^2)
    L_S = float(largoS_string.get())           # Length of pendulum (m)
    dtheta2_dt_S = + (-g_S/L_S)*np.sin(theta_S[0])
    dtheta1_dt_S = theta_S[1]
       
    return [dtheta1_dt_S, dtheta2_dt_S]   

"""
###################################################################################
FUNCIONES PARA LLAMAR 
###################################################################################
"""
"""
     theta1 is angular displacement at current time instant
     theta2 is angular velocity at current time instant
     dtheta2_dt is angular acceleration at current time instant
     dtheta1_dt is rate of change of angular displacement at current time instant i.e. same as theta2 
"""
def penduloSimple():
    theta1_ini_Simple = float(amplitudS_string.get()) * math.pi / 180     # Initial angular displacement (rad)
    theta2_ini_Simple = 0                                                 # Initial angular velocity (rad/s)
    theta_ini_Simple = [theta1_ini_Simple, theta2_ini_Simple]
    theta12_Simple = solve_ivp(sim_pen_eq, t_span, theta_ini_Simple, t_eval = t)
    theta1_Simple = theta12_Simple.y[0,:]
    theta2_Simple = theta12_Simple.y[1,:]
    plt.plot(t,theta1_Simple,label='Angular Displacement (rad)')
    plt.plot(t,theta2_Simple,label='Angular velocity (rad/s)')
    plt.xlabel('Time(s)')
    plt.ylabel('Angular Disp.(rad) and Angular Vel.(rad/s)')
    plt.legend()
    plt.show()    
    
    
    
    
def penduloAmortiguado():
    pass

def penduloForzadoAmortiguado():
    pass

"""
###################################################################################
VARIABLES GLOBALES PARA LA SIMULACIÓN
###################################################################################
"""
# Initial and end values
st = 0                          # Start time (s)
et = 30                         # End time (s)
ts = 0.1                        # Time step (s)
t_span = [st,et+ts]
t = np.arange(st,et+ts,ts)
sim_points = len(t)
l = np.arange(0,sim_points,1)



"""
###################################################################################
INTERFAZ
###################################################################################
"""

root = Tk()
root.title("El pendulo") #titulo de programa
root.iconbitmap('pendulo.ico') #icono de programa
root.geometry("350x900") #tamaño de la ventana
root.resizable(0,0) #venta no se puede modificar ancho ni largo


""" Pendulo simple variables"""
amplitudS_string = StringVar()
largoS_string = StringVar()
gravedadS_string = StringVar()

""" Pendulo amortiguado variables"""
amplitudA_string = StringVar()
largoA_string = StringVar()
gravedadA_string = StringVar()
amortiguamientoA_string = StringVar()
masaA_string = StringVar()


""" Pendulo forzado amortiguado variables"""
amplitudFA_string = StringVar()
largoFA_string = StringVar()
gravedadFA_string = StringVar()
amortiguamientoFA_string = StringVar()
masaFA_string = StringVar()
amplitudFuerzaFA_string = StringVar()
frecuenciaFA_string = StringVar()


"""PENDULO SIMPLE"""

Label(root, text="Pendulo Simple",font=("Arial",12)).pack()

Label(root, text="Digite al amplitud (°)",font=("Arial",10)).pack()
Entry(root, justify="center",textvariable=amplitudS_string).pack() #amplitud
    
Label(root, text="Digite el largo (m)",font=("Arial",10)).pack()
Entry(root, justify="center",textvariable=largoS_string).pack() #largo
    
Label(root, text="Digite la aceleracion de la gravedad (m/s^2)",font=("Arial",10)).pack()
Entry(root, justify="center",textvariable=gravedadS_string).pack() #largo 
    
Button(root,text="Simular", command= penduloSimple).pack(pady=5) #creando boton dentro de raiz 



"""PENDULO AMORTIGUADO"""

Label(root, text="Pendulo Amortiguado",font=("Arial",12)).pack()

Label(root, text="Digite al amplitud (°)",font=("Arial",10)).pack()
Entry(root, justify="center",textvariable=amplitudA_string).pack() #amplitud
    
Label(root, text="Digite el largo (m)",font=("Arial",10)).pack()
Entry(root, justify="center",textvariable=largoA_string).pack() #largo
    
Label(root, text="Digite la aceleracion de la gravedad (m/s^2)",font=("Arial",10)).pack()
Entry(root, justify="center",textvariable=gravedadA_string).pack() #gravedad 

Label(root, text="Constante de amortiguamiento ",font=("Arial",10)).pack()
Entry(root, justify="center",textvariable=amortiguamientoA_string).pack() #constante amortiguamiento
    
Label(root, text="Digite la masa (kg)",font=("Arial",10)).pack()
Entry(root, justify="center",textvariable=masaA_string).pack() #masa 
  
Button(root,text="Simular", command= penduloAmortiguado).pack(pady=5) #creando boton dentro de raiz


 
"""PENDULO FORZADO AMORTIGUADO"""

Label(root, text="Pendulo Forzado Amortiguado",font=("Arial",12)).pack()

Label(root, text="Digite al amplitud (°)",font=("Arial",10)).pack()
Entry(root, justify="center",textvariable=amplitudFA_string).pack() #amplitud
    
Label(root, text="Digite el largo (m)",font=("Arial",10)).pack()
Entry(root, justify="center",textvariable=largoFA_string).pack() #largo
    
Label(root, text="Digite la aceleracion de la gravedad (m/s^2)",font=("Arial",10)).pack()
Entry(root, justify="center",textvariable=gravedadFA_string).pack() #gravedad 

Label(root, text="Constante de amortiguamiento ",font=("Arial",10)).pack()
Entry(root, justify="center",textvariable=amortiguamientoFA_string).pack() #constante amortiguamiento
    
Label(root, text="Digite la masa (kg)",font=("Arial",10)).pack()
Entry(root, justify="center",textvariable=masaFA_string).pack() #masa

Label(root, text="Constante de amortiguamiento ",font=("Arial",10)).pack()
Entry(root, justify="center",textvariable=amplitudFuerzaFA_string).pack() #Amplitud de la fuerza externa
    
Label(root, text="Digite la masa (kg)",font=("Arial",10)).pack()
Entry(root, justify="center",textvariable=frecuenciaFA_string).pack() #frecuencia de la fuerza externa 


Button(root,text="Simular", command= penduloForzadoAmortiguado).pack(pady=5) #creando boton dentro de raiz 



root.mainloop()