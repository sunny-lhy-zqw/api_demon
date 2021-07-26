from test_03.testcasse.game.game import Game
class HouYi(Game):
    def __init__(self,defense):
        super().__init__(1000,200)
        self.defense=defense
    def houyi_figth(self,enomy_power,enomy_hp):
        while True:
            self.final_hp = self.hp + self.defense - enomy_power
            enomy_hp = enomy_hp - self.power
            if self.final_hp <=0:
                print("敌人赢了")
                break
            elif enomy_hp <= 0:
                print("我赢了")
                break

hp=1000
power=200
defense=100
# game=Game(hp,power)
# game.figth(1000,200)

houyi = HouYi(defense)
houyi.houyi_figth(hp,power)