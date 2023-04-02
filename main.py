import itertools
import random


# Les fonctions 

# Fonction qui calcule l'energie du clavier


# Fonction qui calcule un voisin du clavier donner 
def voisin(clavier):
    nouveau_clavier = [ligne[:] for ligne in clavier]
   
    i1, j1 = random.randint(0, len(clavier)-1), random.randint(0, len(clavier[0])-1)
    i2, j2 = random.randint(0, len(clavier)-1), random.randint(0, len(clavier[0])-1)

    while i1 == i2 and j1 == j2 or nouveau_clavier[i1][j1] == nouveau_clavier[i2][j2]:
        i2, j2 = random.randint(0, len(clavier)-1), random.randint(0, len(clavier[0])-1)
    
    nouveau_clavier[i1][j1], nouveau_clavier[i2][j2] = nouveau_clavier[i2][j2], nouveau_clavier[i1][j1]
    
    return nouveau_clavier




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

