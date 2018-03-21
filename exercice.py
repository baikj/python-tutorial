# creer une liste vide   mylist = []
# for une boucle for de range(5)
# entrer des valeurs au clavier avec la fonction input()
# attention a convertir les donnees en entier
# faire un tri
# afficher la liste

mylist = []

for i in range(5):
    mylist.append(int(input("enter your number: ")))
mylist.sort()

print(mylist)

# liste comprehension est utile mais attention a la memoire
# il faut un generator pour optimiser la memoire
# sorted() est pour trier les valeurs d un iterable
# sort() pour trier les lists

# tuple est immuable
T = (1, 2, 3, 4, 5)
len(T)

T += T + (5, 6)

T.index(1)

