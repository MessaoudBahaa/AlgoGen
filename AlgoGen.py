#!/usr/local/bin/python
# coding: utf-8

import os, sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
import random 
import math 


# Fonction pour calculer l'évaluation d'individu (Fitness)
def fitness(individu):
    fit = np.sum(individu[0:len(individu)-2], dtype = np.uint8)
   # print(individu[0:len(individu)-1])
    individu[len(individu)-2]=fit
    return fit


#Fonction pour faire le croisement monopoint avec une probabilité probCroisement
def croiser_monopoint(parent1, parent2  , probCroisement):
    if ( random.random() <= probCroisement):
        #faire croisement
        rand=random.randint(1,tailleIndividu)
        print (rand)

      
        fils1= np.concatenate((parent1[:rand] , parent2[rand:]), axis = None)
        fitness(fils1)
        fils2= np.concatenate((parent2[:rand] , parent1[rand:]), axis = None)
        fitness(fils2)

        return fils1, fils2, True
    return [0]*(tailleIndividu+2),[0]*(tailleIndividu+2),False

#Fonction pour faire le croisement uniforme avec une probabilité probCroisement
def croiser_uniforme(parent1,parent2 , probCroisement):
        
        fils1= []
        fils2=[]
        if ( random.random() <= probCroisement):
            #faire le croisement
            for i in range(tailleIndividu+2):
                if bool(np.random.randint(2)) :
                    fils1.append(parent1[i])
                    fils2.append(parent2[i])
                else:
                    fils1.append(parent2[i])
                    fils2.append(parent1[i])
            fitness(fils1)
            fitness(fils2)
            return np.array(fils1), np.array(fils2), True
        return np.array([0]*(tailleIndividu+2)), np.array([0]*(tailleIndividu+2)), False
    
# Fonction pour faire la mutation bit flip => changer chaque bit avec une probabilité prob
def mutation_bit_flip(parent1,parent2,probMutation):
    fils1= []
    fils2=[]
  
    for x in parent1:
        if (random.random() < probMutation):
            fils1.append( abs(x-1)) #(not(x.astype(bool))).astype(int))
        else:
            fils1.append(x)
    
    for x in parent2:
        if (random.random() < probMutation):
            fils2.append( abs(x-1))# (not(x.astype(bool))).astype(int))
        else:
            fils2.append(x)

    fitness(fils1)
    fitness(fils2)

    #Mettre a jour l'age
    fils1[-1]=0
    fils2[-1]=0
    return np.array(fils1) , np.array(fils2) , True 

# Fonction pour fair des mutation K-flips: 1-flip, 2-flip, 3-flip
def mutation_k_flips(parent1,parent2,probMutation,k):
    fils1= parent1
    fils2= parent2
    #list contenant les indices a choisir aléatoirement
    rands = list (range (tailleIndividu))
    #Muter le premier fils
    for i in range(k):
        random.shuffle(rands)
        if(random.random() < probMutation):
            fils1[rands[-1]] = abs(fils1[rands[-1]]-1)
        rands.pop()

    #list contenant les indices a choisir aléatoirement
    rands = list (range (tailleIndividu))
    #Muter le deuxieme fils
    for i in range(k):
        random.shuffle(rands)
        if(random.random() < probMutation):
            fils2[rands[-1]] = abs(fils2[rands[-1]]-1)
        rands.pop()
    fitness(fils1)
    fitness(fils2)

    # mettre a jour l'age
    fils1[-1]=0
    fils2[-1]=0
    return fils1,fils2,True
# AG  ( taille de population = 20, taille d'individu, initmode, selection , croisement, proba croisement, mutation , probalité mutation, proba mutation , insertion, nb generation)

# Demmarrer avec 100 bits ensuite on peut changer


# Etude des paramètres 

# Probabilité de mutation avec bit flip N = 100 (sans croisement) 
# fixer l'insertion (fitness) et selection (tarmi)



# taille population en performance

# calculer l'amélioration a chaque fois pour avoir la moyenne d'amélioration par exemple de mutation de 3-flips = somme des amélioration sur nb utilisation (utilité)

