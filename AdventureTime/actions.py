from player import Player


class Action():
    """Base class for all actions."""
    def __init__(self, method, name, hotkey, **kwargs):
        """Creates an action.

        param method: the function object to execute.
        param hotkey: the keyboard key the player uses to initiate this action.
        param name: the name of the action.
        param ends_turn: True if the player is expected to move after this action else False.
        """
        self.method = method
        self.hotkey = hotkey
        self.name = name
        self.kwargs = kwargs

    def __str__(self):
        return "{}: {}".format(self.hotkey, self.name)


class MoveNorth(Action):
    def __init__(self):
        super().__init__(method=Player.move_north, name="Move North", hotkey="n")


class MoveSouth(Action):
    def __init__(self):
        super().__init__(method=Player.move_south, name="Move South", hotkey="s")


class MoveEast(Action):
    def __init__(self):
        super().__init__(method=Player.move_east, name="Move East", hotkey="e")


class MoveWest(Action):
    def __init__(self):
        super().__init__(method=Player.move_west, name="Move West", hotkey="w")


class ViewInventory(Action):
    """Prints out the player's current inventory."""
    def __init__(self):
        super().__init__(method=Player.print_inventory, name="View Inventory", hotkey="i")


class Heal(Action):
    def __init__(self):
        super().__init__(method=Player.heal_self, name="Heal Self", hotkey="h")


class Attack(Action):
    def __init__(self, enemy):
        super().__init__(method=Player.attack, name="Attack", hotkey="a", enemy=enemy)


class Flee(Action):
    def __init__(self, tile):
        super().__init__(method=Player.flee, name="Flee", hotkey="f", tile=tile)
