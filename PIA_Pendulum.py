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




def penduloSimple():
    pass


def penduloAmortiguado():
    pass

def penduloForzadoAmortiguado():
    pass




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
amplitudA_string = StringVar()
largoA_string = StringVar()
gravedadA_string = StringVar()
amortiguamientoA_string = StringVar()
masaA_string = StringVar()
amplitudFuerzaFA_string = StringVar()
frecuenciaFA_string = StringVar()


"""PENDULO SIMPLE"""

Label(root, text="Pendulo Simple",font=("Arial",15)).pack()

Label(root, text="Digite al amplitud (°)",font=("Arial",10)).pack()
Entry(root, justify="center",textvariable=amplitudS_string).pack() #amplitud
    
Label(root, text="Digite el largo (m)",font=("Arial",10)).pack()
Entry(root, justify="center",textvariable=largoS_string).pack() #largo
    
Label(root, text="Digite la aceleracion de la gravedad (m/s^2)",font=("Arial",10)).pack()
Entry(root, justify="center",textvariable=gravedadS_string).pack() #largo 
    
Button(root,text="Simular", command= penduloSimple).pack(pady=5) #creando boton dentro de raiz 



"""PENDULO AMORTIGUADO"""

Label(root, text="Pendulo Amortiguado",font=("Arial",15)).pack()

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

Label(root, text="Pendulo Forzado Amortiguado",font=("Arial",15)).pack()

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