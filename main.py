import time
import random
from rune_solver import find_arrow_directions
from interception import *
from game import Game
from player import Player
import sys

def bind(context):
    context.set_filter(interception.is_keyboard, interception_filter_key_state.INTERCEPTION_FILTER_KEY_ALL.value)
    print("Click any key on your keyboard.")
    device = None
    while True:
        device = context.wait()
        if interception.is_keyboard(device):
            print(f"Bound to keyboard: {context.get_HWID(device)}.")
            c.set_filter(interception.is_keyboard, 0)
            break
    return device

def solve_rune(g, p, target):
    """
    Given the (x, y) location of a rune, the bot will attempt to move the player to the rune and solve it.
    """
    while True:
        print("Pathing towards rune...")
        p.go_to(target)
        # Activate the rune.
        time.sleep(1)

        # Interact key  
        p.press("B")

        # Take a picture of the rune.
        time.sleep(1)
        img = g.get_rune_image()
        print("Attempting to solve rune...")
        directions = find_arrow_directions(img)

        if len(directions) == 4:
            print(f"Directions: {directions}.")
            for d, _ in directions:
                p.press(d)

            # The player dot will be blocking the rune dot, attempt to move left/right to unblock it.
            p.hold("LEFT")
            time.sleep(random.uniform(0.5, 1.25))
            p.release("LEFT")

            p.hold("RIGHT")
            time.sleep(random.uniform(0.5, 1.25))
            p.release("RIGHT")

            rune_location = g.get_rune_location()
            if rune_location is None:
                print("Rune has been solved.")
                time.sleep(0.5)
                p.press("LEFT")
                time.sleep(0.5)
                p.press("RIGHT")
                break
            else:
                print("Trying again...")


# Rotation to loot
def loot():
    time.sleep()
 
if __name__ == "__main__":
    if len(sys.argv) == 2:
        rune_cd_time = time.time() + float(sys.argv[1]) * 60
    else:
        rune_cd_time = time.time()
    

    # This setup is required for Interception to mimic your keyboard.
    c = interception()
    d = bind(c)
    
    #top, left, bottom, right
    g = Game((5, 5, 100, 180))
    p = Player(c, d, g)
    counter = 0

    # Starting position (x,y)
    target = (6, 70)

    # Timers for buffs/attacks
    over_time = time.time()
    loot_time = time.time()
    

    # Rotation Loop
    while True:
        #p.player_check(g)      

    ################################################################################
        if time.time() >= rune_cd_time:
            rune_location = g.get_rune_location()
            if rune_location is not None:
                print("A rune has appeared.")
                solve_rune(g, p, rune_location)
                rune_cd_time = time.time() + 60 * 10
           
        start_time = time.time()
        p.release_all()
        p.go_to(target)
        
        time.sleep(0.3)
        p.press("RIGHT")
        for _ in range(2):
            p.press("RIGHT")
            p.press("ALT")
            for _ in range(3):
                p.press("SPACE")
                time.sleep(0.2)
                p.press("SPACE")
                p.press("X")
                time.sleep(0.6)
            p.press("SPACE")
            time.sleep(0.1)
            p.press("SPACE")
            p.press("X")
            time.sleep(0.7)
                

            p.press("SPACE")
            p.hold("UP")
            time.sleep(0.2)
            p.press("SPACE")
            p.release("UP")
            time.sleep(0.6)
            p.press("CTRL")
            time.sleep(0.7)
            p.press("LEFT")


            for _ in range(2):
                p.press("SPACE")
                time.sleep(0.1)
                p.press("SPACE")
                p.press("X")
                time.sleep(0.6)
            p.press("SPACE")
            time.sleep(0.2)
            p.press("SPACE")
            time.sleep(0.3)
            p.press("CTRL")      
            time.sleep(0.7)   
            p.press("S")
            time.sleep(1)

            p.press("SPACE")
            time.sleep(0.2)
            p.press("SPACE")
            p.press("X")
            time.sleep(0.6)
            p.press("SPACE")
            time.sleep(0.2)
            p.press("SPACE")
            p.press("X")
            time.sleep(0.6)
            p.press("CTRL")      
            time.sleep(0.7)   
            p.go_to(target)

            for _ in range(4):
                p.press("RIGHT")
                p.press("ALT")
                for _ in range(3):
                    p.press("SPACE")
                    time.sleep(0.2)
                    p.press("SPACE")
                    p.press("X")
                    time.sleep(0.6)
                p.press("SPACE")
                time.sleep(0.1)
                p.press("SPACE")
                p.press("X")
                time.sleep(0.7)
                    

                p.press("SPACE")
                p.hold("UP")
                time.sleep(0.2)
                p.press("SPACE")
                p.release("UP")
                time.sleep(0.6)
                p.press("CTRL")
                time.sleep(0.7)
                p.press("LEFT")


                for _ in range(2):
                    p.press("SPACE")
                    time.sleep(0.1)
                    p.press("SPACE")
                    p.press("X")
                    time.sleep(0.6)
                p.press("SPACE")
                time.sleep(0.2)
                p.press("SPACE")
                time.sleep(0.3)
                p.press("CTRL")      
                time.sleep(0.7)   
                p.press("SPACE")
                time.sleep(0.2)
                p.press("SPACE")
                p.press("X")
                time.sleep(0.6)
                p.press("SPACE")
                time.sleep(0.2)
                p.press("SPACE")
                p.press("X")
                time.sleep(0.6)
                p.press("CTRL")      
                time.sleep(0.7)   
                p.go_to(target)


        p.press("RIGHT")
        p.press("ALT")
        for _ in range(4):
            p.press("SPACE")
            time.sleep(0.15)
            p.press("SPACE")
            p.press("X")
            time.sleep(0.6)



        p.press("A")
        time.sleep(1.2)
        p.press("LEFT")
        time.sleep(0.1)
        p.press("CTRL")
        p.press("ALT")
        time.sleep(0.6)

        p.press("SPACE")
        time.sleep(0.3)
        p.press("SPACE")
        p.press("X")
        time.sleep(0.6)

        p.press("SPACE")
        time.sleep(0.1)
        p.press("SPACE")
        p.press("X")
        time.sleep(0.6)    

        p.press("SPACE")
        time.sleep(0.1)
        p.press("SPACE")
        p.press("X")
        time.sleep(0.6)

        p.press("SPACE")
        time.sleep(0.2)
        p.press("SPACE")
        time.sleep(0.4)
        p.press("CTRL")
        time.sleep(1.4)

        p.hold("DOWN")
        p.press("SPACE")
        p.release("DOWN")
        time.sleep(0.5)
        p.press("SPACE")
        p.go_to(target)

        # End of rotations
        total_time = time.time() - start_time
        print("Rotation Time:", total_time)