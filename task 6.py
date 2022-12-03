# Вариант 9
import math


class Hero:
    def __init__(self, name, health_points, power_points, damage_points, who_is_this):
        self.name = name
        self.health_points = health_points
        self.power_points = power_points
        self.damage_points = damage_points
        self.who_is_this = who_is_this

    def info(self):
        print(f'Character name: {self.name}')
        print(f'This character is: {self.who_is_this}')
        print(f'Health points: {self.health_points}')
        print(f'Power points: {self.power_points}')
        print(f'Damage points: {self.damage_points}')

    def fight(self):
        print(f'The hero can strike {math.floor(self.power_points / self.damage_points)} times')


class WeakEnemy(Hero):
    def __init__(self, name, health_points, power_points, damage_points, who_is_this, armor):
        super().__init__(name, health_points, power_points, damage_points, who_is_this)
        self.armor = armor
        self.health_points += self.armor

    def info(self):
        super().info()
        print(f'He/She has a armor and it gives him/her +{self.armor} health points')

    def fight_with_weak_enemy(self, hero_damage):
        print(f'The hero must strike {math.ceil(self.health_points / hero_damage)} times to defeat a weak enemy')


class Boss(WeakEnemy):
    def __init__(self, name, health_points, power_points, damage_points, who_is_this, armor, super_blow):
        super().__init__(name, health_points, power_points, damage_points, who_is_this, armor)
        self.super_blow = super_blow
        self.damage_points += self.super_blow

    def info(self):
        super().info()
        print(f'He/She can do a super_blow and it gives him/her +{self.super_blow} damage points')

    def fight_with_boss(self, hero_damage):
        print(f'The hero must strike {math.ceil(self.health_points / hero_damage)} times to defeat a boss')


hero = Hero('Rocket Raccoon', 200, 100, 26, 'hero')
hero.info()
hero.fight()
print('-----')

weak_enemy = WeakEnemy('Ronan', 45, 45, 5, 'weak enemy', 5)
weak_enemy.info()
weak_enemy.fight_with_weak_enemy(26)
print('-----')

boss = Boss('Thanos', 150, 100, 15, 'boss', 10, 20)
boss.info()
boss.fight_with_boss(26)
