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
    tailleIndividu = len(parent1)-2
    if ( random.random() <= probCroisement):
        #faire croisement
        rand=random.randint(1,tailleIndividu)
        print (rand)

      
        fils1= np.concatenate((parent1[:rand] , parent2[rand:]), axis = None)
        fitness(fils1)
        fils2= np.concatenate((parent2[:rand] , parent1[rand:]), axis = None)
        fitness(fils2)

        return fils1, fils2, True
    return parent1, parent2, False

#Fonction pour faire le croisement uniforme avec une probabilité probCroisement
def croiser_uniforme(parent1,parent2 , probCroisement):
    tailleIndividu = len(parent1)-2
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
    return parent1, parent2, False
    
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
    return np.array(fils1) , np.array(fils2) , True 

# Fonction pour fair des mutation K-flips: 1-flip, 2-flip, 3-flip
def mutation_k_flips(parent1,parent2,probMutation,k):
    tailleIndividu = len(parent1)-2
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

def AG  ( taillePopulation =100 , tailleIndividu = 10, init = 1, selection = 0 , croisement = 0 , prob_croisement = 0, mutation = 0 , prob_mutation = 0 , insertion = 1 , nb_generation = 100):
    """
    taillePopulation : la taille de la population  # par defaut 100
    tailleIndividu : la taille de l'individu # par defaut 10 
    init : mode d'initialisation 
        0 : initialiser toute la population à zero
        1 : initialiser la population aléatoirement # la valeur par defaut
    selection : mode de selection
        0 : 2 meilleurs individus
        1 : 2 au hasard 
        2 : 2 meilleurs parmi 5 au hasard # la valeur par defaut
    croisement : type de croisement à effectuer 
        0 : ne pas effectuer croisement # la valeur par defaut
        1 : effectuer un croisement mono-point
        2 : effectuer un croisement uniforme
    prob_croisement : probabilité de croisement, valeurs réelles entre 0 et 1 # la valeur par defaut 0
    mutation :  type de mutation à effectuer 
        0 : ne pas effectuer croisement # la valeur par defaut 
        1 : 1-flip mutation
        2 : 3-flip mutation
        3 : 5-flip mutation 
        4 : bit flip mutation : changer chaque bit avec une probabilité de 1/n
    prob_mutation : probabilité de mutation, valeurs réelles entre 0 et 1 # la valeur par defaut 0
    insertion : mode d'insertion 
        0 : remplacer les individus les plus agés
        1 : remplacer les individus les plus mauvais # la valeur par defaut
    nb_generation : nombre de generation auquel on veut arreter l'algorithme génetique (critère d'arret) # la valeur par defaut 100
    sauvgarde : ....
    """

    # =========== INITIALISATION =======================
    """
    init : mode d'initialisation 
        0 : initialiser toute la population à zero
        1 : initialiser la population aléatoirement # la valeur par defaut
    """


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
    """
    selection : mode de selection
        0 : 2 meilleurs individus
        1 : 2 au hasard 
        2 : 2 meilleurs parmi 5 au hasard # la valeur par defaut
    """
    if (selection == 0):
        # Choisir les 2 meilleurs 
        parent1=population[0]
        parent2=population[1]
    
    elif (selection == 1):
        # Choisir 2 au hazard 
        rand=random.randint(0,taillePopulation-1)

        parent1=population[rand]

        rand=random.randint(0,taillePopulation-2)

        parent2= (np.delete(population,rand,0))[rand]
            

    elif (selection == 2):
        # Choisir 2 meilleurs de 5 au hasard 
        populationSheet=population

        parent1 = np.zeros((1,tailleIndividu+1)).astype(int)
        parent2 = parent1

        for i in range (5):
            rand=random.randint(0,taillePopulation-1-i)
            if  fitness(populationSheet[rand]) >= fitness(parent1)  :
                
                if fitness(parent1) >= fitness(parent2):
                    parent2 = parent1 
                parent1 = populationSheet[rand]
            elif fitness(populationSheet[rand]) >= fitness(parent2) :
                parent2 = populationSheet[rand]
            populationSheet= np.delete(populationSheet,rand,0)
    else : 
        print('valeur de selection non reconnu')


    # ==================== CROISEMENT =======================

    print('---------------- THIS IS THE POP --------------------------------')
    print(population)
    print('---------------- THESE ARE PARENTS --------------------------------')
    print(parent1)
    print(parent2)
    
    # les deux fils
    fils1 = np.zeros((1,tailleIndividu+1)).astype(int)
    fils2 = fils1

    """
    croisement : type de croisement à effectuer 
        0 : ne pas effectuer croisement # la valeur par defaut
        1 : effectuer un croisement mono-point
        2 : effectuer un croisement uniforme
    prob_croisement : probabilité de croisement, valeurs réelles entre 0 et 1 # la valeur par defaut 0
    """
    estCrois = False
    if (croisement == 0): 
        # ne rien faire (pas de croisement)
        fils1 = parent1
        fils2 = parent2
    elif (croisement == 1):
        # faire un croisement mono point
        fils1, fils2, estCrois = croiser_monopoint(parent1,parent2,prob_croisement)
    elif (croisement == 2):
        # faire un croisement uniforme
        fils1, fils2, estCrois = croiser_uniforme(parent1,parent2,prob_croisement)
    else : 
        print('valeur de croisement non reconnu')
        fils1 = parent1
        fils2 = parent2


    # ====================== MUTATION ====================
    """
    mutation :  type de mutation à effectuer 
        0 : ne pas effectuer croisement # la valeur par defaut 
        1 : 1-flip mutation
        2 : 3-flip mutation
        3 : 5-flip mutation 
        4 : bit flip mutation : changer chaque bit 
    prob_mutation : probabilité de mutation, valeurs réelles entre 0 et 1 # la valeur par defaut 0
    """
    estMute = False
    if (mutation == 0 ):
        # ne pas faire mutation
        estMute = False
    elif (mutation == 1 ):
        # faire une mutation 1-flip
        fils1, fils2, estMute = mutation_k_flips(fils1,fils2,prob_mutation,1)
    elif (mutation == 2 ):
        # faire une mutation 3-flip
        fils1, fils2, estMute = mutation_k_flips(fils1,fils2,prob_mutation,3)
    elif (mutation == 3 ):
        # faire une mutation 5-flip
        fils1, fils2, estMute = mutation_k_flips(fils1,fils2,prob_mutation,5)
    elif (mutation == 4 ):
        # faire mutation bit flip
        fils1, fils2, estMute = mutation_bit_flip(fils1,fils2, prob_mutation)
    else : 
        print('valeur de mutation non reconnu')
    
    #Mettre a jour l'age des nouveaux fils si un croisement ou une mutation a été effectué
    fils1[-1]=0
    fils2[-1]=0
    print('---------------- THESE ARE CHILDREN --------------------------------')
    print(fils1)
    print(fils2)
    #fils1, fils2, estCrois = croiser_monopoint(parent1,parent2,1)

    #fils1, fils2, estCrois = croiser_uniforme(parent1,parent2,1)

    #fils1, fils2, estMute = mutation_bit_flip(parent1,parent2,1)

    #fils1, fils2, estMute = mutation_k_flips(parent1,parent2,1,3)

    # ====================== INSERTION ====================

    """
    insertion : mode d'insertion 
        0 : remplacer les individus les plus agés
        1 : remplacer les individus les plus mauvais # la valeur par defaut
    """
    if (estCrois or estMute):
        # mettre à jour la population
        if (insertion == 1):
            # insertion suivant la fitness (les plus mauvais)
            # Ordonner la population suivant l'avant derniere colonne (fitness)
            ind = np.argsort( population[:,tailleIndividu] *-1)
            population= population[ind]
            # supprimer les individus les plus mauvais 
            population=population[:-2]
            # Mettre a jour l'age de la population 
            population[:,-1]=population[:,-1]+1 

        elif (insertion == 0):
            # insertion suivant l'age (les plus agés)
            # Ordonner la population suivant la derniere colonne (age de l'individu)
            ind = np.argsort( population[:,tailleIndividu+1] *-1)
            population= population[ind]
            # supprimer les individus les plus mauvais par age
            population=population[:-2]
            # Mettre a jour l'age de la population 
            population[:,-1]=population[:,-1]+1
        else : 
            print('valeur de mutation non reconnu')

        # remplacer les individus supprimés par les nouveaux enfants 
        population = np.append(population,np.array([fils1,fils2]),axis=0) 
    else : 
        # ne rien faire (pas d'insertion de nouveaux individus)
        # Mettre a jour l'age de la population 
        population[:,-1]=population[:,-1]+1
    

    # ============================= INSERTION =======================


    print('---------------- THIS THE NEW POP --------------------------------')
    print(population)
    
    print('Finished')
    return 0



