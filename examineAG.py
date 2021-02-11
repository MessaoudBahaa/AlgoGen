import AlgoGen as algogen
import numpy as np
import matplotlib.pyplot as plt 

#out = algogen.AG  (taillePopulation =20 , tailleIndividu = 100, init = 1, selection = 2 , croisement = 2 , prob_croisement = 0.5, mutation = 2 , prob_mutation = 0.5 , insertion = 1 , nb_generation = 1000, print_log = 0, save = 0 ,plot=0, nom_fichier= "resultat" )
#print(out)
def examine_taillePop():
    X,Y = [], []
    for taille in range(5,100) :
        out = algogen.AG  (taillePopulation =taille , tailleIndividu = 100, init = 0, selection = 2 , croisement = 2 , prob_croisement = 0.5, mutation = 4 , prob_mutation = 0.5 , insertion = 1 , nb_generation = 1000, print_log = 0, save = 0 ,plot=0, nom_fichier= "resultat" )
        X.append(taille)
        Y.append(out[1].pop())
    plt.plot(X,Y)
    plt.xlabel("taille de population")
    plt.ylabel("fitness de meilleurs individu")
    plt.savefig("autre.png")
    plt.show()
    return 0
def examine_taillePop_():
    for taille in range(10,300,50):
        its,bests = algogen.AG  (taillePopulation =taille , tailleIndividu = 1000,\
                            init = 1, selection = 2 , croisement = 2 , prob_croisement = 0.5, \
                            mutation = 4 , prob_mutation = 0.5 , insertion = 0 , \
                            nb_generation = 10000, print_log = 0, save = 0 ,plot=0, nom_fichier= "resultat" )
       
        plt.plot(its,bests, label=str(taille))
    plt.legend()
    plt.show()
    return 0

def examine_prob_croisement():
    pc = 0.1
    for i in range(1,10,2):
        
        its,bests = algogen.AG  (taillePopulation =20 , tailleIndividu = 1000,\
                            init = 1, selection = 2 , croisement = 2 , prob_croisement = pc, \
                            mutation = 4 , prob_mutation = 0.5 , insertion = 0 , \
                            nb_generation = 10000, print_log = 0, save = 0 ,plot=0, nom_fichier= "resultat" )
       
        plt.plot(its,bests, label=str(round(pc,1)) )
        pc = pc + 0.2
    plt.legend()
    plt.show()
    return 0

def examine_prob_mutation():
    pm = 0.1
    for i in range(1,10,2):
        
        its,bests = algogen.AG  (taillePopulation =20 , tailleIndividu = 1000,\
                            init = 1, selection = 2 , croisement = 2 , prob_croisement = 0.5, \
                            mutation = 4 , prob_mutation = pm , insertion = 0 , \
                            nb_generation = 10000, print_log = 0, save = 0 ,plot=0, nom_fichier= "resultat" )
       
        plt.plot(its,bests, label=str(round(pm,1)) )
        pm = pm + 0.2
    plt.legend()
    plt.show()
    return 0


