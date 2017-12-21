import world
from player import Player


def play():
    world.load_tiles()
    player = Player()
    # Load starting room and display text
    room = world.tile_exists(player.location_x, player.location_y)
    print(room.intro_text())

    while player.is_alive() and not player.victory:
        room = world.tile_exists(player.location_x, player.location_y)
        room.modify_player(player)
        # check if room has changed player state
        if player.is_alive() and not player.victory:
            print("Choose an action:\n")
            available_actions = room.available_actions()
            for action in available_actions:
                print(action)
            action_input = input("Action: ")
            print("")
            for action in available_actions:
                if action_input == action.hotkey:
                    player.do_action(action, **action.kwargs)
                    break
        elif not player.is_alive() and not player.victory:
            print("""
            You have been slain!
            The life force pours out from your body
            and you are left to wonder what you did wrong.     
                  """)

if __name__ == "__main__":
    play()
