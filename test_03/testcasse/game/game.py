
class Game:
    def __init__(self,hp,power):
        self.hp=hp
        self.power=power
    def figth(self,enomy_hp,enomy_power):
        final_hp = self.hp-enomy_power
        enomy_final_hp = enomy_hp-self.power
        if final_hp>enomy_final_hp:
            print("我赢了")
        elif final_hp<enomy_final_hp:
            print("敌人赢了")
        else:
            print("平局")