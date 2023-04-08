import random
import pandas as pd
import math
from matplotlib import pyplot as plt
import numpy as np
import signal
import sys

# LES FONCTIONS 

# Fonction qui calcule un voisin du clavier donner 
def voisin(clavier):
    nouveau_clavier = [ligne[:] for ligne in clavier]
   
    i1, j1 = random.randint(0, len(clavier)-1), random.randint(0, len(clavier[0])-1)
    i2, j2 = random.randint(0, len(clavier)-1), random.randint(0, len(clavier[0])-1)

    while i1 == i2 and j1 == j2 or nouveau_clavier[i1][j1] == nouveau_clavier[i2][j2]:
        i2, j2 = random.randint(0, len(clavier)-1), random.randint(0, len(clavier[0])-1)
    
    nouveau_clavier[i1][j1], nouveau_clavier[i2][j2] = nouveau_clavier[i2][j2], nouveau_clavier[i1][j1]
    
    return nouveau_clavier


# Fonction qui lit la frenquence de 2 lettre
# lettreL = _B / lettreC = C_
def frequence(lettreL,lettreC):
    lettreL = '_'+lettreL

    # On convertie en num pour les colonnes
    lettreInt = ord(lettreC) - ord('A')

    data =pd.read_table('freqBigrammes.txt')
    return data[lettreL][lettreInt]


# Fonction qui calcule la distance entre 2 lettre
def dist(lettreL, lettreC, clavier):
    # Récupération des indices des touches correspondantes
    iL, jL = position(clavier, lettreL)
    iC, jC = position(clavier, lettreC)
    
    # Calcul de la distance euclidienne entre les touches
    dist = math.sqrt((iL - iC) ** 2 + (jL - jC) ** 2)
    
    return dist


# Fonction qui permet de recuperer la position d'une lettre
def position(clavier, lettre):
    for i in range(len(clavier)):
        for j in range(len(clavier[0])):
            if clavier[i][j] == lettre:
                return i, j
    return None


# Fonction qui calcule l'energie du clavier
def energie(clavier):
    somme = 0
    # On parcours le clavier 
    for i in range(4):
        for j in range(10):

            # Si c'est une lettre 
            if(clavier[i][j] != '_'):
               # On parcour les lettre de l'aphaB
               for lettre in lettres:
                    
                    # Formule de l'energie 
                    somme = somme + dist(lettre, clavier[i][j],clavier) * frequence(lettre, clavier[i][j])
    

    return somme


# Fonction à appeler lors de la fermeture de la fenêtre du graphe 
def on_close(event):
    stop()


# Fonction fermeture crtl+C
def handle_signal(signal, frame):
   stop()


# Calcule de T0 
def T0():
    clavierTest = clavier
    result = 0
    for i in range(100):
        clavierTest = voisin(clavierTest)
       
    return (energie(clavierTest) + energie(clavier)) /2


# Ferme correctement le programme 
def stop():
    plt.close()
    print( "Resultat obtenue avec", somme, "iterations")
    print( "L'énergie trouver:", energie(clavier))
    print("Clavier obtenue (les \"_\" sont considérer comme des cases vides):")
    for i in range(4):
        for j in range(10):
            print(clavier[i][j], end=' ')
        print()
    raise SystemExit


# LE MAIN
#Crée le graphe
x = []
y = []

fig, ax = plt.subplots()
line, = ax.plot(x, y,'-*b')

# Fermeture 
plt.gcf().canvas.mpl_connect('close_event', on_close)
signal.signal(signal.SIGINT, handle_signal)

# Definir Graphe
plt.xlabel("Nombre d'itérations", fontsize=8)
plt.ylabel("Température", fontsize=8)
plt.title("Evolution de la méthode du recuit simulé.", fontsize=8)

# On crée un clavier vide de 4x10 
clavier = [['_' for j in range(10)] for i in range(4)]
lettres = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

# Clavier de départ 
# Placement aléatoire des lettres sur le clavier
for lettre in lettres:
    i = random.randint(0, 3)
    j = random.randint(0, 9)
    while clavier[i][j] != '_':
        i = random.randint(0, 3)
        j = random.randint(0, 9)
    clavier[i][j] = lettre

somme =0
palier1=0
palier2 =0
temp = T0()

while(True) : 
    somme = somme +1
    clavierVoisin = voisin(clavier)

    # Plus l'energie est petite mieux c'est 
    if(energie(clavierVoisin) < temp):
        clavier = clavierVoisin 
        palier1 = palier1 +1
        temp = energie(clavier)
    
    palier2 =palier2 +1

    # Calcule du palier
    if(palier1 == 12 or palier2 == 100):
        palier1 =0
        plt.axvline(x=somme, color='red')
        palier2 =0
    
    # Si 100 iterarations se passe sens changement, alors on considaire qu'on stagne  
    if(palier2 == 100 and palier1 == 0):
        stop()

    # Pour le graphe
    x.append(somme)
    y.append(energie(clavierVoisin))
    line.set_data(x, y)
    ax.relim()
    ax.autoscale_view()
    plt.draw()
    plt.pause(0.1)




