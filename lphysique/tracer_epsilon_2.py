# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 13:37:59 2020

@author: Alain Gellé
Université de Rennes 1
Master préparation à l'agrégation de physique
"""

import numpy as np
import matplotlib.pyplot as plt
#import matplotlib.animation as anim    
from matplotlib.widgets import Slider, Button, RadioButtons

"""
Principe :
    Le programme trace une fonction à l'aide de matplotlib
    Il ajoute des "widget" "Slider" qui permettent de modifier
    deux paramètres de la fonction.

Mode d'emploi :
    (1) Mettre la fonction voulue dans "ma_fonction"
        Les deux paramètres sont notés A et B.
    (2) Rentrer les valeurs initiales, min et max
        ainsi que le nom des paramètres.


"""


##### (1) Définition de la fonction
def ma_fonction(x):
    y = np.zeros(x.size)
    for i in range(x.size):
        y = A*((x)/B)/((1-(x)**2)**2+((x)/B)**2)
    return y


##### (2) Définition des paramètres Xe et Q
# Valeur initiale
A0 = 0.2
B0 = 10
A = A0
B = B0
# valeur extremales
Amin = 0
Amax = 10*A0
Bmin = 0
Bmax = 5*B0
# Nom des paramètres
Anom = "Chi_e"
Bnom = "Facteur de qualité"


##### Définition de l'axe des x 
# N est l nombre de points sur l'axe
N = 101
x = np.linspace(0,3,N)

##### Définition du graphique
fig = plt.figure() #figure animation
# ax=plt.axes(xlim=(0,1.),ylim=(-1.2,2.05))  #Axes x et y
ax = plt.axes()
plt.subplots_adjust(left = 0.1,bottom=0.25)  #on place le graphique sur la page
courbe, = ax.plot(x,ma_fonction(x))
plt.title(r"$\varepsilon_2(\omega)$")
plt.text(2.7,0.2, r"$\frac{\omega}{\omega_0}$",fontsize=20)
# premier slider
A_axSlider = plt.axes([0.2,0.07,0.7,0.05])
A_Slider = Slider(A_axSlider,Anom,Amin,Amax,A0)  
# deuxième slider
B_axSlider = plt.axes([0.2,0.12,0.7,0.05])
B_Slider = Slider(B_axSlider,Bnom,Bmin,Bmax,B0)

##### fonction pour modifier les paramètres et actulaiser la courbe
def update(val):    
    global A, B
    # on change la valeur des paramètres
    A = A_Slider.val
    B = B_Slider.val
    # on recalcul et on affiche la fonction
    courbe.set_ydata(ma_fonction(x))
    
A_Slider.on_changed(update)
B_Slider.on_changed(update)

# On lance le calcul du graph
plt.show()