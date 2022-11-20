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
import time

"""
###################################################################################
FUNCION PARA SIMULAR
###################################################################################

"""

def simular(titulo, theta_Simular, simulacion, L):
    
    
    status.set("Cargando simulación...")
    frame3.update_idletasks() 
    
    puntos_simulacion = len(t)
    l_simulacion =np.arange(0,puntos_simulacion,1)

    x_posicion = L*np.sin(theta_Simular)
    y_posicion = -L*np.cos(theta_Simular)
    
    #Eliminando simulación anterior para no haya overlapping
    dir = simulacion
    for f in os.listdir(simulacion):
        os.remove(os.path.join(dir,f))
        
        
    os.chdir(simulacion + '/') #cambia directorio de trabajo

    
    for punto in l_simulacion:
         plt.figure()
         plt.title(titulo)
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
    
    if titulo == "Pendulo Simple":
        os.system("ffmpeg -f image2 -r 20 -i image%05d.png -vcodec mpeg4 -y moviePS.avi")
        movie = "moviePS.avi"
        
    elif titulo == "Pendulo Amortiguado":
        os.system("ffmpeg -f image2 -r 20 -i image%05d.png -vcodec mpeg4 -y moviePA.avi")
        movie = "moviePA.avi"
        
    elif titulo == "Pendulo Forzado Amortiguado":
        os.system("ffmpeg -f image2 -r 20 -i image%05d.png -vcodec mpeg4 -y moviePFA.avi")
        movie = "moviePFA.avi"
        
    elif titulo == "Pendulo Simple Test 1":
        os.system("ffmpeg -f image2 -r 20 -i image%05d.png -vcodec mpeg4 -y movieTest1PS.avi")
        movie = "movieTest1PS.avi"
        
    elif titulo == "Pendulo Simple Test 2":
        os.system("ffmpeg -f image2 -r 20 -i image%05d.png -vcodec mpeg4 -y movieTest2PS.avi")
        movie = "movieTest2PS.avi"

    elif titulo == "Pendulo Simple Test 3":
        os.system("ffmpeg -f image2 -r 20 -i image%05d.png -vcodec mpeg4 -y movieTest3PS.avi")
        movie = "movieTest3PS.avi"
        
    elif titulo == "Pendulo Amortiguado Test 1":
        os.system("ffmpeg -f image2 -r 20 -i image%05d.png -vcodec mpeg4 -y movieTest1PA.avi")
        movie = "movieTest1PA.avi"        

    elif titulo == "Pendulo Amortiguado Test 2":
        os.system("ffmpeg -f image2 -r 20 -i image%05d.png -vcodec mpeg4 -y movieTest2PA.avi")
        movie = "movieTest2PA.avi" 

    elif titulo == "Pendulo Amortiguado Test 3":
        os.system("ffmpeg -f image2 -r 20 -i image%05d.png -vcodec mpeg4 -y movieTest3PA.avi")
        movie = "movieTest3PA.avi" 

    elif titulo == "Pendulo Forzado Amortiguado Test 1":
        os.system("ffmpeg -f image2 -r 20 -i image%05d.png -vcodec mpeg4 -y movieTest1PFA.avi")
        movie = "movieTest1PFA.avi"

    elif titulo == "Pendulo Forzado Amortiguado Test 2":
        os.system("ffmpeg -f image2 -r 20 -i image%05d.png -vcodec mpeg4 -y movieTest2PFA.avi")
        movie = "movieTest2PFA.avi"

    elif titulo == "Pendulo Forzado Amortiguado Test 3":
        os.system("ffmpeg -f image2 -r 20 -i image%05d.png -vcodec mpeg4 -y movieTest3PFA.avi")
        movie = "movieTest3PFA.avi"   

    status.set("¡Listo!")
    frame3.update_idletasks()        
        
    os.startfile(movie) #mostrando video
    os.chdir('../') #Regresando a la direccion anterior de trabajo



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
           
        simulacion = "Simulacion PS"
        L_S = float(largoS_string.get())
        simular(titulo, theta_Graficar, simulacion,L_S)
        
        root2.mainloop()
        
    elif(grafica == "grafica_Pendulo Amortiguado.jpg"):
        root3 = Toplevel()
        root3.title("Pendulo Amortiguado") #titulo de programa
        root3.geometry("500x300") #tamaño de la ventana
        root3.resizable(0,0) #ventana no se puede modificar ancho ni largo
        imagen3 = ImageTk.PhotoImage(Image.open(grafica))
        Label(root3, image=imagen3).pack(side="top")
        
        simulacion = "Simulacion PA"
        L_A = float(largoA_string.get())
        simular(titulo, theta_Graficar, simulacion,L_A)        
        
        root3.mainloop()

    elif(grafica == "grafica_Pendulo Forzado Amortiguado.jpg"):
        root4 = Toplevel()
        root4.title("Pendulo Amortiguado") #titulo de programa
        root4.geometry("500x300") #tamaño de la ventana
        root4.resizable(0,0) #ventana no se puede modificar ancho ni largo
        imagen4 = ImageTk.PhotoImage(Image.open(grafica))
        Label(root4, image=imagen4).pack(side="top")
        
        simulacion = "Simulacion PFA"
        L_FA = float(largoFA_string.get())
        simular(titulo, theta_Graficar, simulacion,L_FA)        
        
        root4.mainloop()
        
     
