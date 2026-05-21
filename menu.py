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
        print("  |Config| |Account| |Messages| |Patch notes|  ")
        print("  ___________________________________________  ")
        print(" |----(                          )-----------| ")
        print(" |----(   Limbus                 )-----------| ")
        print(" |----(   Company                )-----------| ")
        print(" |----(                          )-----------| ")
        print(" |----(    Python                )-----------| ")
        print(" |----(    Edition     :D        )-----------| ")
        print(" _____(__________________________)___________| ")
        print("   |Sinners| |Drive| |Extraction| |Dispense|   ")
        print("                                               ")
        print("                                               ")

        selecMenu = str(input("escoge a donde ir: "))
        if selecMenu == "config" or "Config":
            config()
        elif selecMenu == "account" or "Account":
            account()
        elif selecMenu == "messages" or "Messages":
            messages()
        elif selecMenu == "patch notes" or "Patch notes":
            patchNotes()
        elif selecMenu == "sinners" or "Sinners":
            sinners()
        elif selecMenu == "drive" or "Drive":
            drive()
        elif selecMenu == "extraction" or "Extraction":
            extraction()
        elif selecMenu == "dispense" or "Dispense":
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

    drive_select = str(input("selecciona opción o /volver/ para volver al menú"))

    if drive_select == "battle test" or "Battle test":
        BtlT.batalla()
    elif drive_select == "cantos" or "Cantos":
        print("aun no hay")
        drive()
    elif drive_select == "volver" or "Volver":
        menu()

def extraction():
    gacha.gacha()

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
    if goback == "y" or "Y":
        menu()

menu()