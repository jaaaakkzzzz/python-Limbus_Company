class enemigo:
    def __init__(self,nombre,nivel,tipo,defensa,Mhp,hp,Msp,sp,skill1,skill2,skill3,skillDef,pasiva):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.defensa = defensa
        self.Mhp = Mhp
        self.hp = hp
        self.Msp = Msp
        self.sp = sp
        self.skill1 = skill1
        self.skill2 = skill2
        self.skill3 = skill3
        self.skillDef = skillDef
        self.pasiva = pasiva

dummy = enemigo('dummie', 1, 'abnormalidad machina',  60, 120, 120, 0, 0, '¿nada?', '¿algo?', 'embestidas', 'evade:apuntaste mal', 'em, esta mal')