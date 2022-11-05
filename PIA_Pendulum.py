# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 21:19:23 2022

@author: mario
"""
from tkinter import *
from PIL import ImageTk, Image
import math
import numpy as np
import scipy
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import os

"""
###################################################################################
FUNCION PARA SIMULAR
###################################################################################

"""



"""
###################################################################################
FUNCION PARA GRAFICAR
###################################################################################

"""
def graficar(t,theta_Graficar, omega_Graficar, titulo):
    
    plt.plot(t, theta_Graficar, label = "Desplazamiento angular (rad)")
    plt.plot(t, omega_Graficar, label = "Velocidad angular (rad/s)")
    plt.title(titulo)
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Desp. Angular (rad) y Vel. Angular (rad/s)")
    plt.legend()
#   plt.show()
    grafica = "grafica_{}.jpg".format(titulo)
    plt.savefig(grafica)
    plt.close()
    
    if(grafica == "grafica_Pendulo Simple.jpg"):
        root2 = Toplevel()
        root2.title("Pendulo Simple") #titulo de programa
        root2.geometry("500x300") #tamaño de la ventana
        root2.resizable(0,0) #ventana no se puede modificar ancho ni largo
        imagen2 = ImageTk.PhotoImage(Image.open(grafica))
        Label(root2, image=imagen2).pack(side="top")
        root2.mainloop()
        
    elif(grafica == "grafica_Pendulo Amortiguado.jpg"):
        root3 = Toplevel()
        root3.title("Pendulo Amortiguado") #titulo de programa
        root3.geometry("500x300") #tamaño de la ventana
        root3.resizable(0,0) #ventana no se puede modificar ancho ni largo
        imagen3 = ImageTk.PhotoImage(Image.open(grafica))
        Label(root3, image=imagen3).pack(side="top")
        root3.mainloop()

    elif(grafica == "grafica_Pendulo Forzado Amortiguado.jpg"):
        root4 = Toplevel()
        root4.title("Pendulo Amortiguado") #titulo de programa
        root4.geometry("500x300") #tamaño de la ventana
        root4.resizable(0,0) #ventana no se puede modificar ancho ni largo
        imagen4 = ImageTk.PhotoImage(Image.open(grafica))
        Label(root4, image=imagen4).pack(side="top")
        root4.mainloop()
    

"""
###################################################################################
FUNCIONES PARA RESOLVER ECUACIONES DIFERENCIALES
###################################################################################

"""
"""
Ecuacion diferencial

d2Theta/dt2 + (g/L)*senTheta = 0

Reescribir en dos ecuaciones lineales de primer orden

dTheta/dt = omega 

domega/dt = -(g/L)senTheta

"""
def ecPenduloSimple(y_S,t):
    theta_S, omega_S = y_S
    g_S = float(gravedadS_string.get())
    L_S = float(largoS_string.get())
    
    return [omega_S, (-g_S/L_S)*np.sin(theta_S)]  # [dtheta/dt, domega/dt]

    
"""
Ecuacion diferencial

d2Theta/dt2 + (b/m)*dTheta/dt + (g/L)*senTheta = 0

Reescribir en dos ecuaciones lineales de primer orden

dTheta/dt = omega 

domega/dt = -(b/m)*dTheta/dt -(g/L)senTheta

"""


def ecPenduloAmortiguado(y_A,t):
    theta_A, omega_A = y_A
    g_A = float(gravedadA_string.get())
    L_A = float(largoA_string.get())
    b_A = float(amortiguamientoA_string.get())
    m_A = float(masaA_string.get())
    
    return [omega_A, (-b_A/m_A)*omega_A + (-g_A/L_A)*np.sin(theta_A)]  # [dtheta/dt, domega/dt]


"""
Ecuacion diferencial

d2Theta/dt2 + (b/m)*dTheta/dt + (g/L)*senTheta = Asen(wt)
d2Theta/dt2 + (g/L)*senTheta - Asen(wt)= 0

Reescribir en dos ecuaciones lineales de primer orden

dTheta/dt = omega 

domega/dt = -(b/m)*dTheta/dt -(g/L)senTheta + Asen(wt)

