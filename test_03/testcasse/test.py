
# class Game:
#     def __init__(self,hp,power):
#         self.hp=hp
#         self.power=power
#     def figth(self,enomy_hp,enomy_power):
#         final_hp = self.hp-enomy_power
#         enomy_final_hp = enomy_hp-self.power
#         if final_hp>enomy_final_hp:
#             print("我赢了")
#         elif final_hp<enomy_final_hp:
#             print("敌人赢了")
#         else:
#             print("平局")
# hp=1000
# power=200
# game=Game(hp,power)
# game.figth(1000,200)

# class HouYi(Game):
#     def __init__(self,defense):
#         super().__init__(1000,200)
#         self.defense=defense
#     def houyi_figth(self,enomy_power,enomy_hp):
#         final_hp = self.hp+self.defense-enomy_power
#         enomy_final_hp = enomy_hp-self.power
#         if final_hp>enomy_final_hp:
#             print("我赢了")
#         elif final_hp<enomy_final_hp:
#             print("敌人赢了")
#         else:
#             print("平局")
# hp=1000
# power=200
# defense=100
# game=Game(hp,power)
# game.figth(1000,200)
#
# houyi = HouYi(defense)
# houyi.houyi_figth(hp,power)
import os

print(os.path.join('..' + 'test.py'))