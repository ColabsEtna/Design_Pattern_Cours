class AttackStrategy:
    def attack(self, attacker, target):
        pass

class SwordAttack(AttackStrategy):
    def attack(self, attacker, target):
        damage = max(0, attacker.attack - target.defense)
        return damage

class ShieldBash(AttackStrategy):
    def attack(self, attacker, target):
        damage = max(0, attacker.attack * 0.8 - target.defense * 0.5)
        return damage

class MagicAttack(AttackStrategy):
    def attack(self, attacker, target):
        damage = max(0, attacker.attack * 1.5 - target.defense)
        return damage

class Fireball(AttackStrategy):
    def attack(self, attacker, target):
        damage = max(0, attacker.attack * 2 - target.defense)
        return damage

class BowAttack(AttackStrategy):
    def attack(self, attacker, target):
        damage = max(0, attacker.attack * 1.2 - target.defense)
        return damage

class PoisonArrow(AttackStrategy):
    def attack(self, attacker, target):
        damage = max(0, attacker.attack * 1.1 - target.defense)
        return damage
