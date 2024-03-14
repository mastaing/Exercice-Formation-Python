
print("\n\tBienvenue dans le combat des TITANS\n\
\nDeux joueur s'affronte dans un combat singulier !\n\
Les deux combattants démarrent avec 250 points de vie chacun\n\
Le combat se déroule en 4 attaques, chaque joueur peut attaquer deux fois chacun leurs tours.\n\
Celui qui a le plus de point de vie à la fin de la partie remporte le combat!\n\
\n\tBonne Chance joueur!")

import random

random_attack = True # True = face / False = pile
random_damage = 0

joueur1_name = ""
joueur1_hp = 250

joueur2_name = ""
joueur2_hp = 250

joueur1_name = input("Premier joueur, choisissez un pseudo : ")
print(f"{joueur1_name} est le Joueur 1")

joueur2_name = input("Second joueur, choisissez un pseudo : ")
print(f"{joueur2_name} est le Joueur 2")

input()

print("\nLE COMBAT COMMENCE ! \n")

#-----------------------------------------------------------------------------------------------------------------------
# 1ère attaque
print(f"{joueur1_name} : {joueur1_hp} PV  , {joueur2_name} : {joueur2_hp} PV ")
print(f"\n{joueur1_name} attaque {joueur2_name}")

random_attack = random.randint(0, 1)
random_attack = bool(random_attack)
 
if random_attack:
    # Si l'attaque réussit
    random_damage = random.randint(20, 100)
    joueur2_hp -= random_damage

    print(f"\nL'attaque de {joueur1_name} à réussi")
    print(f"\n{joueur2_name} prend {random_damage} de dégats {joueur2_name} n'a plus que {joueur2_hp} point de vie !\n")
else:
    # Si l'attaque échoue
    print(f"\nL'attaque de {joueur1_name} à échouer ...\n")
#-----------------------------------------------------------------------------------------------------------------------

input()

# 2ème attaque
print(f"{joueur1_name} : {joueur1_hp} PV  , {joueur2_name} : {joueur2_hp} PV ")
print(f"\n{joueur2_name} attaque {joueur1_name}")

random_attack = random.randint(0, 1)
random_attack = bool(random_attack)

if random_attack:
    # Si l'attaque réussit
    random_damage = random.randint(20, 100)
    joueur1_hp -= random_damage

    print(f"\nL'attaque de {joueur2_name} à réussi")
    print(f"\n{joueur1_name} prend {random_damage} de dégats {joueur1_name} n'a plus que {joueur1_hp} point de vie !\n")
else:
    # Si l'attaque échoue
    print(f"\nL'attaque de {joueur2_name} à échouer ...\n")

#-----------------------------------------------------------------------------------------------------------------------

input()

# 3ème attaque
print(f"{joueur1_name} : {joueur1_hp} PV  , {joueur2_name} : {joueur2_hp} PV ")
print(f"\n{joueur1_name} attaque {joueur2_name}")

random_attack = random.randint(0, 1)
random_attack = bool(random_attack)

if random_attack:
    # Si l'attaque réussit
    random_damage = random.randint(20, 100)
    joueur2_hp -= random_damage

    print(f"\nL'attaque de {joueur1_name} à réussi")
    print(f"\n{joueur2_name} prend {random_damage} de dégats {joueur2_name} n'a plus que {joueur2_hp} point de vie !\n")
else:
    # Si l'attaque échoue
    print(f"\nL'attaque de {joueur1_name} à échouer ...\n")

#-----------------------------------------------------------------------------------------------------------------------

input()

# 4ème attaque
print(f"{joueur1_name} : {joueur1_hp} PV  , {joueur2_name} : {joueur2_hp} PV ")
print(f"\n{joueur2_name} attaque {joueur1_name}")

random_attack = random.randint(0, 1)
random_attack = bool(random_attack)

if random_attack:
    # Si l'attaque réussit
    random_damage = random.randint(20, 100)
    joueur1_hp -= random_damage

    print(f"\nL'attaque de {joueur2_name} à réussi")
    print(f"\n{joueur1_name} prend {random_damage} de dégats {joueur1_name} n'a plus que {joueur1_hp} point de vie !\n")
else:
    # Si l'attaque échoue
    print(f"\nL'attaque de {joueur2_name} à échouer ...\n")

#-----------------------------------------------------------------------------------------------------------------------

input()

# Résultat final
print("\nFIN DU COMBAT !\n")
print(f"{joueur1_name} : {joueur1_hp} PV  , {joueur2_name} : {joueur2_hp} PV ")
if joueur1_hp > joueur2_hp :
    print(f"{joueur1_name} a gagner le combat !")

elif joueur1_hp < joueur2_hp :
    print(f"{joueur2_name} a gagner le combat !")

else :
    print("Match nul !")