# Amaçage - > appliquer chaque op 10 fois au départ et voir l'utilité de chaque mutation ( 1 flip 3 flip 5 flip bit flip) et les presenter en proba proportionnelle  ------ E greedy


# pour chaque test : on fait 20 executions ---> on fait la moyenne 


# return  :   - graine aléatoire 
#             - fichier externe : valeur de meilleur solution pour chaque iteration // Nom fichier important

# parameter


taillePopulation = 10 
tailleIndividu = 10
init = 1

# =========== INITIALISATION =======================
# initialiser la population avec des zeros
population = np.zeros( (taillePopulation,tailleIndividu+2),  dtype=np.uint8 )

if init != 0:
    # Initialiser avec des valeurs aléatoires
    population = np.concatenate( (np.random.rand(taillePopulation,tailleIndividu+1 ) , np.zeros((taillePopulation,1))), axis=1)
    population = (population > 0.5).astype(int)
    #population[:,tailleIndividu+2]=0

    # Calculer Fitness des individus
    for i in population:
        fitness(i)

    # Ordonner la population suivant la derniere colonne (fitness)
    ind = np.argsort( population[:,tailleIndividu] *-1)
    population= population[ind]

population= population.astype(int)
# ============ SELECTION =====================================


# Choisir les 2 meilleurs 
parent1=population[0]
parent2=population[1]

# Choisir 2 au hazard 
rand=random.randint(0,taillePopulation-1)

parent1=population[rand]

rand=random.randint(0,taillePopulation-2)

parent2= (np.delete(population,rand,0))[rand]
    


# Choisir 2 meilleurs de 5 au hasard 
populationSheet=population

parent1 = np.zeros((1,tailleIndividu+1)).astype(int)
parent2 = parent1

for i in range (5):
    rand=random.randint(0,taillePopulation-1-i)
    if  fitness(populationSheet[rand]) > fitness(parent1)  :
        
        if fitness(parent1) > fitness(parent2):
            parent2 = parent1 
        parent1 = populationSheet[rand]
    elif fitness(populationSheet[rand]) > fitness(parent2) :
        parent2 = populationSheet[rand]
    populationSheet= np.delete(populationSheet,rand,0)



# ================== CROISEMENT ==============
print('---------------- THIS IS NEW --------------------------------')
print(population)
print('---------------- THESE ARE PARENTS --------------------------------')
print(parent1)
print(parent2)
fils1 = np.zeros((1,tailleIndividu+1)).astype(int)
fils2 = fils1
"""


fils1, fils2, estCrois = croiser_monopoint(parent1,parent2,0.5)

print(fils1)
print(fils2)

"""

#fils1, fils2, estCrois = croiser_monopoint(parent1,parent2,1)

#fils1, fils2, estCrois = croiser_uniforme(parent1,parent2,1)

fils1, fils2, estMute = mutation_bit_flip(parent1,parent2,1)

#fils1, fils2, estMute = mutation_k_flips(parent1,parent2,1,3)


# insertion suivant la fitness

# Ordonner la population suivant l'avant derniere colonne (fitness)
ind = np.argsort( population[:,tailleIndividu] *-1)
population= population[ind]
# supprimer les individus les plus mauvais 
population=population[:-2] 

# Mettre a jour l'age de la population par fitness
population[:,-1]=population[:,-1]+1



# insertion suivant l'age
# Ordonner la population suivant la derniere colonne (age de l'individu)
ind = np.argsort( population[:,tailleIndividu+1] *-1)
population= population[ind]
# supprimer les individus les plus mauvais par age
population=population[:-2] 


#np.concatenate((population ,fils1),axis=1)


print (np.array([fils1,fils2]))

# remplacer les individus les plus mauvais 
population = np.append(population,np.array([fils1,fils2]),axis=0) # here were a problem 



#sauvgarde


print('---------------- THIS THE NEW POP --------------------------------')
print(population)
print('---------------- THESE ARE CHILDREN --------------------------------')
print(fils1)
print(fils2)
print('Finished')

