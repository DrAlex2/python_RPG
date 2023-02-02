import random


class Player:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.lvl = 1
        self.exp = 0
    def create_hero(name, race, prof):
        name = name
        hp = 0
        damage = 0
        if race == races[0]:
            hp += 100
            damage += 85
        elif race == races[1]:
            hp += 150
            damage += 60
        elif race == races[2]:
            hp += 100
            damage += 75
        elif race == races[3]:
            hp += 85
            damage += 100
        else:
            print("Такой расы не существует")
            hp = 0
            damage = 0

        if prof == prof_list[0]:
            hp -= 5
            damage += 10
        elif prof == prof_list[1]:
            hp += 0
            damage += 5
        else:
            print("Такой профессии не существует")
            hp = 0
            damage = 0
        return Player(name, hp, damage)
class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    @staticmethod
    def create_enemy():
        enemy_name = random.choice(enemy_names)
        enemy_hp = random.randint(60, 180)
        enemy_damage = random.randint(70, 120)
        return  Enemy(enemy_name, enemy_hp, enemy_damage)

    def attack(self, victim):
        victim.hp -= self.damage
        if victim.hp <= 0:
            print(victim.name, "Поврежден. Конец игры.")
            quit()
        else:
            print(self.name, "Нанесен удар: %s" % self.damage)
            print(victim.name, "Теперь имеет", victim.hp, "Очков здоровья")

enemy_names = ["Дракон", "Демон", "Орк"]


player_name = input("Введите имя своего героя: ")

races = ["эльф", "гном", "человек", "волшебник"]
prof_list = ["лучник", "мечник"]

race = input(f"Кем вы хотите играть? \n"
             f"Доступные расы {races}: ").lower()
prof = input(f"Какой профессией вы хотите владеть? \n"
             f"Доступные профессии {prof_list}: ").lower()

enemy = Enemy.create_enemy()
hero = Player.create_hero(player_name, race, prof)
print(f"Здравствуй, {hero.name}")
print(hero.hp, hero.damage)
print(f"Ваш враг {enemy.name}")
print(enemy.hp, enemy.damage)