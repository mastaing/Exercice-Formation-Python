"""
Module de calcul de périmètre, aire et volume de plusieurs formes géometriques : 

Périmetre d'un carré   : 4c / c+c+c+c
Aire d'un carré        : c*c / c**2
Volume d'un cube       : c**3
Périmètre d'un cercle  : 2πr
Aire d'un cercle       : πr**2
Volume d'un sphère     : (4πr**3)/3

"""

import geoshape

c = ""

r  = ""

perimetre_carre =""

aire_carre = ""

volume_cube = ""

perimetre_cercle = ""

aire_cercle = ""

volume_sphere = ""


#------------------------------------------------------------
#Calculs pour le Carré/Cube
#------------------------------------------------------------

def perimetre_carre(cote) : 
    return 4 * cote


def aire_carre(cote) :
    return cote * cote
    

def volume_cube(cote) :
    return cote**3


#------------------------------------------------------------
#Calculs pour le Cercle/Shpère
#------------------------------------------------------------

PI = 3.14

def perimetre_cercle(rayon) :
    return 2*PI*rayon

def aire_cercle(rayon) :
    return PI*rayon**2

def volume_sphere(rayon) :
    return 4*PI*rayon**3/3
    

if __name__ == '__main__' :
    
    print(f"\nLe périmètre est de: {perimetre_carre(2)} m²")

    print(f"\nL'aire du carré est de: {aire_carre(2)} m²")

    print(f"\nLe volumme du cube est de: {volume_cube(2)} m³")


    print(f"\nLe périmètre du cercle est de: {perimetre_cercle(3)} m²")

    print(f"\nL'aire du cercle est de: {aire_cercle(3)} m²")

    print(f"\nLe volume de la Sphère est de: {volume_sphere(3)} m³")
