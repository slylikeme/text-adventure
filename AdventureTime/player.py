import random
import items, world


class Player():
    def __init__(self):
        self.inventory = [items.Gold(15), items.Rock()]
        self.hp = 100
        self.location_x, self.location_y = world.starting_position
        self.victory = False

    def is_alive(self):
        return self.hp > 0

    def do_action(self, action, **kwargs):
        action_method = getattr(self, action.method.__name__)
        if action_method:
            action_method(**kwargs)

    def print_inventory(self):
        for item in self.inventory:
            print(item, '\n')
        print("You have {} hitpoints.\n ".format(self.hp))

    def add_gold(self, amt):
        for i, j in enumerate(self.inventory):
            if isinstance(j, items.Gold):
                self.inventory[i].add(amt)

    def move(self, dx, dy):
        self.location_x += dx
        self.location_y += dy
        print(world.tile_exists(self.location_x, self.location_y).intro_text())

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)

    def heal_self(self):
        best_potion = None
        max_heal = 0
        for i in self.inventory:
            if isinstance(i, items.HealPotion):
                if i.healing_value > max_heal:
                    max_heal = i.healing_value
                    best_potion = i

        try:
            self.hp += best_potion.healing_value
            print("You heal for {}. Your hp is now {}.\n".format(best_potion.healing_value, self.hp))
            self.inventory.remove(best_potion)

        except:
            print("You dont have a healing potion!\n")


    def attack(self, enemy):
        best_weapon = None
        max_dmg = 0
        for i in self.inventory:
            if isinstance(i, items.Weapon):
                if i.damage > max_dmg:
                    max_dmg = i.damage
                    best_weapon = i

        print("You use your {} against the {}!".format(best_weapon.name, enemy.name))
        enemy.hp -= best_weapon.damage
        if not enemy.is_alive():
            print("You strike a mortal blow against the {}! It crumples in a mangled heap to the floor.".format(enemy.name))
        else:
            print("You hit the {0}! {0} HP is now {1}".format(enemy.name, enemy.hp))

    def flee(self, tile):
        """Moves the player randomly to an adjacent tile."""
        available_moves = tile.adjacent_moves()
        r = random.randint(0, len(available_moves) - 1)
        self.do_action(available_moves[r])
