# coding: utf-8
# license: GPLv3
from gameunit import *
from random import randint, choice

class Enemy(Attacker):
    pass


def generate_random_enemy():
    RandomEnemyType = choice(enemy_types)
    enemy = RandomEnemyType()
    return enemy


def generate_dragon_list(enemy_number):
    enemy_list = [generate_random_enemy() for i in range(enemy_number)]
    return enemy_list


class Dragon(Enemy):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer


class GreenDragon(Dragon):
    def __init__(self):
        self._health = 100
        self._attack = 10
        self._color = 'зелёный'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '+' + str(y)
        self.set_answer(str(x + y))
        return self.__quest

class RedDragon(Dragon):
    def __init__(self):
        self._health = 100
        self._attack = 10
        self._color = 'красный'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '-' + str(y)
        self.set_answer(str(x - y))
        return self.__quest

class BlackDragon(Dragon):
    def __init__(self):
        self._health = 100
        self._attack = 10
        self._color = 'черный'

    def question(self):
        x = randint(1,10)
        y = randint(1,10)
        self.__quest = str(x) + '*' + str(y)
        self.set_answer(str(x * y))
        return self.__quest

class BlueTroll(Dragon):
    def __init__(self):
        self._health = 100
        self._attack = 10
        self._color = 'Blue'

    def question(self):
        x = randint(1,2)
        self.__quest ='Угадай число от 1 до 2'
        self.set_answer(x)
        return self.__quest

class YellowTroll(Dragon):
    def __init__(self):
        self._health = 100
        self._attack = 10
        self._color = 'Yellow'

    def question(self):
        x = randint(3,20)
        self.__quest ='Number '+ str(x) + ' is simple? Yes=1 or No=0'
        for i in range(2,x+1):
            if x%i == 0:
                self.set_answer(1)
            else:
                self.set_answer(0)

        return self.__quest

class OrangeTroll(Dragon):
    def __init__(self):
        self._health = 100
        self._attack = 10
        self._color = 'Orange'

    def question(self):
        x = randint(2, 2)
        self.__quest = 'Введите множители числа ' + str(x) + " в возрастающем порядке через запятую"
        answer_list = []
        i = 2
        M = int(x)
        while M >= 2:
            if M % i == 0:
                answer_list.append(i)
                M = M / i
            else:
                i += 1
        #print(self.set_answer)
        tmp = []
        for i in answer_list:
            tmp.append(str(i))
        answer = ",".join(tmp)
        self.set_answer(answer)
        print(answer)
        return self.__quest


enemy_types = [GreenDragon, RedDragon, BlackDragon, BlueTroll, YellowTroll, OrangeTroll]
#GreenDragon, RedDragon, BlackDragon, BlueTroll, YellowTroll, OrangeTroll