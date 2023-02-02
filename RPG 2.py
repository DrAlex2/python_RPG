import random
import time

class Player:
    def __init__(self, name, race_player, class_player, hp, damage):
        self.name = name
        self.race_player = race_player
        self.class_player = class_player
        self.hp = hp
        self.damage = damage
        self.lvl = 1
        self.exp = 0

    @staticmethod
    def lvlUp():
        hero.exp = 0
        hero.hp += 7 * hero.lvl
        hero.damage += 5 * hero.lvl
        hero.lvl += 1
        print(f"Ваш уровень повысился. Теперь у вас: {hero.lvl} уровень")
        return hero.lvl


    @staticmethod
    def create_weapon():
        weapon_type_list = ['Меч', 'Лук', 'Топор']
        weapon_rare_dict = {
            1: "Обычный",
            2: "Редкий",
            3: "Эпический"
        }
        rnd_wpn_type = weapon_type_list[random.randint(0, len(weapon_type_list) - 1)]
        rnd_wpn_rare = random.choice(list(weapon_rare_dict.keys()))

        if rnd_wpn_type == weapon_type_list[0]:
            hero.damage += 5 * rnd_wpn_rare
        elif rnd_wpn_type == weapon_type_list[1]:
            hero.damage += 7 * rnd_wpn_rare
        elif rnd_wpn_type == weapon_type_list[2]:
            hero.damage += 9 * rnd_wpn_rare
        return rnd_wpn_type, weapon_rare_dict[rnd_wpn_rare]

    @staticmethod
    def create_heal():
        heal_size_dict = {
            20: "Пластырь",
            35: "Бинты",
            50: "Аптечка"
        }
        rnd_heal_size = random.choice(list(heal_size_dict.keys()))
        hero.hp += rnd_heal_size
        return heal_size_dict[rnd_heal_size]

    def attack(self, victim):
        victim.hp -= self.damage
        if victim.hp <= 0:
            print(f"{victim.name} повержен. Ваш герой получает 25 опыта")
            time.sleep(0.5)
            self.exp += random.randint(25, 45)
            print(f"Ваш опыт: {self.exp}")
            expiriens = self.lvl * 50
            if self.exp >= expiriens:
                Player.lvlUp()
            # событие на получение оружия или хилок
            heal_weapon_choice = random.choice(list(choice_list))
            if heal_weapon_choice == "weapon":
                weapon = Player.create_weapon()
                print(f"Вам выпало оружие! {weapon[0], weapon[1]}")
                print(f"Ваш урон теперь {self.damage}")
                time.sleep(.7)
            elif heal_weapon_choice == "heal":
                heal = Player.create_heal()
                print(f"Вам выпала {heal}")
                print(f"Ваше здоровье теперь {self.hp}")
                time.sleep(.7)
            return False
        else:
            print(f"{victim.name} теперь имеет {victim.hp} очков здоровья")
            time.sleep(0.5)
            return True


def create_hero(name,  race_player, class_player):
    name = name
    hp = 0
    damage = 0
    if race_player == race_list[0]:
        hp += 100
        damage += 85
    elif race_player == race_list[1]:
        hp += 150
        damage += 60
    elif race_player == race_list[2]:
        hp += 100
        damage += 75

    else:
        print("Такой расы не существует")
        hp = 0
        damage = 0

    if class_player == class_list[0]:
        hp -= 5
        damage += 15
    elif class_player == class_list[1]:
        hp += 0
        damage += 7
    elif class_player == class_list[2]:
        hp -= 3
        damage += 12
    elif class_player == class_list[3]:
        hp += 10
        damage += 3
    else:
        print("Такой профессии не существует")
        hp = 0
        damage = 0
    return Player(name, race_player, class_player, hp, damage)


class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage


    def attack(self, victim):
        victim.hp -= self.damage
        if victim.hp <= 0:
            print(victim.name, "поврежден. Конец игры.")
            quit()
        else:
            print(self.name, "Нанесен удар: %s" % self.damage)
            print(victim.name, "теперь имеет", victim.hp, "Очков здоровья")
            return True


def create_enemy():
    enemy_name = random.choice(enemy_names)
    enemy_hp = random.randint(70, 140) + hero.lvl * 20
    enemy_damage = random.randint(20, 30) + hero.lvl * 10
    return  Enemy(enemy_name, enemy_hp, enemy_damage)

enemy_names = ["Дракон", "Демон", "Орк"]
class_list = ["лучник", "мечник", "маг", "тяжелый мечник"]
race_list = ["человек", "эльф", "гном"]
choice_list = ["weapon", "heal"]
person = []

print("Здравствуйте. Введите ваше имя: ")
person.append(input())

print("Выберите расу персонажа: ")
for i in race_list:
    print(i, end=" ")
person.append(input().lower())

print("Выберите класс персонажа: ")
for i in class_list:
    print(i, end=" ")
person.append(input().lower())

hero = create_hero(person[0], person[1], person[2])
person.clear()


print("Персонаж создан!")
print(f"Главный герой -> {hero.name} \n"
      f"Класс -> {hero.class_player} \n"
      f"Род -> {hero.race_player} \n"
      f"Здоровье -> {hero.hp} \n"
      f"Урон -> {hero.damage} \n"
      f"Уровень -> {hero.lvl} \n"
      f"Опыт -> {hero.exp} \n")

def fight_choice():
    answer = int(input("Атаковать (1) или бежать (0): "))
    if answer == 1:
        win_lose = hero.attack(enemy)
        if win_lose:
            time.sleep(.7)
            enemy.attack(hero)
            fight_choice()
    elif answer == 0:
        plan = random.randint(0,1)
        if plan == 0:
            print("Побег неудался. Вам придется сражаться")
            enemy.attack(hero)
            time.sleep(1)
            fight_choice()
        elif plan == 1:
            print("Побег удался")
    else:
        print("Будьте внимательней, такого действия нет.")
        time.sleep(2)
        fight_choice()



while True:
    event = random.randint(0,3)
    if event == 0 or event == 1:
        print("Вам ни кто не встретился на пути. Можно идти дальше")
        time.sleep(2)
    elif event == 3 or event == 2:
        enemy = create_enemy()
        print(f"Вам встретился {enemy.name} \n"
              f"Здоровье врага -> {enemy.hp} \n"
              f"Урон врага -> {enemy.damage}")
        fight_choice()

# print("Враг создан!")
# print(f"Ваш враг -> {enemy.name} \n"
#