def examine_croisement(k):
    its,meanbests_mono = algogen.AG  (taillePopulation =20 , tailleIndividu = 200,\
                            init = 1, selection = 2 , croisement = 1 , prob_croisement = 0.5, \
                            mutation = 0 , prob_mutation = 0.5 , insertion = 0 , \
                            nb_generation = 2000, print_log = 0, save = 0 ,plot=0, nom_fichier= "resultat" )
    newbests_mono = meanbests_mono
    for i in range(1,k):
        meanbests_mono = (np.array(meanbests_mono)+np.array(newbests_mono) )/2
        its,newbests_mono = algogen.AG  (taillePopulation =20 , tailleIndividu = 200,\
                            init = 1, selection = 2 , croisement = 1 , prob_croisement = 0.5, \
                            mutation = 0 , prob_mutation = 0.5 , insertion = 0 , \
                            nb_generation = 2000, print_log = 0, save = 0 ,plot=0, nom_fichier= "resultat" )

    its,meanbests_uni = algogen.AG  (taillePopulation =20 , tailleIndividu = 200,\
                            init = 1, selection = 2 , croisement = 2 , prob_croisement = 0.5, \
                            mutation = 0 , prob_mutation = 0.5 , insertion = 0 , \
                            nb_generation = 2000, print_log = 0, save = 0 ,plot=0, nom_fichier= "resultat" )
    newbests_uni = meanbests_uni
    for i in range(1,k):
        meanbests_uni = (np.array(meanbests_uni)+np.array(newbests_uni) )/2
        its,newbests = algogen.AG  (taillePopulation =20 , tailleIndividu = 200,\
                            init = 1, selection = 2 , croisement = 2 , prob_croisement = 0.5, \
                            mutation = 0 , prob_mutation = 0.5 , insertion = 0 , \
                            nb_generation = 2000, print_log = 0, save = 0 ,plot=0, nom_fichier= "resultat" )
    plt.plot(its,meanbests_mono, label ="Mono-point")
    plt.plot(its,meanbests_uni, label = "Uniforme")
    plt.legend()
    plt.show()
    return 0
def examine_mutation(k):
    # 1 flip
    its,meanbests_1f = algogen.AG  (taillePopulation =20 , tailleIndividu = 200,\
                            init = 1, selection = 2 , croisement = 0 , prob_croisement = 0, \
                            mutation = 1 , prob_mutation = 0.5 , insertion = 0 , \
                            nb_generation = 2000, print_log = 0, save = 0 ,plot=0, nom_fichier= "resultat" )
    newbests_1f = meanbests_1f
    for i in range(1,k):
        meanbests_1f = (np.array(meanbests_1f)+np.array(newbests_1f) )/2
        its,newbests_1f = algogen.AG  (taillePopulation =20 , tailleIndividu = 200,\
                            init = 1, selection = 2 , croisement = 0 , prob_croisement = 0, \
                            mutation = 1 , prob_mutation = 0.5 , insertion = 0 , \
                            nb_generation = 2000, print_log = 0, save = 0 ,plot=0, nom_fichier= "resultat" )

    # 3flip test
    its,meanbests_3f = algogen.AG  (taillePopulation =20 , tailleIndividu = 200,\
                            init = 1, selection = 2 , croisement = 0 , prob_croisement = 0, \
                            mutation = 2 , prob_mutation = 0.5 , insertion = 0 , \
                            nb_generation = 2000, print_log = 0, save = 0 ,plot=0, nom_fichier= "resultat" )
    newbests_3f = meanbests_3f
    for i in range(1,k):
        meanbests_3f = (np.array(meanbests_3f)+np.array(newbests_3f) )/2
        its,newbests_3f = algogen.AG  (taillePopulation =20 , tailleIndividu = 200,\
                            init = 1, selection = 2 , croisement = 0 , prob_croisement = 0, \
                            mutation = 2 , prob_mutation = 0.5 , insertion = 0 , \
                            nb_generation = 2000, print_log = 0, save = 0 ,plot=0, nom_fichier= "resultat" )
    
    # 5 flip
    its,meanbests_5f = algogen.AG  (taillePopulation =20 , tailleIndividu = 200,\
                            init = 1, selection = 2 , croisement = 0 , prob_croisement = 0, \
                            mutation = 3 , prob_mutation = 0.5 , insertion = 0 , \
                            nb_generation = 2000, print_log = 0, save = 0 ,plot=0, nom_fichier= "resultat" )
    newbests_5f = meanbests_5f
    for i in range(1,k):
        meanbests_5f = (np.array(meanbests_5f)+np.array(newbests_5f) )/2
        its,newbests_5f = algogen.AG  (taillePopulation =20 , tailleIndividu = 200,\
                            init = 1, selection = 2 , croisement = 0 , prob_croisement = 0, \
                            mutation = 3 , prob_mutation = 0.5 , insertion = 0 , \
                            nb_generation = 2000, print_log = 0, save = 0 ,plot=0, nom_fichier= "resultat" )

     # bit flip
    its,meanbests_bf = algogen.AG  (taillePopulation =20 , tailleIndividu = 200,\
                            init = 1, selection = 2 , croisement = 0 , prob_croisement = 0, \
                            mutation = 4 , prob_mutation = 0.5 , insertion = 0 , \
                            nb_generation = 2000, print_log = 0, save = 0 ,plot=0, nom_fichier= "resultat" )
    newbests_bf = meanbests_bf
    for i in range(1,k):
        meanbests_bf = (np.array(meanbests_bf)+np.array(newbests_bf) )/2
        its,newbests_bf = algogen.AG  (taillePopulation =20 , tailleIndividu = 200,\
                            init = 1, selection = 2 , croisement = 0 , prob_croisement = 0, \
                            mutation = 4 , prob_mutation = 0.5 , insertion = 0 , \
                            nb_generation = 2000, print_log = 0, save = 0 ,plot=0, nom_fichier= "resultat" )
    its = range(1,2000)
    plt.plot(its,meanbests_1f, label ="1-flip")
    plt.plot(its,meanbests_3f, label ="3-flip")
    plt.plot(its,meanbests_5f, label ="5-flip")
    plt.plot(its,meanbests_bf, label ="bit-flip")
    plt.legend()
    plt.show()
    return 0

