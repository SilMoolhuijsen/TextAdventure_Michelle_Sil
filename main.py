import time
import os
import sys
import classes

#Lists used when choosing the game's text speed
txtSpeed5 = ["Very Fast", "very fast", "very Fast", "Very fast", "5"]
txtSpeed4 = ["Fast", "fast", "4"]
txtSpeed3 = ["Normal", "normal", "3"]
txtSpeed2 = ["Slow", "slow", "2"]
txtSpeed1 = ["Very Slow", "very slow", "very Slow", "Very slow", "1"]
txtSpeed6 = ["Fastest", "fastest", "6"]
END_SENTENCE = [".", "!", "?"]
COMMA = ","

#List that stores all of the player's items
player_inventory = []

#Function to (re)run the game
def start_game():
  #Let's player choose the game's text speed
  def choose_ts():
    ts = 0.0075
    def slowprint(s):
      for letter in s:
        sys.stdout.write(letter)
        sys.stdout.flush()
        if letter in COMMA:
          time.sleep(ts * 8)
        if letter in END_SENTENCE:
          time.sleep(ts * 16)
        else:
          time.sleep(ts)
    TextSpeed = slowprint("Text speeds: Very Slow (1), Slow (2), Normal (3), Fast (4), Very Fast (5) or Fasterst (6)\nChoose a text speed: ")
    TextSpeed = input()
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    if TextSpeed in txtSpeed5:
      ts = 0.005
    elif TextSpeed in txtSpeed4:
      ts = 0.01
    elif TextSpeed in txtSpeed3:
      ts = 0.02
    elif TextSpeed in txtSpeed2:
      ts = 0.05
    elif TextSpeed in txtSpeed1:
      ts = 0.1
    elif TextSpeed in txtSpeed6:
      ts = 0
    else:
      slowprint("That is not a valid text speed. Choose from Very Slow (1), Slow (2), Normal (3), Fast (4) or Very Fast (5).\n\n")
      time.sleep(0.5)
      start_game()
      os.system('cls' if os.name == 'nt' else "printf '\033c'")
    
    #Function that removes spaces from user input, converts it into uppercase and slowprints it
    def modified_input(string):
      slowprint(string)
      a = input()
      a = a.replace(" ","")
      a = a.upper()
      return a

    #Start of the text adventure
    def start():
      #Lets player choose his name
      def choose_name_start():
        player_name = modified_input("What's your name?\n")
        slowprint("\nOkay " + player_name + ", let's embark on an adventure!")
        time.sleep(1.0)
        os.system('cls' if os.name == 'nt' else "printf '\033c'")
        time.sleep(0.1)
        intro()
      
      #Introduction to the text adventure
      def intro():
        slowprint("You're a millionair and retired CIA agent. You were one of the best fighters ofas the entire CIA. But you're not as skillfull as you were 25 years ago. You're 55 years old now. It's been 3 years since you retired. You've just been enjoying life since then. But that is all going to change.\n\n")
        input("[PRESS ENTER TO CONTINUE]\n\n")
        slowprint("One morning, you wake up. When you analyse the situation, you notice that you're not in your bed, you're sitting in a chair. Also, you don't know this place. It's a room with no windows. Now, you also feel your ankles and torso have been tied to the chair that you're sitting in. You hear deep voices talking in the background. Maybe they're criminals who kidnapped you for your money. Or perhaps they want classified information about the CIA. You have no idea how or why you're in this situation. But you know that you have to get out of here as soon as possible.\n\n")
        input("[PRESS ENTER TO CONTINUE]\n\n")
        slowprint("You don't feel any weapons on you, so you start to examine the room.\n")
        slowprint("You find you're sitting exactly in the centre of the room.\n")
        slowprint("You see a machete on the table against the wall approximately 2 metres to your left. One of the kidnappers must have forgotten about it.\n")
        time.sleep(0.5)
        slowprint("There's a handgun on the ground about 1,5 metres in front of you.\n")
        time.sleep(0.5)
        slowprint("And some tools hanging from the wall roughly 2 metres to your right-hand side.\n")
        time.sleep(0.5)
        slowprint("There's two possible exits, the wall in front you has a door on the right side. And there is a vent in the ceiling close to the tools.\n\n")
        time.sleep(0.5)
        IntroQuestion()

      #First question of the game
      def IntroQuestion():
        IntroInput = modified_input("What will you do?\nA. Hop over to machete\nB. Reach for handgun\nC. Go to tools\nD. Move to door and try to open it\nE. Go to the vent\n")
        if IntroInput == "A":
          slowprint("You successfully made it to the table.\n\n")
          input("[PRESS ENTER TO CONTINUE]")
          os.system('cls' if os.name == 'nt' else "printf '\033c'")
          Machete()
        elif IntroInput == "B":
          slowprint("You're at the handgun, but you can't reach it. You'll need to cut the rope and free yourself.\n\n")
          input("[PRESS ENTER TO CONTINUE]")
          os.system('cls' if os.name == 'nt' else "printf '\033c'")
          Handgun()
        elif IntroInput == "C":  
          slowprint("You made it to the tools.\n\n")
          input("[PRESS ENTER TO CONTINUE]")
          os.system('cls' if os.name == 'nt' else "printf '\033c'")
          Tools()
        elif IntroInput == "D":
          slowprint("You bump against the door and it opens. You see two armed men staring down at you.\nYOU WERE KNOCKED UNCONCIOUS\n\n")
          input("[PRESS ENTER TO CONTINUE]")
          os.system('cls' if os.name == 'nt' else "printf '\033c'")
          IntroQuestion()
        elif IntroInput == "E":
          slowprint("You can't do anything there.\n\n")
          IntroQuestion()
        else:
          slowprint("Please choose A, B, C, D or E only.\n\n")
          time.sleep(1)
          IntroQuestion()

      #Question if player decided to go to machete 
      def Machete():
        MacheteInput1 = modified_input("What will you do now?\nA. Kick the table until the machete falls off and cut the rope to free yourself.\nB. Try to grab the machete with your mouth and cut the rope to free yourself.\n")
        if MacheteInput1 == "A":
          slowprint("You hear the deep voices coming closer. You see two armed men enter the room. One runs towards you.\nYOU WENT UNCONCIOUS BY A TASER GUN\n\n")
          input("[PRESS ENTER TO CONTINUE]")
          os.system('cls' if os.name == 'nt' else "printf '\033c'")
          IntroQuestion()
        elif MacheteInput1 == "B":
          player_inventory.append("machete")
          slowprint("You acquire the machete and place it in your right hand. You use it to cut the rope. You're now able to move about freely.")
          input("[PRESS ENTER TO CONTINUE]")
          os.system('cls' if os.name == 'nt' else "printf '\033c'")
          def Machete2():
            MacheteInput2 = modified_input("Where will you go now?\nA. To the handgun.\nB. To the tools\nC. Through the door\n")
            if MacheteInput2 == "A":
              Handgun()
            elif MacheteInput2 == "B":
              Tools()
            elif MacheteInput2 == "C":
              slowprint("You open the door cautiously and see two startled armed men.\nYOU WERE SHOT AT AGGRESSIVELY WITH A RIFLE\n\n")
              input("[PRESS ENTER TO RESPAWN]")
              os.system('cls' if os.name == 'nt' else "printf '\033c'")
              Machete2()
            else:
              slowprint("Please choose A, B or C only.\n\n")
              time.sleep(1)
              Machete2()
          Machete2()
        else:
          slowprint("Please choose A or B only.\n\n")
          time.sleep(1)
          Machete()

      #Question if player decided to go to handgun
      def Handgun():
        slowprint("")
        HandgunInput1 = modified_input()
        

      #Question if player decided to go to tools
      def Tools():
        slowprint("There's screwdrivers, hammers and a crowbar.\n\n")
        if "machete" in player_inventory:
          ToolsInput1 = modified_input("Which tool will you grab?\nA. A screwdriver\nB. A hammer\nC. The crowbar\n")
          if ToolsInput1 == "A":
            player_inventory.append("screwdriver")
          elif ToolsInput1 == "B":
            player_inventory.append("hammer")
          elif ToolsInput1 == "C":
            player_inventory.append("crowbar")
          else:
            slowprint("Please choose A, B or C only.\n\n")
            time.sleep(1)
            Tools()
        else:
          slowprint("But unfortunately, you aren't able to grab any of them now")
          IntroQuestion()
      
      #Statements to run the different large functions of the game
      choose_name_start()
    start()
  choose_ts()
start_game()