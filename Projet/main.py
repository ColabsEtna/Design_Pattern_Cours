from GameManager import GameManager
from Characters import CharacterFactory

def main():
    game_manager = GameManager.get_instance()

    # Création du personnage du joueur
    character_type = input("Choose your character (Warrior, Mage, Archer): ")
    character_name = input("Enter your character's name: ")
    player = CharacterFactory.create_character(character_type, character_name)
    
    # Définir la stratégie d'attaque initiale
    print("Available strategies: ", ", ".join(player.strategies.keys()))
    initial_strategy = input("Choose initial attack strategy: ")
    player.set_strategy(initial_strategy)
    
    game_manager.set_player(player)

    # Création d'un ennemi
    enemy = CharacterFactory.create_character("Warrior", "Enemy Warrior")
    enemy.set_strategy("SwordAttack")
    game_manager.set_enemy(enemy)

    # Boucle principale du jeu
    while player.health > 0 and enemy.health > 0:
        print("\n--- Player's Turn ---")
        player.perform_attack(enemy)

        if enemy.health <= 0:
            print("You have defeated the enemy!")
            break

        print("\n--- Enemy's Turn ---")
        enemy.perform_attack(player)

        if player.health <= 0:
            print("You have been defeated by the enemy!")
            break

        # Changer de stratégie d'attaque (optionnel)
        change_strategy = input("\nDo you want to change your attack strategy? (yes/no): ").lower()
        if change_strategy == "yes":
            print("Available strategies: ", ", ".join(player.strategies.keys()))
            new_strategy = input("Choose new strategy: ")
            player.set_strategy(new_strategy)

if __name__ == "__main__":
    main()
