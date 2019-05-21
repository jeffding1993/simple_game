class Zombie:

    def __init__(self, name):
        armor_list = ["无", 0, "路障", 5, "铁桶", 15]
        self.name = name
        self.hp = 100
        if self.name[:2] == "普通":
            self.__armor = armor_list[0]
        if self.name[:2] == "路障":
            self.__armor = armor_list[2]
        if self.name[:2] == "铁桶":
            self.__armor = armor_list[4]

    @property
    def armor_name(self):
        return self.__armor

    @armor_name.setter
    def armor_name(self, new_name):
        self.__armor = new_name
        self.name = new_name + "僵尸"

    @property
    def armor_count(self):
        armor_list = ["无", 0, "路障", 5, "铁桶", 15]
        for i, v in enumerate(armor_list):
            if self.__armor == v:
                return armor_list[i + 1]

# z1 = Zombie("普通僵尸")
# z1.armor_name = "铁桶"
# print(z1.armor_name)
# print(z1.armor_count)
# print(z1.name)
