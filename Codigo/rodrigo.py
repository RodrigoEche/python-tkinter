#pag 394
import sys
print(sys.path)

import platform as plataforma
print("Sistema operativo ---> "+plataforma.system())

#pag 398
#https://pypi.org/project/tabulate/
from tabulate import tabulate
print(tabulate([["Nombre","Edad"],["Rodrigo",51],["Yanina",47]],    headers="firstrow"))
print("   ")
print(tabulate( [["Mascota","Nombre","Raza"],["Perro","Pancha","Galgo"],
                ["Gato","Violeta","Negrus"],["Gato","Michin","Salvagius"]],   
                 headers="firstrow",  tablefmt="grid"))