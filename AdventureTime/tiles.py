import items, enemies, actions, world


class MapTile:
    """The base class for a tile within the world space."""
    def __init__(self, x, y):
        """Creates a new tile.

        param x: x coordinate of the tile.
        param y: y coordinate of the tile.
        """
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self, player):
        raise NotImplementedError()

    def adjacent_moves(self):
        """Returns all move actions for adjacent tiles."""
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves

    def available_actions(self):
        """Returns all of the available actions in this room."""
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())
        return moves


class StartingRoom(MapTile):
    def intro_text(self):
        return """
        You are in a decrepit stone room with a single flickering torch on the far wall.
        Shadows dance and hide in every corner.
        You can barely make out four diverging pathways, each equally dark
        and foreboding.
        You need to make it out!
        """

    def modify_player(self, player):
        # Room has no action on the player
        pass


class EscapeRoom(MapTile):
    def intro_text(self):
        return """
        You see a bright light ahead of you...
        The light hurts your eyes as you approach it...
        It's sunlight! You've found the exit!
        You open the heavy wooden door and flee the dungeon.

        Victory is yours!

        For now...
        """
    def modify_player(self, player):
        player.victory = True


class SnakePitRoom(MapTile):
    def intro_text(self):
        return """
        You have fallen into a pit of deadly snakes!
        You desperately fight them off using your weapon, slaying one after another.
        It is to no avail, as you are overwhelmed by sheer numbers.
        They bite you countless times. As your vision fades and your mind swims,
        a thought enters your head:

        Maybe I should not have gone in this room...

        You have died!
        """

    def modify_player(self, player):
        player.hp = 0


class HealingRoom(MapTile):
    def intro_text(self):
        return """
        This room is much warmer than the others. The stones are free from moss,
        and seem almost new. The very air itself is cleaner.
        A sudden rush of warmth surrounds you!
        You are fully healed!
        """

    def modify_player(self, player):
        player.hp = 100


class LootRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)

    def add_loot(self, player):
        if isinstance(self.item, items.Gold):
            player.add_gold(self.item.amt)
        else:
            player.inventory.append(self.item)

        self.item = None

    def modify_player(self, player):
        if self.item:
            self.add_loot(player)


class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} hp remaining.".format(self.enemy.damage, player.hp))

    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
        else:
            return self.adjacent_moves()


class EmptyDungeon(MapTile):
    def intro_text(self):
        return """
        Water is dripping somewhere nearby. Dungeon cells line either side of the path.
        All of them appear empty.
        You must forge onwards.
        """

    def modify_player(self, player):
        # Room has no action on the player
        pass


class CavedInDungeon(MapTile):
    def intro_text(self):
        return """
        It appears this room suffered a partial cave-in sometime in the distant past.
        You can make out the grim remains of a crushed skeleton in one of the
        destroyed cells.
        You shudder and wonder if you will meet a similar fate.
        """

    def modify_player(self, player):
        # Room has no action on the player
        pass


class PeopleDungeon(MapTile):
    def intro_text(self):
        return """
        The smell of disease and death fills every corner of this dungeon. You
        gag, nearly vomiting from the stench. Covering your mouth and nose,
        you stumble forward.
        Soft, pitiful moans escape from some of the darkened cells.
        You must escape this wretched place!
        """

    def modify_player(self, player):
        # Room has no action on the player
        pass


class GiantSpiderRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.GiantSpider())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A giant spider drops down from the inky blackness above and swipes
            at you with long evil legs.
            """
        else:
            return """
            A mangled spider corpse sprawls across the floor. You gingerly step
            around it, but despite your best efforts you get some goo on your shoes.
            You scrape it off as best you can.
            """

class OgreRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Ogre())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A massive ogre roars and charges forward, crushing the bones of previous
            victims under his gnarled feet.
            It attacks you with a menacing stone club.
            """
        else:
            return """
            An enormous ogre corpse lies facedown on the cave floor, surrounded
            by a huge pool of purple blood.
            """


class LordRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.DungeonLord())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            The lord of the dungeon towers above you.
            He laughs maniacally as he attacks you with his razor-sharp scythe.
            """
        else:
            return """
            A pile of rancid ashes is all that remains of the once mighty Dungeon Lord.
            """

class FindDaggerRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Dagger())

    def intro_text(self):
        if self.item:
            return """
            You notice something shiny in the corner of the chamber. You move closer.
            It's a dagger! You pick it up.
            """
        else:
            return """
            This the room where you found your dagger.
            There is nothing remarkable about this room now.
            """


class FindSwordRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Sword())

    def intro_text(self):
        if self.item:
            return """
            A mighty sword is cradled between the feet of a ruined statue.
            It glows with a light of its own.
            You gladly pick it up.
            Finally you feel strong enough to face anything this dungeon has to offer.
            """
        else:
            return """
            This the room where you found your sword.
            The statue seems to have been aged since you took the sword.
            You feel a pang of regret, but you must survive!
            """


class Find5GoldRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Gold(5))

    def intro_text(self):
        if self.item:
            return """
            Someone dropped 5 gold pieces on the floor. You scoop them up greedily.
            """
        else:
            return """
            You previously discovered gold in this room.
            It is now empty and unremarkable.
            """
