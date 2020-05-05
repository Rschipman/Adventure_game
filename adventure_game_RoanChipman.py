import time
import random

holster = []
win = []
enemy_list = ["murderous vampire", "wretched pirate Red Beard",
              "wicked witch", "evil fairie", "awful gym teacher"]
weapon_list = ["the Sword of Destiny", "the magic Wand of Elderberry",
               "the Mirror of Truth", "a fart gun"]
weapon_choice = random.choice(weapon_list)
enemy_choice = random.choice(enemy_list)


def print_pause(message, delay = 2):
    print(message)
    time.sleep(int(delay))


def valid_input(prompt, options = []):
    response = ""
    valid = False
    while not valid:
        response = input(prompt)
        for x in options:
            if response == x:
                valid = True
                break
            if not valid:
                print_pause("Enter a valid choice")
    return response


def restart():
    print_pause("You are standing in a field lush with wildflowers.")
    print_pause("Behind, some distance away, "
                "lays a house shrouded in mystery . . . \n")
    print_pause("To your left a dark gloomy cave.")
    response = valid_input("What would you like to do? \n"
                           "Press '1' to return to your home village, '2' to"
                           " investigate the cave \n", ["1", "2"])
    if response == "1":
        the_village()
    elif response == "2":
        the_cave()


def intro():
    print_pause("You are standing in a field lush with wildflowers.")
    print_pause("You spot your trusty, yet rusted, short sword on "
                "the ground next to you and holster it. ")
    print_pause("You look around as you remember the cries of the "
                "tortured townfolk you have been sent to save\n"
                "from a vicious, unseen enemy.")
    print_pause("Ahead of you, some distance away, \n"
                "lays a house shrouded in mystery . . . ")
    print_pause("To your right a dark gloomy cave.")
    the_field()


def the_field():
    response = valid_input("What would you like to do? \n"
                           "Press '1' to proceed towards the house "
                           "Press '2' to investigate the cave \n", ["1", "2"])

    if response == "1":
        print_pause("You approach the house and knock confidently on the"
                    " door")
        print_pause("You draw your weapon as the door creaks open on its"
                    " own \n")
        the_house()

    elif response == "2":
        the_cave()


def the_cave():
    print_pause("You walk towards the cave.")
    print_pause("You peer cautiously inside.")
    print_pause("In the depths of the cave you spot something!")
    response = valid_input("Would you like to fetch the object? \n"
                           "Press '1' to fetch '2' to flee back to"
                           " the field \n", ["1", "2"])
    if response == "1":
        print_pause("You pick up the mysterious object.")
        print_pause("Behold! The %s!" % weapon_choice)
        print_pause("You throw aside your old tarnished weapon")
        print_pause("You continue on your quest with your new weapon safely"
                    " holstered")
        holster.append(weapon_choice)
        the_field_cave()
    elif response == "2":
        the_field_cave()


def the_field_cave():
    print_pause("You return to the field")
    print_pause("To the right lays the mysterious house,")
    print_pause("to your back the cave")
    if weapon_choice in holster:
        response = valid_input("Would you like to proceed to the house?\n"
                               "Press '1' to proceed to the house '2' to"
                               " return to you village with your new"
                               " treasure \n", ["1", "2"])
        if response == "1":
            print_pause("You continue to the house.")
            the_house()
        elif response == "2":
            the_village()
    else:
        response = valid_input("What would you like to do? \n"
                               "Press '1' to approach the house '2' to flee"
                               " home to your village \n", ["1", "2"])
        if response == "1":
            the_house()
        else:
            the_village()


def the_house():
    print_pause("The house appears empty")
    print_pause("Shadows cloak the entire room leaving little to be "
                "observed")
    response = valid_input("Do you dare enter? \n"
                           "Press '1' to enter '2' to run back to the"
                           " field \n", ["1", "2"])
    if response == "1":
        print_pause("Suddenly you are struck by an ear piercing screech!")
        if weapon_choice in holster:
            print_pause("With no thought left in your mind, but the need for"
                        " survival strong in your bones, "
                        "you draw your weapon with lighting speed")
            print_pause("The %s stops in their tracks!" % enemy_choice)
            print_pause("'NO! It can't be! Not %s!!' a"
                        " goosebump inducing voice says. " % weapon_choice)
            print_pause("The %s glares daggers in to your heart before "
                        "fleeing in fear" % enemy_choice)
            win.append("victory")
            print_pause("You victoriously gather treasures scattered around "
                        "the house "
                        "to bring home to your village.")
            the_village()
        else:
            print_pause("The noise nearly cripples you. "
                        "You stagger and struggle to keep your "
                        "weapon in hand.")
            print_pause("Before you have a chance to attack you, "
                        "feel something forcefully strike your head")
            print_pause(". . . ")
            print_pause("You slowly awaken.")
            print_pause("You rise to your feet.")
            intro()
    elif response == "2":
        print_pause("You flee, a chill deep in your bones.")
        restart()


def the_village():
    if "victory" in win:
        print_pause("The villagers rejoice as you enter in to your home's"
                    " village square, "
                    "face beaming with your victory")
        print_pause("The people lift you above their heads chanting your "
                    "name in their victory cries")
        print_pause("YOU WIN!")
        replay_game()
    else:
        if weapon_choice in holster:
            print_pause("The villagers throw old rotted food at the greedy"
                        " bastard they once believed to be a hero")
            print_pause("Your greed has caused you to completly forget your "
                        "mission")
            print_pause("The village will never forgive you.")
        else:
            print_pause("You enter the village, your head hung low.")
            print_pause("The villagers wont even look at the coward that "
                        "returned without a fight")
            print_pause("Ashamed you vow to never leave your house again")
        you_lose()


def start_game():
    print_pause("You a lowly farmer working the fields are approached by a"
                " frail, sickly looking, old man.")
    print_pause("He speaks quielty:")
    response = valid_input("'Are you a brave soul in search of a dangerous"
                           " quest?' \n"
                           "Please press '1' for Yes or '2' for No \n", ["1",
                           "2"])
    if response == "1":
        play_game()
    elif response == "2":
        print_pause("Understood.")
        print_pause("So long.")
        exit()


def you_lose():
    print_pause("YOU LOSE")
    replay_game()


def play_game():
    print_pause("'Thank goodness!'")
    print_pause("'You are our saviour from this awful beast!'")
    print_pause("'You shall leave immediately!'")
    print_pause("The man strikes you suddenly")
    print_pause("You fall unconcious.")
    print_pause("You awaken and arise slowly.")
    print_pause(". . . ")
    intro()

def replay_game():
    print_pause("Would you like to play again?")
    response = valid_input( "Press '1' for YES '2' for NO\n", ["1", "2"])
    if response == "1":
        start_game()
    elif response == "2":
        print_pause("Farewell")
        exit()


start_game()