"""


def ecPenduloForzadoAmortiguado(y_FA,t):
    theta_FA, omega_FA = y_FA
    b_FA = float(amortiguamientoFA_string.get())
    m_FA = float(masaFA_string.get())
    g_FA = float(gravedadFA_string.get())
    L_FA = float(largoFA_string.get())
    A_fuerza = float(amplitudFuerzaFA_string.get())
    w_fuerza = float(frecuenciaFA_string.get())
    
    return [omega_FA, ( ((-b_FA/m_FA)*omega_FA) + (-g_FA/L_FA)*np.sin(theta_FA) + (A_fuerza*np.sin(w_fuerza*t)) )]  # [dtheta/dt, domega/dt]



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
    angulo_inicial_S = float(amplitudS_string.get())        #angulo incial
    theta0_S = np.radians(angulo_inicial_S)                 #grados a radianes
    omega0_S = 0                                            #velocidad inicial
    y0_S = (theta0_S, omega0_S) 
    solucion_S = odeint(ecPenduloSimple,y0_S,t)
    theta_S, omega_S = solucion_S.T
    titulo = "Pendulo Simple"
    
    graficar(t,theta_S, omega_S, titulo)
    
    
def penduloAmortiguado():
    angulo_inicial_A = float(amplitudA_string.get())        #angulo incial
    theta0_A = np.radians(angulo_inicial_A)                 #grados a radianes
    omega0_A = 0                                            #velocidad inicial
    y0_A = (theta0_A, omega0_A) 
    solucion_A = odeint(ecPenduloAmortiguado,y0_A,t)
    theta_A, omega_A = solucion_A.T
    titulo = "Pendulo Amortiguado"
    
    graficar(t,theta_A, omega_A, titulo)    


def penduloForzadoAmortiguado():
    angulo_inicial_FA = float(amplitudFA_string.get())        #angulo incial
    theta0_FA = np.radians(angulo_inicial_FA)                 #grados a radianes
    omega0_FA = 0 
    y0_FA = (theta0_FA, omega0_FA)
    solucion_FA = odeint(ecPenduloForzadoAmortiguado,y0_FA,t)
    theta_FA, omega_FA = solucion_FA.T
    titulo = "Pendulo Forzado Amortiguado"
    
    graficar(t,theta_FA, omega_FA, titulo)
    

"""
###################################################################################
VARIABLES GLOBALES PARA LA SIMULACIÓN
###################################################################################
"""
#Condiciones iniciales de tiempo
   
t0 = 0            #tiempo inicial
tf = 15           #tiempo final 
saltos = tf*25    #cantidad de pasos, 25 constante para buena visualizacion

t = np.linspace(t0,tf, saltos)



"""
###################################################################################
INTERFAZ Y VARIABLES STRINGVAR
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

Label(root, text="Digite la amplitud (°)",font=("Arial",10)).pack()
Entry(root, justify="center",textvariable=amplitudS_string).pack() #amplitud
    
Label(root, text="Digite el largo (m)",font=("Arial",10)).pack()
Entry(root, justify="center",textvariable=largoS_string).pack() #largo
    
Label(root, text="Digite la aceleracion de la gravedad (m/s^2)",font=("Arial",10)).pack()
Entry(root, justify="center",textvariable=gravedadS_string).pack() #largo 
    
Button(root,text="Simular", command= penduloSimple).pack(pady=5) #creando boton dentro de raiz 



"""PENDULO AMORTIGUADO"""

Label(root, text="Pendulo Amortiguado",font=("Arial",12)).pack()

Label(root, text="Digite la amplitud (°)",font=("Arial",10)).pack()
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

Label(root, text="Digite la amplitud (°)",font=("Arial",10)).pack()
Entry(root, justify="center",textvariable=amplitudFA_string).pack() #amplitud
    
Label(root, text="Digite el largo (m)",font=("Arial",10)).pack()
Entry(root, justify="center",textvariable=largoFA_string).pack() #largo
    
Label(root, text="Digite la aceleracion de la gravedad (m/s^2)",font=("Arial",10)).pack()
Entry(root, justify="center",textvariable=gravedadFA_string).pack() #gravedad 

Label(root, text="Constante de amortiguamiento ",font=("Arial",10)).pack()
Entry(root, justify="center",textvariable=amortiguamientoFA_string).pack() #constante amortiguamiento
    
Label(root, text="Digite la masa (kg)",font=("Arial",10)).pack()
Entry(root, justify="center",textvariable=masaFA_string).pack() #masa

Label(root, text="Amplitud fuerza externa (N)",font=("Arial",10)).pack()
Entry(root, justify="center",textvariable=amplitudFuerzaFA_string).pack() #Amplitud de la fuerza externa
    
Label(root, text="Frecuencia fuerza externa (rad/s)",font=("Arial",10)).pack()
Entry(root, justify="center",textvariable=frecuenciaFA_string).pack() #frecuencia de la fuerza externa 


Button(root,text="Simular", command= penduloForzadoAmortiguado).pack(pady=5) #creando boton dentro de raiz 



root.mainloop()