AG  ( taillePopulation =10 , tailleIndividu = 10, init = 1, selection = 2 , croisement = 0 , prob_croisement = 0, mutation = 4 , prob_mutation = 1 , insertion = 1 , nb_generation = 100)
"""
    taillePopulation : la taille de la population  # par defaut 100
    tailleIndividu : la taille de l'individu # par defaut 10 
    init : mode d'initialisation 
        0 : initialiser toute la population à zero
        1 : initialiser la population aléatoirement # la valeur par defaut
    selection : mode de selection
        0 : 2 meilleurs individus
        1 : 2 au hasard 
        2 : 2 meilleurs parmi 5 au hasard # la valeur par defaut
    croisement : type de croisement à effectuer 
        0 : ne pas effectuer croisement # la valeur par defaut
        1 : effectuer un croisement mono-point
        2 : effectuer un croisement uniforme
    prob_croisement : probabilité de croisement, valeurs réelles entre 0 et 1 # la valeur par defaut 0
    mutation :  type de mutation à effectuer 
        0 : ne pas effectuer croisement # la valeur par defaut 
        1 : 1-flip mutation
        2 : 3-flip mutation
        3 : 5-flip mutation 
        4 : bit flip mutation : changer chaque bit avec une probabilité de 1/n
    prob_mutation : probabilité de mutation, valeurs réelles entre 0 et 1 # la valeur par defaut 0
    insertion : mode d'insertion 
        0 : remplacer les individus les plus agés
        1 : remplacer les individus les plus mauvais # la valeur par defaut
    nb_generation : nombre de generation auquel on veut arreter l'algorithme génetique (critère d'arret) # la valeur par defaut 100
    sauvgarde : ....
    """