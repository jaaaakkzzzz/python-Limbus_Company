import skills
import pasivas
#creamos la clase personaje
class pj:
    def __init__(self,nombre,nivel,MHp,HP,MSp,SP,DEF,velocidad,skill1,skill2,skill3,skill_def,in_battle_pasivas,support_pasivas):
        self.nombre = nombre
        self.nivel = nivel
        self.nivel = nivel
        self.MHp = MHp
        self.HP = HP
        self.MSp = MSp
        self.SP = SP
        self.DEF = DEF
        self.velocidad = velocidad
        self.skill1 = skill1
        self.skill2 = skill2
        self.skill3 = skill3
        self.skill_def = skill_def
        self.in_battle_pasivas = in_battle_pasivas
        self.support_pasivas = support_pasivas

#creamos un personaje y todo lo que conlleva

jhonny = pj('jhonathan', 1, 100, 100, 45, 0, 5, 'golpe', 'patada', 'ráfaga', 'bloqueo', 'oh, nada?', 'apollo moral')