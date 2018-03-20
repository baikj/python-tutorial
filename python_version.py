# faire un import de sys
# mettre sys.version_info dans une variable
# aficher le resultat dans une chaine de caracteres
# attention a utiliser str() et les acces par un tableau d'indices dans une liste

import sys

info = sys.version_info
version = ".".join(str(x) for x in info)

#print('This is python version ' + str(info[0]) + '.' + str(info[1]) + '.' + str(info[2]) + ' ' + str(info[3]) + ' ' + str(info[4]))

print('This is python ' + version)