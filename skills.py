import random
import enemigos
import estados
def golpe():
        poder_base = 50
        clash_power_Jskill1 = 4
        coin_powerJskill1 = 3
        print(clash_power_Jskill1)

        coin_1 = random.randit(0,1)
        if coin_1 == 1:
                print("HEADS")
                print("<-H->")
                poder_base = poder_base + 5
                print(clash_power_Jskill1 + coin_powerJskill1)
                enemigos.enemigo.hp = enemigos.enemigo.hp - (poder_base - enemigos.enemigo.defensa) / (abs(poder_base - enemigos.enemigo.defensa)+25)*100
                print ("has hecho: ",enemigos.enemigo.hp,". de daño")
                print("has infligido burn (1 count- 1 potency)")
                enemigos.enemigo.estados = enemigos.enemigo.estados + estados.burn
        else:
                print("TAILS")
                print("<-T->")
                poder_base = poder_base - 10
                print(clash_power_Jskill1 - 2)
                enemigos.enemigo.hp = enemigos.enemigo.hp - ((poder_base - enemigos.enemigo.defensa) / (abs(poder_base - enemigos.enemigo.defensa)+25)*100) - 10
                print("has hecho: ",enemigos.enemigo.hp,". de daño")

