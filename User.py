import time


class User:
    def __init__(self, name):
        self.name = name

    def beat(self, cls):
        attack = 25
        while cls.hp > 0:
            real_attack = attack - cls.armor_count
            cls.hp -= real_attack
            print("造成伤害%s" % real_attack)
            time.sleep(3)
        print("%s用户击杀了%s" % (self.name, cls.name))
