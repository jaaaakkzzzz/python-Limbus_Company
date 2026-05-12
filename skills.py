import random
import enemigos
def golpe():
        poder_base = 50
        clash_power_Jskill1 = 4
        coin_powerJskill1 = 3
        print(clash_power_Jskill1)

        coin_1 = random.randit(0,1)
        if coin_1 == 1:
                print("HEADS")
                poder_base = poder_base + 5
                print(clash_power_Jskill1 + coin_powerJskill1)
                enemigos.enemigo.hp = enemigos.enemigo.hp