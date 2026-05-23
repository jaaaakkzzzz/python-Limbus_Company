import datos_cuenta as cuenta
import BattleTest as BtlT
import extraction as gacha

def plantilla ():
    print(" ______________________________________")
    print("|                                      |")
    print("|                                      |")
    print("|                                      |")
    print("|                                      |")
    print("|                                      |")
    print("|                                      |")
    print("|                                      |")
    print("|                                      |")
    print("|                                      |")
    print("|                                      |")
    print("-______________________________________-")




def menu():
        print("  |1.Config| |2.Account| |3.Messages| |4.Patch notes|  ")
        print("  _____________________________________________________")
        print(" |----(                          )--------------------|")
        print(" |----(   Limbus                 )--------------------| ")
        print(" |----(   Company                )--------------------| ")
        print(" |----(                          )--------------------| ")
        print(" |----(    Python                )--------------------| ")
        print(" |----(    Edition     :D        )--------------------| ")
        print(" _____(__________________________)____________________| ")
        print("   |5.Sinners| |6.Drive| |7.Extraction| |8.Dispense|   ")
        print("                                               ")
        print("                                               ")

        selecMenu = int(input("escoge a donde ir: "))
        if selecMenu == 1:
            config()
        elif selecMenu == 2:
            account()
        elif selecMenu == 3:
            messages()
        elif selecMenu == 4:
            patchNotes()
        elif selecMenu == 5:
            sinners()
        elif selecMenu == 6:
            drive()
        elif selecMenu == 7:
            gacha.gacha()
        elif selecMenu == 8:
            dispense()

def config():
    print(" ______________________________________")
    print("|                                      |")
    print("|                                      |")
    print("|                                      |")
    print("|      no config yet                   |")
    print("|                                      |")
    print("|      :(                              |")
    print("|                                      |")
    print("|                                      |")
    print("|                                      |")
    print("|                                      |")
    print("-______________________________________-")

    volver = str(input("volver al ,menu?(  (y) para volver  ): "))
    if volver == "y":
        menu() 

def account():
    print(" ______________________________________")
    print("|                                      |")
    print("|                                      |")
    print("|nombre usuario:",cuenta.nombreUsuario,)
    print("|id usuario: ",cuenta.idUsuario,"      ")
    print("|codigo amigo: ",cuenta.codigoAmigo,"  ")
    print("|                                      |")
    print("|                                      |")
    print("|                                      |")
    print("|                                      |")
    print("|                                      |")
    print("|                                      |")
    print("-______________________________________-")

def messages():
    print(" ______________________________________")
    print("|                                      |")
    print("|                                      |")
    print("|                                      |")
    print("|      no messages found               |")
    print("|                                      |")
    print("|      or friends  :(                  |")
    print("|                                      |")
    print("|                                      |")
    print("|                                      |")
    print("|                                      |")
    print("-______________________________________-")

    volver = str(input("volver al ,menu?(  (y) para volver  ): "))
    if volver == "y":
        menu() 

def patchNotes():
    print(" ______________________________________")
    print("|1.-notas 0.0.0.1                      |")
    print("|2.-notas de prueba                    |")
    print("|                                      |")
    print("|                                      |")
    print("|                                      |")
    print("|                                      |")
    print("|                                      |")
    print("|                                      |")
    print("|                                      |")
    print("|                                      |")
    print("-______________________________________-")
    abrirNota = int(input("que nota quieres abrir?(escribe 1, 2 para seleccionar)"))
    if abrirNota == 1:
        print("0.0.0.1 patch notes:")
        print("nada (aun)")

    elif abrirNota == 2:
        print("esto de prueba nomas")
    volver = str(input("volver al ,menu?(  (y) para volver  ) o (n) para solo volver a patch notes: "))
    if volver == "y":
        menu() 
    elif volver == "n":
        patchNotes()

def sinners():
    print(" _________________________________________________________________________________")
    print("| 1.jhonnathan                                                                    |")
    print("|                                                                                 |")
    print("|                                                                                 |")
    print("|                                                                                 |")
    print("|                                                                                 |")
    print("|                                                                                 |")
    print("|                                                                                 |")
    print("|                                                                                 |")
    print("|                                                                                 |")
    print("|                                                                                 |")
    print("-________________________________________________________________________________-")


def drive():
    print(" ______________________________________")
    print("| 1.Battle test                        |")
    print("| 2.Cantos                             |")
    print("|                                      |")
    print("|                                      |")
    print("|                                      |")
    print("|                                      |")
    print("|                                      |")
    print("|                                      |")
    print("|                                      |")
    print("|                                      |")
    print("-______________________________________-")

    drive_select = int(input("selecciona opción o /67/ para volver al menú: "))

    if drive_select == 1:
        BtlT.batalla()
    elif drive_select == 2:
        print("aun no hay")
        drive()
    elif drive_select == 67:
        menu()


def dispense():
    print(" ______________________________________")
    print("|                                      |")
    print("|      not yet                         |")
    print("|                                      |")
    print("|                                      |")
    print("|                                      |")
    print("|                                      |")
    print("|                                      |")
    print("|                                      |")
    print("|                                      |")
    print("|                                      |")
    print("-______________________________________-")
    goback = str(input("ir al menu?  (y)"))
    if goback == "y":
        menu()

menu()