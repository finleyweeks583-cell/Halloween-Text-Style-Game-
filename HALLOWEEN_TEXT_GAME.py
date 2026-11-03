import time 
import pyfiglet
import random


valid_input = False
valid_input_2 = False
GAME_RESET = False 

MONEY = 10
HEALTH = 100
items = []

LOCATION_ONE = "DARK FOREST"
LOCATION_TWO = "CASTLE BAPHOMET"
LOCATION_THREE = "CABIN IN THE WOODS"
LOCATION_FOUR = "PLACEHOLDER4"


def DARK_FOREST():
    
    PATH_CHOSEN = False 
    CABIN_OPTION = False 

    print("Loading.....")
    print()
    time.sleep(0.7)
    print("Loading....")
    print()
    time.sleep(0.5)
    print("Loading...")
    print()
    time.sleep(0.5)
    print("Loading..")
    print()
    time.sleep(0.5)
    ENTER_DARK_FOREST = (pyfiglet.figlet_format(f"ENTERING THE {LOCATION_ONE} !", font = 'small'))
    print("\033[32m" + ENTER_DARK_FOREST + "\033[0m")
    print()
    time.sleep(2)
    print("As you walk through the forest path you reach a cross road, The left path seems to have more ware and used regularly whereas the right path is overgrown and looks barley used")
    print()
    time.sleep(3)

    while (not PATH_CHOSEN):
        path_choice = input("Which path will you go down, Left or Right: ").strip().upper()
        print()
        time.sleep(1)
    
        if path_choice == "LEFT":
            PATH_CHOSEN = True 
            print("Loading.....")
            print()
            time.sleep(0.7)
            print("Loading....")
            print()
            time.sleep(0.5)
            print("Loading...")
            print()
            time.sleep(0.5)
            print("Loading..")
            print()
            time.sleep(0.5)
            ENTER_CASTLE = (pyfiglet.figlet_format(F"ENTERING {LOCATION_TWO} ! ", font = 'small'))
            print("\033[95m" + ENTER_CASTLE + "\033[0m")
            time.sleep(1.50)



        elif path_choice == "RIGHT":
            PATH_CHOSEN = True
            print("Loading.....")
            print()
            time.sleep(0.7)
            print("Loading....")
            print()
            time.sleep(0.5)
            print("Loading...")
            print()
            time.sleep(0.5)
            print("Loading..")
            print()
            time.sleep(0.5)            
            ENTER_CABIN = (pyfiglet.figlet_format(F"ENTERING {LOCATION_THREE} ! ", font = 'DOOM'))
            print("\033[33m" + ENTER_CABIN + "\033[0m")
            time.sleep(1.5)
            print("You each the door of an old dilapidated wood cabin, The plants all around the radius of the cabin look dead")
            print()

            while (not CABIN_OPTION):
                time.sleep(1.25)
                cabin_userinput = input("What will you do. A: Knock on the door of the cabin or B: Look around the perimeter : ").strip().upper()
                print()

                if cabin_userinput == "A":
                    CABIN_OPTION = True 
                    print("You walk up and knock on the door")
                    time.sleep(0.5)
                    Knocks = random.randint(1, 10)
                    if Knocks >= 7:
                        print("The second you knock on the door you can feel its loose and it slowly opens with a screach")
                        print()

                    else:
                        print()
                        print(f"You knock on the door {Knocks} times but no answer, you decide to go look around the property some more.")
                        

                elif cabin_userinput == "B":
                    CABIN_OPTION = True 
                    print()
                    print("Option B")
                    

                else:
                    CABIN_OPTION = False
                    print("That is not a valid input, please try again")
                    print()

            
    
        else:
            PATH_CHOSEN = False
            print("That is not a valid option, please try again")
            print()


while (not GAME_RESET):

    

    print()
    PLAYER_NAME = input("Please enter your characters name: ")
    welcome_text = pyfiglet.figlet_format(f"WELCOME TO THE GAME !", font = 'doom')
    time.sleep(1)
    print("\033[91m" + welcome_text + "\033[0m")
    print()

    time.sleep(1.25)
    print("You wake up in what seems to be a dark cell of somekind, the door is lightly ajar what will you do?")

    time.sleep(2)
    print()
    CELL_OPTION_ONE = print("Option A - Walk over to the door and leave")
    print()
    CELL_OPTION_TWO = print("Option B - Search around the small cell")

    while (not valid_input):
        print()
        user_input_cell = input("Chose your option: ").strip().upper()
        print()

        if user_input_cell == "A":
            valid_input = True
            GAME_RESET = True
            print("You exit the cell and infrot of you lays a dark dirt path surrounded by tall trees with only the faint shine of moonlight throught the thick leaves")
            print()
            time.sleep(2)
            DARK_FOREST()
       

        elif user_input_cell == "B":
            valid_input = True 
            print("After looking around the cell you notice a cabnet, After opening the cabnet you are presented with 2 bottles")
            print()
            time.sleep(1.5)
        
            while (not valid_input_2):
                potion_input = input("What bottle will you pick, 1 or 2: ").strip().upper()
                print()
            
                if potion_input == "1":
                    valid_input_2 = True 
                    print("That was poision.......")
                    print()
                    time.sleep(2)
                    print("You Died")
                    time.sleep(0.5)
                    print("Try again")
                    time.sleep(0.5)
                    GAME_RESET = False
                
            
                elif potion_input == "2":
                    GAME_RESET = True
                    valid_input_2 = True
                    print("That was water, nothing happens")
                    print()
                    time.sleep(1.25)
                    print("After drinking the water you put the other bottle in your pocket and exit the cell. " \
                    "Infrot of you lays a dark dirt path surrounded by tall trees with only the faint shine of moonlight throught the thick leaves")
                    print()
                    time.sleep(2)
                    items.append("Bottle of liquid")
                    print(f" You now have: {', ' .join(items)}")
                    print()
                    time.sleep(2)
                    DARK_FOREST()
                   
                else:
                    GAME_RESET = True
                    print("That is not a valid option, please try again")
                    print()
                    valid_input_2 = False
                
        else:
            GAME_REST = True
            print("That is not a valid option, Please try again")
            valid_input = False

