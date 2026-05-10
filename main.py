import tkinter as gui
import prueba_import

print("bienvenido a limbus python, este es un  fanmade hecho con python al 100%, estamos recien creando todo")
print("escoge una opcion:" \
      "1.-Escoger sinners" \
      "2.-drive" \
      "3.-o ver patch notes" \
      "(escoges 1,2 o 3)")
menu_isi = int(input(":"))

if menu_isi == 1:
    print("Aun no tenemos sinners, upsie upsie." \
          "Proximamente, previsto para la 1.3.7.")
elif menu_isi == 2:
    print("Proximamente prologo, previsto para la versión 1.3.0." \
          "En la 1.0 solo tendremos un combate")
elif menu_isi == 3:
    print("notas de versión 0.0.1:")
    print("No hay notas aun, pero aqui algunas cosas a tener en cuenta")
    print("1.-se ha iniciado el projecto, aun sin GUI.")
    print("2.-las piezas de codigo se iran subiendo de a pedazos para su testeo, posteriori entrarán en main,")
    print("   o en caso de que se puedan conectar archivos de python entre sí, se notificara via github.")
    print("3.-este es un projecto de fans, nada que esté aqui deberia tomarse como canon en el universo de P.M.")
    print("4.-todos los derechos son de project moon, no mios.")
    print("5.-sigan mi pagina de github, para que no se pierdan las actualizaciones del projecto")
    
else:
    print(f"no existe la opción{menu_isi}")


ejecutar_prueba = input("yes?")
if ejecutar_prueba == "y":
    prueba_import.mensaje()