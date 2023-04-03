import itertools
import random
import pandas as pd


# Les fonctions 

# Fonction qui calcule l'energie du clavier
def energie():
    
    return 0


# Fonction qui calcule un voisin du clavier donner 
def voisin(clavier):
    nouveau_clavier = [ligne[:] for ligne in clavier]
   
    i1, j1 = random.randint(0, len(clavier)-1), random.randint(0, len(clavier[0])-1)
    i2, j2 = random.randint(0, len(clavier)-1), random.randint(0, len(clavier[0])-1)

    while i1 == i2 and j1 == j2 or nouveau_clavier[i1][j1] == nouveau_clavier[i2][j2]:
        i2, j2 = random.randint(0, len(clavier)-1), random.randint(0, len(clavier[0])-1)
    
    nouveau_clavier[i1][j1], nouveau_clavier[i2][j2] = nouveau_clavier[i2][j2], nouveau_clavier[i1][j1]
    
    return nouveau_clavier


def frequence(lettre1,lettre2):
    lettre1 = '_'+lettre1

    # On numerote les lettres 
    if(lettre2 == 'A'):
        lettre2 = 0
    if(lettre2 == 'B'):
        lettre2 = 1
    if(lettre2 == 'C'):
        lettre2 = 2
    if(lettre2 == 'D'):
        lettre2 = 3
    if(lettre2 == 'E'):
        lettre2 = 4
    if(lettre2 == 'F'):
        lettre2 = 5
    if(lettre2 == 'G'):
        lettre2 = 6
    if(lettre2 == 'H'):
        lettre2 = 7
    if(lettre2 == 'I'):
        lettre2 = 8
    if(lettre2 == 'J'):
        lettre2 = 9
    if(lettre2 == 'K'):
        lettre2 = 10
    if(lettre2 == 'L'):
        lettre2 = 11
    if(lettre2 == 'M'):
        lettre2 = 12
    if(lettre2 == 'N'):
        lettre2 = 13
    if(lettre2 == 'O'):
        lettre2 = 14
    if(lettre2 == 'P'):
        lettre2 = 15
    if(lettre2 == 'Q'):
        lettre2 = 16
    if(lettre2 == 'R'):
        lettre2 = 17
    if(lettre2 == 'S'):
        lettre2 = 18
    if(lettre2 == 'T'):
        lettre2 = 19
    if(lettre2 == 'U'):
        lettre2 = 20
    if(lettre2 == 'V'):
        lettre2 = 21
    if(lettre2 == 'W'):
        lettre2 = 22
    if(lettre2 == 'X'):
        lettre2 = 23
    if(lettre2 == 'Y'):
        lettre2 = 24
    if(lettre2 == 'Z'):
        lettre2 = 25
               

    data =pd.read_table('freqBigrammes.txt')
    #print(data['_A']['A_'])
    #df = pd.DataFrame(data)
    #print(df)
    print(data[lettre1][lettre2])
    return 0



# On crée un clavier vide de 4x10 
clavier = [['_' for j in range(10)] for i in range(4)]


lettres = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

frequence('B','B')

# Clavier de départ 
# Placement aléatoire des lettres sur le clavier
for lettre in lettres:
    i = random.randint(0, 3)
    j = random.randint(0, 9)
    while clavier[i][j] != '_':
        i = random.randint(0, 3)
        j = random.randint(0, 9)
    clavier[i][j] = lettre



# Affichage du clavier, une casse vide du tableau est défini par _
for i in range(4):
    for j in range(10):
        print(clavier[i][j], end=' ')
    print()


print()

# Affichage du  nvx clavier, une casse vide du tableau est défini par _
clavier = voisin(clavier)
for i in range(4):
    for j in range(10):
        print(clavier[i][j], end=' ')
    print()

