from Strategies import SwordAttack, ShieldBash, MagicAttack, Fireball, BowAttack, PoisonArrow


class Character:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.strategies = {}
        self.current_strategy = None

    def add_strategy(self, strategy_name, strategy):
        self.strategies[strategy_name] = strategy

    def set_strategy(self, strategy_name):
        self.current_strategy = self.strategies.get(strategy_name)
        if self.current_strategy is None:
            print(f"Strategy {strategy_name} not found for {self.name}.")

    def perform_attack(self, target):
        if self.current_strategy is not None:
            damage = self.current_strategy.attack(self, target)
            target.health -= damage
            print(f"{self.name} attacks {target.name} with {self.current_strategy.__class__.__name__} and deals {damage} damage. {target.name} has {target.health} health left.")
        else:
            print(f"{self.name} has no attack strategy set!")

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack=30, defense=20)
        self.add_strategy("SwordAttack", SwordAttack())
        self.add_strategy("ShieldBash", ShieldBash())

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack=50, defense=10)
        self.add_strategy("MagicAttack", MagicAttack())
        self.add_strategy("Fireball", Fireball())

class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack=25, defense=15)
        self.add_strategy("BowAttack", BowAttack())
        self.add_strategy("PoisonArrow", PoisonArrow())

class CharacterFactory:
    @staticmethod
    def create_character(character_type, name):
        if character_type == "Warrior":
            return Warrior(name)
        elif character_type == "Mage":
            return Mage(name)
        elif character_type == "Archer":
            return Archer(name)
        else:
            raise ValueError("Unknown character type")
