from zombie import Zombie
from user import User
import random


class Game:
    name = "植物大战僵尸"

    @classmethod
    def start(cls):
        print("欢迎来到%s的世界" % cls.name)
        targets_lst = [Zombie(random.choice(['普通僵尸', '路障僵尸', '铁桶僵尸'])) for i in range(3)]
        user1 = User("jeff")

        count = 0
        while len(targets_lst) != 0:
            target = targets_lst.pop(0)
            print("开始击杀第%s只僵尸" % str(count + 1))
            while 1:
                res = user1.beat(target)
                if res:
                    break
            print("已击杀第%s只僵尸" % str(count + 1))
            count += 1


starter = Game()
starter.start()
