class Enemy:
    """Base class for enemies."""
    def __init__(self, name, hp, damage):
        """ Creates a new enemy.

        param name: name of the enemy.
        param name: hitpoints of the enemy.
        param damage: damage an enemy does to player.
        """
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0


class GiantSpider(Enemy):
    def __init__(self):
        super().__init__(name="Giant Spider", hp=10, damage=2)


class Ogre(Enemy):
    def __init__(self):
        super().__init__(name="Ogre", hp=30, damage=15)

class DungeonLord(Enemy):
    def __init__(self):
        super().__init__(name="Dungeon Lord", hp=50, damage=20)