"""
###################################################################################
FUNCION PARA GRAFICAR TEST
###################################################################################

"""
       
def graficarTest(t,theta_Graficar1,theta_Graficar2,theta_Graficar3, omega_Graficar1,omega_Graficar2,omega_Graficar3,titulo1,titulo2,titulo3,ID):
    plt.plot(t, theta_Graficar1, label = "Desplazamiento angular (rad)")
    plt.plot(t, omega_Graficar1, label = "Velocidad angular (rad/s)")
    plt.title(titulo1)
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Desp. Angular (rad) y Vel. Angular (rad/s)")
    plt.legend()
    grafica1 = "grafica_{}.jpg".format(titulo1)
    plt.savefig(grafica1)
    plt.close()
    
    plt.plot(t, theta_Graficar2, label = "Desplazamiento angular (rad)")
    plt.plot(t, omega_Graficar2, label = "Velocidad angular (rad/s)")
    plt.title(titulo2)
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Desp. Angular (rad) y Vel. Angular (rad/s)")
    plt.legend()
    grafica2 = "grafica_{}.jpg".format(titulo2)
    plt.savefig(grafica2)
    plt.close()    
    
    plt.plot(t, theta_Graficar3, label = "Desplazamiento angular (rad)")
    plt.plot(t, omega_Graficar3, label = "Velocidad angular (rad/s)")
    plt.title(titulo3)
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Desp. Angular (rad) y Vel. Angular (rad/s)")
    plt.legend()
    grafica3 = "grafica_{}.jpg".format(titulo3)
    plt.savefig(grafica3)
    plt.close()    
    
    if ID == "S":
        root5 = Toplevel()
        root5.title("Pendulo Simple Test") #titulo de programa
        root5.geometry("1300x500") #tamaño de la ventana
        root5.resizable(0,1) #ventana no se puede modificar ancho ni largo
        
        Label(root5, text="Amplitud 1: 20°, Amplitud 2: 40°, Amplitud 3: 80°",font=("Arial",12)).pack()
        Label(root5, text="Longitud 1: 0.4 m, Longitud 2: 0.5 m, Longitud 3: 0.5 m",font=("Arial",12)).pack()
        Label(root5, text="Gravedad: 9.8 m/s^2",font=("Arial",12)).pack()
        
        imagenS1 = ImageTk.PhotoImage(Image.open(grafica1))
        Label(root5, image=imagenS1).pack(side = "left")
        
        imagenS2 = ImageTk.PhotoImage(Image.open(grafica2))
        Label(root5, image=imagenS2).pack(side = "left") 
        
        imagenS3 = ImageTk.PhotoImage(Image.open(grafica3))
        Label(root5, image=imagenS3).pack(side = "left")        
        
        """Simulacion Test 1 PS"""
        simulacion1 = "Simulacion Test 1 PS"
        test1_L_S = largoS_Test1
        simular(titulo1, theta_Graficar1, simulacion1,test1_L_S)
        """Simulacion Test 2 PS"""
        simulacion2 = "Simulacion Test 2 PS"
        test2_L_S = largoS_Test2
        simular(titulo2, theta_Graficar2, simulacion2,test2_L_S)
        """Simulacion Test 3 PS"""
        simulacion3 = "Simulacion Test 3 PS"
        test3_L_S = largoS_Test3
        simular(titulo3, theta_Graficar3, simulacion3,test3_L_S)
         
        root5.mainloop()
        
    if ID == "A":
        root6 = Toplevel()
        root6.title("Pendulo Amortiguado Test") #titulo de programa
        root6.geometry("1300x500") #tamaño de la ventana
        root6.resizable(0,1) #ventana no se puede modificar ancho ni largo
        
        Label(root6, text="Test 1: 40°, Test 2: 80°, Test 3: 140°",font=("Arial",12)).pack()
        Label(root6, text="Longitud 1: 0.4 m, Longitud 2: 0.5 m, Longitud 3: 0.5 m",font=("Arial",12)).pack()
        Label(root6, text="Cte Amortiguamiento 1: 0.5, Cte Amortiguamiento 2: 0.5, Cte Amortiguamiento 3: 0.5",font=("Arial",12)).pack()
        Label(root6, text="Masa 1: 1 Kg, Masa 2: 2 Kg, Masa 3: 4 Kg",font=("Arial",12)).pack()
        Label(root6, text="Gravedad: 9.8 m/s^2",font=("Arial",12)).pack()
        
        imagenA1 = ImageTk.PhotoImage(Image.open(grafica1))
        Label(root6, image=imagenA1).pack(side = "left")
        
        imagenA2 = ImageTk.PhotoImage(Image.open(grafica2))
        Label(root6, image=imagenA2).pack(side = "left") 
        
        imagenA3 = ImageTk.PhotoImage(Image.open(grafica3))
        Label(root6, image=imagenA3).pack(side = "left")
        
        """Simulacion Test 1 PA"""
        simulacion1 = "Simulacion Test 1 PA"
        test1_L_A = largoA_Test1
        simular(titulo1, theta_Graficar1, simulacion1,test1_L_A)
        """Simulacion Test 2 PA"""
        simulacion2 = "Simulacion Test 2 PA"
        test2_L_A = largoA_Test2
        simular(titulo2, theta_Graficar2, simulacion2,test2_L_A)
        """Simulacion Test 3 PA"""
        simulacion3 = "Simulacion Test 3 PA"
        test3_L_A = largoA_Test3
        simular(titulo3, theta_Graficar3, simulacion3,test3_L_A)
        
        root6.mainloop()        
    
    if ID == "FA":
        root7 = Toplevel()
        root7.title("Pendulo Forzado Amortiguado Test") #titulo de programa
        root7.geometry("1300x500") #tamaño de la ventana
        root7.resizable(0,1) #ventana no se puede modificar ancho ni largo
        
        Label(root7, text="Test 1: 60°, Test 2: 100°, Test 3: 160°",font=("Arial",12)).pack()
        Label(root7, text="Longitud 1: 0.4 m, Longitud 2: 0.5 m, Longitud 3: 0.5 m",font=("Arial",12)).pack()
        Label(root7, text="Cte Amortiguamiento 1: 0.5, Cte Amortiguamiento 2: 0.5, Cte Amortiguamiento 3: 0.5",font=("Arial",12)).pack()
        Label(root7, text="Masa 1: 1 Kg, Masa 2: 1 Kg, Masa 3: 1 Kg",font=("Arial",12)).pack()
        Label(root7, text="Fuerza 1: 0 N, Fuerza 2: 5 N, Fuerza 3: 10 N",font=("Arial",12)).pack()
        Label(root7, text="Frecuencia 1: 0 rad/s, Frecuencia 2: 10 rad/s, Frecuencia 3: 20 rad/s",font=("Arial",12)).pack()
        Label(root7, text="Gravedad: 9.8 m/s^2",font=("Arial",12)).pack()
        
        imagenFA1 = ImageTk.PhotoImage(Image.open(grafica1))
        Label(root7, image=imagenFA1).pack(side = "left")
        
        imagenFA2 = ImageTk.PhotoImage(Image.open(grafica2))
        Label(root7, image=imagenFA2).pack(side = "left") 
        
        imagenFA3 = ImageTk.PhotoImage(Image.open(grafica3))
        Label(root7, image=imagenFA3).pack(side = "left")
        
        """Simulacion Test 1 PFA"""
        simulacion1 = "Simulacion Test 1 PFA"
        test1_L_FA = largoFA_Test1
        simular(titulo1, theta_Graficar1, simulacion1,test1_L_FA)
        """Simulacion Test 2 PFA"""
        simulacion2 = "Simulacion Test 2 PFA"
        test2_L_FA = largoFA_Test2
        simular(titulo2, theta_Graficar2, simulacion2,test2_L_FA)
        """Simulacion Test 3 PFA"""
        simulacion3 = "Simulacion Test 3 PFA"
        test3_L_FA = largoFA_Test3
        simular(titulo3, theta_Graficar3, simulacion3,test3_L_FA)
        
        root7.mainloop()             
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
FUNCIONES PARA RESOLVER ECUACIONES DIFERENCIALES DE TESTS
###################################################################################
"""
def ecPenduloSimpleTest(y_S,t):
    theta_S, omega_S = y_S
    
    if countS == 1:
        return [omega_S, (-gravedadS_Test/largoS_Test1)*np.sin(theta_S)]  # [dtheta/dt, domega/dt]
    elif countS == 2:
        return [omega_S, (-gravedadS_Test/largoS_Test2)*np.sin(theta_S)]  # [dtheta/dt, domega/dt]
    elif countS == 3:
        return [omega_S, (-gravedadS_Test/largoS_Test3)*np.sin(theta_S)]  # [dtheta/dt, domega/dt]
    
def ecPenduloAmortiguadoTest(y_A,t):
    theta_A, omega_A = y_A
    
    if countA == 1:    
        return [omega_A, (-constantePA_Test1/masaPA_test1)*omega_A + (-gravedadA_Test/largoA_Test1)*np.sin(theta_A)]  # [dtheta/dt, domega/dt]    

    elif countA == 2:
        return [omega_A, (-constantePA_Test2/masaPA_test2)*omega_A + (-gravedadA_Test/largoA_Test2)*np.sin(theta_A)]  # [dtheta/dt, domega/dt]

    elif countA == 3:
        return [omega_A, (-constantePA_Test3/masaPA_test3)*omega_A + (-gravedadA_Test/largoA_Test3)*np.sin(theta_A)]  # [dtheta/dt, domega/dt]        


def ecPenduloForzadoAmortiguadoTest(y_FA,t):
    theta_FA, omega_FA = y_FA
    
    if countFA == 1:
        return [omega_FA, ( ((-constanteFA_Test1/masaFA_test1)*omega_FA) + (-gravedadFA_Test/largoFA_Test1)*np.sin(theta_FA) + (fuerzaFA_test1*np.sin(frecuenciaFA_test1*t)) )]  # [dtheta/dt, domega/dt]
        
    elif countFA == 2:
        return [omega_FA, ( ((-constanteFA_Test2/masaFA_test2)*omega_FA) + (-gravedadFA_Test/largoFA_Test2)*np.sin(theta_FA) + (fuerzaFA_test2*np.sin(frecuenciaFA_test2*t)) )]  # [dtheta/dt, domega/dt]
    
    elif countFA == 3:
        return [omega_FA, ( ((-constanteFA_Test3/masaFA_test3)*omega_FA) + (-gravedadFA_Test/largoFA_Test3)*np.sin(theta_FA) + (fuerzaFA_test3*np.sin(frecuenciaFA_test3*t)) )]  # [dtheta/dt, domega/dt]     


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
    actualizarTiempo()
    
    angulo_inicial_S = float(amplitudS_string.get())        #angulo incial
    theta0_S = np.radians(angulo_inicial_S)                 #grados a radianes
    omega0_S = 0                                            #velocidad inicial
    y0_S = (theta0_S, omega0_S) 
    solucion_S = odeint(ecPenduloSimple,y0_S,t)
    theta_S, omega_S = solucion_S.T
    titulo = "Pendulo Simple"
    
    graficar(t,theta_S, omega_S, titulo)
    
    
def penduloAmortiguado():
    actualizarTiempo()
    
    angulo_inicial_A = float(amplitudA_string.get())        #angulo incial
    theta0_A = np.radians(angulo_inicial_A)                 #grados a radianes
    omega0_A = 0                                            #velocidad inicial
    y0_A = (theta0_A, omega0_A) 
    solucion_A = odeint(ecPenduloAmortiguado,y0_A,t)
    theta_A, omega_A = solucion_A.T
    titulo = "Pendulo Amortiguado"
    
    graficar(t,theta_A, omega_A, titulo)    


def penduloForzadoAmortiguado():
    actualizarTiempo()
    
    angulo_inicial_FA = float(amplitudFA_string.get())        #angulo incial
    theta0_FA = np.radians(angulo_inicial_FA)                 #grados a radianes
    omega0_FA = 0 
    y0_FA = (theta0_FA, omega0_FA)
    solucion_FA = odeint(ecPenduloForzadoAmortiguado,y0_FA,t)
    theta_FA, omega_FA = solucion_FA.T
    titulo = "Pendulo Forzado Amortiguado"
    
    graficar(t,theta_FA, omega_FA, titulo)
    
    
def testS():
    actualizarTiempo()
    
    global gravedadS_Test
    gravedadS_Test = 9.8
  
    global countS
    countS = 1
    """Caso 1"""
    global angulo_inicial_S_Test1
    angulo_inicial_S_Test1 = 20
    global largoS_Test1
    largoS_Test1 = 0.4 
    
    theta0_S = np.radians(angulo_inicial_S_Test1)                 #grados a radianes
    omega0_S = 0                                            #velocidad inicial
    y0_S = (theta0_S, omega0_S) 
    
    solucion_S = odeint(ecPenduloSimpleTest,y0_S,t)
    theta_S1, omega_S1 = solucion_S.T
    titulo1 = "Pendulo Simple Test 1"
    
    countS = 2
    """Caso 2"""
    global angulo_inicial_S_Test2
    angulo_inicial_S_Test2 = 40
    global largoS_Test2
    largoS_Test2 = 0.5
    
    theta0_S = np.radians(angulo_inicial_S_Test2)                 #grados a radianes
    omega0_S = 0                                            #velocidad inicial
    y0_S = (theta0_S, omega0_S) 
    
    solucion_S = odeint(ecPenduloSimpleTest,y0_S,t)
    theta_S2, omega_S2 = solucion_S.T
    titulo2 = "Pendulo Simple Test 2"
    
    countS = 3
    """Caso 3"""
    global angulo_inicial_S_Test3
    angulo_inicial_S_Test3 = 80
    global largoS_Test3
    largoS_Test3 = 0.5
    
    theta0_S = np.radians(angulo_inicial_S_Test3)                 #grados a radianes
    omega0_S = 0                                            #velocidad inicial
    y0_S = (theta0_S, omega0_S) 
    
    solucion_S = odeint(ecPenduloSimpleTest,y0_S,t)
    theta_S3, omega_S3 = solucion_S.T
    titulo3 = "Pendulo Simple Test 3"
    
    graficarTest(t,theta_S1,theta_S2,theta_S3, omega_S1,omega_S2,omega_S3, titulo1,titulo2,titulo3,"S")
    

    
    
def testA():
    actualizarTiempo()
    
    global gravedadA_Test
    gravedadA_Test = 9.8
   
    global countA
    countA = 1
    """Caso 1"""
    global angulo_inicial_A_Test1
    angulo_inicial_A_Test1 = 40
    
    global largoA_Test1
    largoA_Test1 = 0.4

    global constantePA_Test1
    constantePA_Test1 = 0.5
    
    global masaPA_test1
    masaPA_test1 = 1    
    
    theta0_A = np.radians(angulo_inicial_A_Test1)                 #grados a radianes
    omega0_A = 0                                            #velocidad inicial
    y0_A = (theta0_A, omega0_A) 
    solucion_A = odeint(ecPenduloAmortiguadoTest,y0_A,t)
    theta_A1, omega_A1 = solucion_A.T
    titulo1 = "Pendulo Amortiguado Test 1"
    
    countA = 2
    """Caso 2"""
    global angulo_inicial_A_Test2
    angulo_inicial_A_Test2 = 80
    
    global largoA_Test2
    largoA_Test2 = 0.5

    global constantePA_Test2
    constantePA_Test2 = 0.5
    
    global masaPA_test2
    masaPA_test2 = 2    
             
    theta0_A = np.radians(angulo_inicial_A_Test2)                 #grados a radianes
    omega0_A = 0                                            #velocidad inicial
    y0_A = (theta0_A, omega0_A) 
    solucion_A = odeint(ecPenduloAmortiguadoTest,y0_A,t)
    theta_A2, omega_A2 = solucion_A.T
    titulo2 = "Pendulo Amortiguado Test 2"
    
    countA = 3
    """Caso 3"""
    global angulo_inicial_A_Test3
    angulo_inicial_A_Test3 = 140
    
    global largoA_Test3
    largoA_Test3 = 0.5

    global constantePA_Test3
    constantePA_Test3 = 0.5
     
    global masaPA_test3
    masaPA_test3 = 4    
                
    theta0_A = np.radians(angulo_inicial_A_Test3)                 #grados a radianes
    omega0_A = 0                                            #velocidad inicial
    y0_A = (theta0_A, omega0_A) 
    solucion_A = odeint(ecPenduloAmortiguadoTest,y0_A,t)
    theta_A3, omega_A3 = solucion_A.T
    titulo3 = "Pendulo Amortiguado Test 3"    
    
    graficarTest(t,theta_A1,theta_A2,theta_A3, omega_A1,omega_A2,omega_A3, titulo1,titulo2,titulo3,"A")

def testFA():
    actualizarTiempo()
    
    global gravedadFA_Test
    gravedadFA_Test = 9.8  
    
    global countFA 
    countFA = 1
    """Caso 1"""
    global angulo_inicial_FA_Test1
    angulo_inicial_FA_Test1 = 60
    
    global largoFA_Test1
    largoFA_Test1 = 0.4

    global constanteFA_Test1
    constanteFA_Test1 = 0.5
    
    global masaFA_test1
    masaFA_test1 = 1     
    
    global fuerzaFA_test1
    fuerzaFA_test1 = 0    
    
    global frecuenciaFA_test1
    frecuenciaFA_test1 = 0


    theta0_FA = np.radians(angulo_inicial_FA_Test1)                 #grados a radianes
    omega0_FA = 0 
    y0_FA = (theta0_FA, omega0_FA)
    solucion_FA = odeint(ecPenduloForzadoAmortiguadoTest,y0_FA,t)
    theta_FA1, omega_FA1 = solucion_FA.T
    titulo1 = "Pendulo Forzado Amortiguado Test 1"
    
    countFA = 2
    """Caso 2"""
    global angulo_inicial_FA_Test2
    angulo_inicial_FA_Test2 = 100
    
    global largoFA_Test2
    largoFA_Test2 = 0.5

    global constanteFA_Test2
    constanteFA_Test2 = 0.5
    
    global masaFA_test2
    masaFA_test2 = 1     
    
    global fuerzaFA_test2
    fuerzaFA_test2 = 5    
    
    global frecuenciaFA_test2
    frecuenciaFA_test2 = 10


    theta0_FA = np.radians(angulo_inicial_FA_Test2)                 #grados a radianes
    omega0_FA = 0 
    y0_FA = (theta0_FA, omega0_FA)
    solucion_FA = odeint(ecPenduloForzadoAmortiguadoTest,y0_FA,t)
    theta_FA2, omega_FA2 = solucion_FA.T
    titulo2 = "Pendulo Forzado Amortiguado Test 2"       
    
       
    countFA = 3
    """Caso 3"""
    global angulo_inicial_FA_Test3
    angulo_inicial_FA_Test3 = 160
    
    global largoFA_Test3
    largoFA_Test3 = 0.5

    global constanteFA_Test3
    constanteFA_Test3 = 0.5
    
    global masaFA_test3
    masaFA_test3 = 1     
    
    global fuerzaFA_test3
    fuerzaFA_test3 = 10    
    
    global frecuenciaFA_test3
    frecuenciaFA_test3 = 20


    theta0_FA = np.radians(angulo_inicial_FA_Test2)                 #grados a radianes
    omega0_FA = 0 
    y0_FA = (theta0_FA, omega0_FA)
    solucion_FA = odeint(ecPenduloForzadoAmortiguadoTest,y0_FA,t)
    theta_FA3, omega_FA3 = solucion_FA.T
    titulo3 = "Pendulo Forzado Amortiguado Test 3"    
 
    graficarTest(t,theta_FA1,theta_FA2,theta_FA3, omega_FA1,omega_FA2,omega_FA3, titulo1,titulo2,titulo3,"FA")
    
"""
###################################################################################
VARIABLES GLOBALES PARA LA SIMULACIÓN
###################################################################################
"""
#Condiciones iniciales de tiempo
def actualizarTiempo():
    
    global t
    
    t0 = 0                                   #tiempo inicial
    if len(tSimulacion.get()) == 0:          #Si la entrada está vacia
        tf = 5                                      #default 5 seg 
        saltos = tf*25                              #cantidad de pasos, 25 constante para buena visualizacion                          
                          
    else:                                           #Si el usuario digitó un tiempo
        tf = int(tSimulacion.get())               #tiempo final 
        saltos = tf*25                              #cantidad de pasos, 25 constante para buena visualizacion

    t = np.linspace(t0,tf, saltos)
   




"""
###################################################################################
INTERFAZ Y VARIABLES STRINGVAR
###################################################################################
"""


root = Tk()
root.configure(bg='lightblue')
root.title("El pendulo") #titulo de programa
root.iconbitmap('pendulo.ico') #icono de programa
root.geometry("820x450") #tamaño de la ventana
root.resizable(0,0) #venta no se puede modificar ancho ni largo


status = StringVar()

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

"""Tiempo de simulacion"""
tSimulacion = StringVar()

Label(root, bg = "lightblue", text="Simulación de un péndulo",font=("Arial",15)).pack(padx = 10, pady = 10, side = "top")
Label(root, bg = "lightblue", text="Digite el tiempo de simulación (s): ",font=("Arial",8)).pack(padx = 10, pady = 10, side = "top")
Entry(root, justify="center",textvariable=tSimulacion).pack()



"""PENDULO SIMPLE"""

frame1 = Frame(root, bg = "lightblue")

Label(frame1, bg = "lightblue", text="Péndulo Simple",font=("Arial",8)).pack()

Label(frame1, bg = "lightblue", text="Digite la amplitud (°)",font=("Arial",7)).pack()
Entry(frame1, justify="center",textvariable=amplitudS_string).pack() #amplitud
    
Label(frame1, bg = "lightblue", text="Digite el largo (m)",font=("Arial",7)).pack()
Entry(frame1, justify="center",textvariable=largoS_string).pack() #largo
    
Label(frame1, bg = "lightblue", text="Digite la aceleración de la gravedad (m/s^2)",font=("Arial",7)).pack()
Entry(frame1, justify="center",textvariable=gravedadS_string).pack() #largo 
    
Button(frame1,text="Simular", command= penduloSimple).pack(pady=5) #creando boton dentro de frame1

frame1.pack(padx = 5, pady = 5, side = "left")

"""PENDULO AMORTIGUADO"""

frame2 = Frame(root, bg = "lightblue")

Label(frame2, bg = "lightblue", text="Péndulo Amortiguado",font=("Arial",8)).pack()

Label(frame2, bg = "lightblue", text="Digite la amplitud (°)",font=("Arial",7)).pack()
Entry(frame2, justify="center",textvariable=amplitudA_string).pack() #amplitud
    
Label(frame2, bg = "lightblue", text="Digite el largo (m)",font=("Arial",7)).pack()
Entry(frame2, justify="center",textvariable=largoA_string).pack() #largo
    
Label(frame2, bg = "lightblue", text="Digite la aceleración de la gravedad (m/s^2)",font=("Arial",7)).pack()
Entry(frame2, justify="center",textvariable=gravedadA_string).pack() #gravedad 

Label(frame2, bg = "lightblue", text="Constante de amortiguamiento ",font=("Arial",7)).pack()
Entry(frame2, justify="center",textvariable=amortiguamientoA_string).pack() #constante amortiguamiento
    
Label(frame2, bg = "lightblue", text="Digite la masa (kg)",font=("Arial",7)).pack()
Entry(frame2, justify="center",textvariable=masaA_string).pack() #masa 
  
Button(frame2,text="Simular", command= penduloAmortiguado).pack(pady=5) #creando boton dentro de frame2

frame2.pack(padx = 5, pady = 5, side = "left")
 
"""PENDULO FORZADO AMORTIGUADO"""

frame3 = Frame(root, bg = "lightblue")

Label(frame3, bg = "lightblue", text="Péndulo Forzado Amortiguado",font=("Arial",8)).pack()

Label(frame3, bg = "lightblue", text="Digite la amplitud (°)",font=("Arial",7)).pack()
Entry(frame3, justify="center",textvariable=amplitudFA_string).pack() #amplitud
    
Label(frame3, bg = "lightblue", text="Digite el largo (m)",font=("Arial",7)).pack()
Entry(frame3, justify="center",textvariable=largoFA_string).pack() #largo
    
Label(frame3, bg = "lightblue", text="Digite la aceleración de la gravedad (m/s^2)",font=("Arial",7)).pack()
Entry(frame3, justify="center",textvariable=gravedadFA_string).pack() #gravedad 

Label(frame3, bg = "lightblue", text="Constante de amortiguamiento ",font=("Arial",7)).pack()
Entry(frame3, justify="center",textvariable=amortiguamientoFA_string).pack() #constante amortiguamiento
    
Label(frame3, bg = "lightblue", text="Digite la masa (kg)",font=("Arial",7)).pack()
Entry(frame3, justify="center",textvariable=masaFA_string).pack() #masa

Label(frame3, bg = "lightblue", text="Amplitud fuerza externa (N)",font=("Arial",7)).pack()
Entry(frame3, justify="center",textvariable=amplitudFuerzaFA_string).pack() #Amplitud de la fuerza externa
    
Label(frame3, bg = "lightblue", text="Frecuencia fuerza externa (rad/s)",font=("Arial",7)).pack()
Entry(frame3, justify="center",textvariable=frecuenciaFA_string).pack() #frecuencia de la fuerza externa 
Button(frame3,text="Simular", command= penduloForzadoAmortiguado).pack(pady=5) #creando boton dentro de frame3

frame3.pack(padx = 5, pady = 5, side = "left") 

"""PENDULOS PARA TEST"""
frame4 = Frame(root, bg = "lightblue")

"""TEST 1 PENDULO SIMPLE"""
Button(frame4,text="Test 1 Péndulo Simple", command= testS).pack(padx = 5, pady = 5) #creando boton dentro de frame4

"""TEST 2 PENDULO AMORTIGUADO"""
Button(frame4,text="Test 2 Péndulo Amortiguado", command= testA).pack(padx = 5, pady = 5) #creando boton dentro de frame4

""""TEST 3 PENDULO FORZADO AMORTIGUADO"""
Button(frame4,text="Test 3 Péndulo Forzado Amortiguado", command= testFA).pack(padx = 5, pady = 5) #creando boton dentro de frame4

frame4.pack(padx = 5, pady = 5, side = "left")

"""STATUS"""
status.set("")
Label(frame3, bg = "lightblue", textvariable = status, font=("Arial",12)).pack(padx = 10, pady = 10, side = "left")

root.mainloop()