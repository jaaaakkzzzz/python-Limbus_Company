import random as rng
import menu
class recurso:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad

lunacy = recurso("lunacy", 0)
lunacy.cantidad = 1000

def gacha():
    print(" _____________________________________________________________________")
    print("| |lunacy: ",lunacy.cantidad,"|                                        ")
    print("|                                                                     |")
    print("|                                                                     |")
    print("|    ____________________________________________________________     |")
    print("|   |                                                             |   |")
    print("|   |  Cosas a obtener:                                           |   |")
    print("|   |  1.-caca                                                    |   |")
    print("|   |  2.-caja de caca                                            |   |")
    print("|   |                                                             |   |")
    print("|   |                                                             |   |")
    print("|   |                                                             |   |")
    print("|   |                                                             |   |")
    print("|   |                                                             |   |")
    print("|   |                                                             |   |")
    print("|   |                                                             |   |")
    print("|   |                                                             |   |")
    print("|   |                                                             |   |")
    print("|   |                                                             |   |")
    print("|   -_____________________________________________________________-   |")
    print("|                                                                     |")
    print("|    |extract x1|    |extract x10|  |menu|                            |")
    print("-_____________________________________________________________________-")

    extr_selec = str(input("selcciona"))
    if extr_selec == "menu" or "Menu":
        menu.menu()

caca_chance = rng.randint(1,10)