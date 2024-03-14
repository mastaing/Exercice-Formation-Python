import time




terminal_launched = True
terminal_name = "default"
user_command = ""
cpt = 0

while terminal_launched :

    user_command = input(f"[{terminal_name}]> ")

    if user_command == "run" :
        while cpt < 5:
            print(".")
            cpt += 1
            time.sleep(1)
        cpt = 0
    
    elif user_command == "name" :
        terminal_name = input(f"[{terminal_name}]> nouveau nom de terminal")

    elif user_command == "help" :
        print("\
--------------------\n\
LISTE DES COMMANDES :\n\
--------------------\n\
-run  : Run le programme\n\
-name : Changer le nom du terminal\n\
-help : Afficher la liste des commandes\n\
-quit : Quitter le programme\n ")

    elif user_command == "quit" :
        print(f"[{terminal_name}]> Fin du programme.")
        terminal_launched = False

    else :
        print(f"[{terminal_name}]> Commande incorect, écrivez help pour plus d'information. ")
