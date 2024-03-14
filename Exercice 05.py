import copy



people = ["Laura", "Camille", "Bryan", "Josh", "Amélia", "Kamel" ,"Nami", "Clint", "Mike", "Samira", "Jean-Charles","Quentin", "Ben", "Marie", "Françoise", "Jordana", "Farid"]


element = ""
position = ""

def get_lenght() :
    print(f"Il y a {len(people)} élement dans la liste")



def get_position():
    position = people.index(element) + 1
    print(f"{element} est en {position}éme postion !")


    
    


# Programme Principale

print(people[:])         # Affichage de la Liste

people.sort()            # Trie par ordre alphabétique

print(people[:])         # Affichage de la Liste

get_lenght()             # Affiche le nombre d'elements dans ma liste

element = "Bryan"       

get_position()           # afficher la position de Bryan

for name in people :
    if name[0] == "J" :
        people.remove(name)
        
for name in people :
    if name[0] == "J" :
        people.remove(name)

print(people[:])

for i in range(len(people)) :
    if people[i] == "Mike" :
        people[i] = "Michel"


print(people[:])

people.append("Henri")
people.append("Bryan Junior")
people.append("Kumiko")

print(people[:])

new_list = []

for name in people :
    if len(name) > 5 :
        new_list.append(name)


print(new_list[:])



