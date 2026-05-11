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
                muñeco_entrenamiento.HP = muñeco_entrenamiento.HP - (poder_base - muñeco_entrenamiento.DEF) //((poder_base - muñeco_entrenamiento.DEF) + 25) *100