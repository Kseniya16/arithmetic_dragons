# coding: utf-8
# license: GPLv3


class Attacker:
    _health = None
    _attack = None
    _experience = None

    def attack(self, target):
        target._health -= self._attack

    def is_alive(self):
        return self._health > 0

    def its_experience_plus(self):
        self._experience += 100
        return self._experience

    def its_experience_minus(self):
        self._experience -= 50
        return self._experience