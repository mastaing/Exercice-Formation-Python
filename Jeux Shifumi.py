import random
 



def tirage_ordi ():

    # choix aléatoire entre pierre, papier et ciseau
    
    return random.choice(["pierre", "papier", "ciseau"])


def tirage_joueur ():

    # choix du joueur

    while True :
        tirage = input ("faite votre choix entre pierre, papier ou ciseau !") 
        if tirage in ['pierre', 'papier', 'ciseau']:
            return tirage 
        
        print("Comande inconnue, choisisez entre pierre, papier ou ciseau !")

def determine_gagnant (tirage_joueur,tirage_ordi) :

    # Résultat du jeu

    if tirage_joueur == tirage_ordi :
        return "Égalité!"

    elif (tirage_joueur == 'pierre' and tirage_ordi == 'ciseau' ) or (tirage_joueur == 'papier' and tirage_ordi == 'pierre' ) or (tirage_joueur == 'ciseau' and tirage_ordi == 'papier' ) : 
        return "Vous avez gagné!"

    else :
        return "Vous avez Perdu!"


def principale():
    print ("Une partie de Shifumi va commencer !")

    while True :

        tirage_joueur_val = tirage_joueur()
        tirage_ordi_val   = tirage_ordi()
         
        print(f"Vous avez choisi: {tirage_joueur_val}")
        print(f"L'ordinateur a choisi: {tirage_ordi_val}")

        resultat = determine_gagnant(tirage_joueur_val,tirage_ordi_val)
        print(resultat)

        continuer = input("voulez vous continuer ? (oui/non)").lower()
        
        if continuer != 'oui':
            print("Merci d'avoir jouer")
            break
        




    









#PROGRAMME PRINCIPALE
tirage_joueur()

tirage_ordi()
print(tirage_ordi())

resultat (tirage_joueur,tirage_ordi)

