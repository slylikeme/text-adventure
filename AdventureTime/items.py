class Item():
    """ The base class for all items."""
    def __init__(self, name, description, value):
        """Creates a new item

        param name: name of the item.
        param name: description of the item.
        param name: value of the item if sold to a vendor.
        """
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)


class Gold(Item):
    def __init__(self, amt):
        """Gold item which can be used to purchase things.

        param amt: amount of gold, which is equal to its value.
        """
        self.amt = amt
        super().__init__(name="Gold",
                         description='{} sparkling gold coins.'.format(str(self.amt)),
                         value=self.amt)

    def add(self, amt):
        self.amt += amt
        self.description = '{} sparkling gold coins.'.format(str(self.amt))
        self.value = self.amt


class Consumable(Item):
    def __init__(self, name, description, value, healing_value):
        """Consumable class that heals player.

        param healing_value: amount consumable will heal player
        """
        self.healing_value = healing_value
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nHealing Value: {}".format(self.name, self.description, self.value, self.healing_value)


class HealPotion(Consumable):
    def __init__(self):
        super().__init__(name="Healing Potion",
                         description="A golden liquid that bubbles inside the vial.",
                         value=60,
                         healing_value=25)


class Weapon(Item):
    """The base class for weapon items, based on the item class."""
    def __init__(self, name, description, value, damage):
        """Creates a weapon, which does damage to enemies and is wielded by the Player.

        param damage: damage that is done to enemy hitpoints.
        """
        self.damage = damage
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)


class Rock(Weapon):
    def __init__(self):
        super().__init__(name="Rock",
                         description="A fist sized rock, perfect for smashing.",
                         value=0,
                         damage=5)


class Dagger(Weapon):
    def __init__(self):
        super().__init__(name="Dagger",
                         description="A small rusted dagger. More dangerous than a rock.",
                         value=10,
                         damage=10)

class Sword(Weapon):
    def __init__(self):
        super().__init__(name="Sword",
                         description="A beautifully crafted longsword. Razor-sharp and incredibly balanced.",
                         value=30,
                         damage=20)
