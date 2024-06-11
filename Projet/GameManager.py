class GameManager:
    _instance = None

    @staticmethod
    def get_instance():
        if GameManager._instance is None:
            GameManager._instance = GameManager()
        return GameManager._instance

    def __init__(self):
        if GameManager._instance is not None:
            raise Exception("This class is a singleton!")
        self.game_state = {
            "player": None,
            "enemy": None
        }

    def set_player(self, player):
        self.game_state["player"] = player

    def get_player(self):
        return self.game_state["player"]

    def set_enemy(self, enemy):
        self.game_state["enemy"] = enemy

    def get_enemy(self):
        return self.game_state["enemy"]