def examine_mutation_():
    # 1 flip
    its1,meanbests_1f = algogen.AG  (taillePopulation =20 , tailleIndividu = 1000,\
                            init = 1, selection = 2 , croisement = 0 , prob_croisement = 0, \
                            mutation = 1 , prob_mutation = 0.5 , insertion = 0 , \
                            nb_generation = 10000, print_log = 0, save = 0 ,plot=0, nom_fichier= "resultat" )
 

    # 3flip test
    its3,meanbests_3f = algogen.AG  (taillePopulation =20 , tailleIndividu = 1000,\
                            init = 1, selection = 2 , croisement = 0 , prob_croisement = 0, \
                            mutation = 2 , prob_mutation = 0.5 , insertion = 0 , \
                            nb_generation = 10000, print_log = 0, save = 0 ,plot=0, nom_fichier= "resultat" )
    
    
    # 5 flip
    its5,meanbests_5f = algogen.AG  (taillePopulation =20 , tailleIndividu = 1000,\
                            init = 1, selection = 2 , croisement = 0 , prob_croisement = 0, \
                            mutation = 3 , prob_mutation = 0.5 , insertion = 0 , \
                            nb_generation = 10000, print_log = 0, save = 0 ,plot=0, nom_fichier= "resultat" )
    
   
     # bit flip
    itsb,meanbests_bf = algogen.AG  (taillePopulation =20 , tailleIndividu = 1000,\
                            init = 1, selection = 2 , croisement = 0 , prob_croisement = 0, \
                            mutation = 4 , prob_mutation = 0.5 , insertion = 0 , \
                            nb_generation = 10000, print_log = 0, save = 0 ,plot=0, nom_fichier= "resultat" )
    
    plt.plot(its1,meanbests_1f, label ="1-flip")
    plt.plot(its3,meanbests_3f, label ="3-flip")
    plt.plot(its5,meanbests_5f, label ="5-flip")
    plt.plot(itsb,meanbests_bf, label ="bit-flip")
    plt.legend()
    plt.show()
    return 0
                     

#examine_croisement(20)
#examine_taillePop_()
#examine_prob_croisement()
examine_prob_mutation()
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
    print_log : afficher ou non le log de l'execution 
        0 : ne pas afficher
        1 : afficher
    save : sauvegarder ou pas l'hitorique des iterations
        0 : ne pas sauvgarder
        1 : sauvgarder # la valeur par defaut 
    plot : tracer le graphe des iterations en fonction de meilleur individu
        0 : ne pas tracer le graphe
        1 : tracer le graphe
    nom_fichier : string contenant le nom du fichier de données nom_fichier".txt" et le nom de graph nom_fichier".png" # la valeur par defaut "data"
 
    """