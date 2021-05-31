import time
import os
import sys

#Lists containing valid inputs for every text speed
txtSpeed5 = ["VERY FAST", "5"]
txtSpeed4 = ["FAST", "4"]
txtSpeed3 = ["NORMAL", "3"]
txtSpeed2 = ["SLOW", "2"]
txtSpeed1 = ["VERY SLOW", "1"]
txtSpeed6 = ["FASTEST", "6"]

#List and variable with characters used when slowprinting
END_SENTENCE = [".", "!", "?"]
COMMA = ","

#Lists containing some valid answers
AnsYes = ["YES", "Y"]
AnsNo = ["NO", "N"]

#Lists with some items
ToolsList = ["SCREWDRIVER", "HAMMER", "CROWBAR"]

#List that stores all of the player's items
player_inventory = []

#Function that prints strings letter by letter
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

#Function that removes spaces from user input, converts it into uppercase and slowprints it
def modified_input(string):
  slowprint(string)

  a = input()

  a = a.replace(" ","")
  a = a.upper()
  
  return a

#Function to (re)run the game
def start_game():

  #Lets the player choose the game's text speed
  def choose_ts():
    global ts
    ts = 0.0075

    TextSpeed = modified_input("Text speeds: Very Slow (1), Slow (2), Normal (3), Fast (4), Very Fast (5) or Fastest (6)\nChoose a text speed: ")
    
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

      choose_ts()
    
    choose_name()
  
  #Lets the player choose their name
  def choose_name():
    player_name = modified_input("What's your name?\n")

    slowprint("\nOkay " + player_name + ", let's embark on an adventure!")
    
    time.sleep(1)
    
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    
    time.sleep(0.1)
    
    intro()
  
  #Introduction to the text adventure
  def intro():
    def introtext1():
      slowprint("You're a millionair and retired CIA agent. You were one of the best fighters ofas the entire CIA. But you're not as skillfull as you were 25 years ago. You're 55 years old now. It's been 3 years since you retired. You've just been enjoying life since then. But that is all going to change.\n\n")

      input("[PRESS ENTER FOR NEXT PAGE]")

      os.system('cls' if os.name == 'nt' else "printf '\033c'")

      introtext2()


    def introtext2():
      slowprint("One morning, you wake up. When you analyse the situation, you notice that you're not in your bed, you're sitting in a chair. Also, you don't know this place. It's a room with no windows. Now, you also feel your ankles and torso have been tied to the chair that you're sitting in. You hear deep voices talking in the background. Maybe they're criminals who kidnapped you for your money. Or perhaps they want classified information about the CIA. You have no idea how or why you're in this situation. But you know that you have to get out of here as soon as possible.\n\n")

      ENTER_or_B = modified_input("[ENTER B FOR LAST PAGE / PRESS ENTER FOR NEXT PAGE]")

      os.system('cls' if os.name == 'nt' else "printf '\033c'")

      if ENTER_or_B == "B":
        introtext1()
      
      else:
        introtext3()

    def introtext3():
      slowprint("You don't feel any weapons on you, so you start to examine the room.\n")
      slowprint("You find you're sitting exactly in the centre of the room.\n")
      slowprint("You see a machete on the table against the wall approximately 2 metres to your left. One of the kidnappers must have forgotten about it.\n")
      slowprint("There's a handgun on the ground about 1,5 metres in front of you.\n")
      slowprint("And some tools hanging from the wall roughly 2 metres to your right-hand side.\n")
      slowprint("There's two possible exits, the wall in front you has a door on the right side. And there is a vent in the ceiling close to where the handgun is located.\n\n")

      ENTER_or_B = modified_input("[ENTER B FOR LAST PAGE / PRESS ENTER FOR NEXT PAGE]")

      os.system('cls' if os.name == 'nt' else "printf '\033c'")

      if ENTER_or_B == "B":
        introtext2()
      
      else:
        IntroQuestion()
    
    introtext1()

  #First question of the game
  def IntroQuestion():
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    
    if not player_freed:
      IntroInput = modified_input("What will you do?\nA. Hop over to machete\nB. Reach for handgun\nC. Go to tools\nD. Move to door and try to open it\nE. Go to the vent\n")

    elif player_freed:
      IntroInput = modified_input("What will you do?\nA. Hop over to machete\nB. Reach for handgun\nC. Go to tools\nD. Move to door and try to open it\nE. Go to the vent\n")

    if IntroInput == "A":
      Machete()

    elif IntroInput == "B":
      Handgun()

    elif IntroInput == "C":  
      Tools()

    elif IntroInput == "D":
      slowprint("You bump against the door and it opens. You see two armed men staring down at you.\nYOU WERE KNOCKED UNCONCIOUS\n\n")

      input("[PRESS ENTER TO CONTINUE]")

      IntroQuestion()

    elif IntroInput == "E":
      Vent()

    else:
      slowprint("Please choose A, B, C, D or E only.\n\n")

      time.sleep(1)
      
      IntroQuestion()

  #Question if player decided to go to machete 
  def Machete():
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    
    slowprint("You successfully made it to the table.\n\n")
    
    MacheteInput1 = modified_input("What will you do now?\nA. Kick the table until the machete falls off and cut the rope to free yourself.\nB. Try to grab the machete with your mouth and cut the rope to free yourself.\n")

    if MacheteInput1 == "A":
      slowprint("You hear the deep voices coming closer. You see two armed men enter the room. One runs towards you.\nYOU WENT UNCONCIOUS BY A TASER GUN\n\n")

      input("[PRESS ENTER TO CONTINUE]")
      
      IntroQuestion()
    
    elif MacheteInput1 == "B":
      
      player_inventory.append("MACHETE")

      slowprint("You've acquired the machete! You place it in your right hand and use it to cut the rope. You're now able to move about freely.")

      global player_freed
      player_freed = True

      input("[PRESS ENTER TO CONTINUE]")

      os.system('cls' if os.name == 'nt' else "printf '\033c'")

      def Machete2():
        MacheteInput2 = modified_input("Where will you go now?\nA. To the handgun.\nB. To the tools\nC. Through the door\n")

        if MacheteInput2 == "A":
          slowprint("You're at the handgun.")
          
          input("[PRESS ENTER TO CONTINUE]")

          os.system('cls' if os.name == 'nt' else "printf '\033c'")

          Handgun()
        
        elif MacheteInput2 == "B":
          slowprint("You made it to the tools.\n\n")

          input("[PRESS ENTER TO CONTINUE]")
          
          os.system('cls' if os.name == 'nt' else "printf '\033c'")
          
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
    slowprint("You're at the handgun.")

    if not player_freed:
      slowprint("You can't reach it. You'll need to cut the rope and free yourself.\n\n")

      IntroQuestion()
    
    elif player_freed:
      HandgunInput1 = modified_input("Will you grab the handgun? [Y/N]\n")

      if HandgunInput1 in AnsYes:
        player_inventory.append("HANDGUN")

        slowprint("It's is a fake. You take it anyway.")
      
      elif HandgunInput1 in AnsNo:
        def Handgun2():
          HandgunInput2 = modified_input("You left the handgun on the ground.\n\nWhere will you go now?\nA. To the door\nB. To the Tools\nC. To the vent D. Back to the handgun")

          if HandgunInput2 == "A":
            slowprint("You open the door cautiously and see two startled armed men.\nYOU WERE SHOT AT AGGRESSIVELY WITH A RIFLE\n\n")

            input("[PRESS ENTER TO RESPAWN]")
            
            os.system('cls' if os.name == 'nt' else "printf '\033c'")
            
            Handgun2()

          if HandgunInput2 == "B":
            slowprint("You made it to the tools.\n\n")

            input("[PRESS ENTER TO CONTINUE]")
            
            os.system('cls' if os.name == 'nt' else "printf '\033c'")
            
            Tools()

          elif HandgunInput2 == "C":
            Vent()
          
          elif HandgunInput2 == "D":
            Handgun()
          
          else:
            slowprint("Please choose A, B, C or D only.\n\n")

            time.sleep(1)

            Handgun2()
        
        Handgun2()

  #Question if player decided to go to tools
  def Tools():
    slowprint("You made it to the tools.\n\n")

    slowprint("There's screwdrivers, hammers and crowbars.\n\n")

    if not player_freed:
      slowprint("But unfortunately, you aren't able to grab any of them now. You'll need to free yourself first.")

      IntroQuestion()
    
    elif player_freed:
      ToolCheck = any(item in player_inventory for item in ToolsList)

      if ToolCheck is True:
        ToolSwitch = modified_input("Would you like to switch?\n")

        if ToolSwitch in AnsYes:
          player_inventory.remove(tool for tool in ToolsList in player_inventory)
          
          Tools()

        elif ToolSwitch in AnsNo:
          slowprint("You kept the " + tool for tool in ToolsList in player_inventory + ".")

      elif ToolCheck is False:
        ToolsInput1 = modified_input("You're only able to hold one tool at a time. Which tool will you grab?\nA. A screwdriver\nB. A hammer\nC. A crowbar\n")

        if ToolsInput1 == "A":
          player_inventory.append("SCREWDRIVER")

          slowprint("\n\nYou obtained a screwdriver!\n\n")

        elif ToolsInput1 == "B":
          player_inventory.append("HAMMER")

          slowprint("\n\nYou obtained a hammer!\n\n")

        elif ToolsInput1 == "C":
          player_inventory.append("CROWBAR")

          slowprint("\n\nYou obtained a crowbar!\n\n")

        else:
          slowprint("Please choose A, B or C only.\n\n")
          time.sleep(1)
          Tools()

        def Tools2():
          if "HANDGUN" in player_inventory:
            ToolsInput2 = modified_input("Where will you go now?\nA. Through the door\nB. To the vent\n")

          elif "HANDGUN" not in player_inventory:
            ToolsInput2 = modified_input("Where will you go now?\nA. Through the door\nB. To the vent\nC. To the handgun")

          if ToolsInput2 == "A":
            slowprint("You open the door cautiously and see two startled armed men.\nYOU WERE SHOT AT AGGRESSIVELY WITH A RIFLE\n\n")

            input("[PRESS ENTER TO RESPAWN]")
            
            os.system('cls' if os.name == 'nt' else "printf '\033c'")
            
            Tools2()
          
          elif ToolsInput2 == "B":
            Vent()

          elif "HANDGUN" not in player_inventory and ToolsInput2 == "C":
            slowprint("You're at the handgun.")

            input("[PRESS ENTER TO CONTINUE]")
            
            os.system('cls' if os.name == 'nt' else "printf '\033c'")
            
            Handgun()
          
          else:
            slowprint("Please choose A, B or C only.\n\n")
            
            time.sleep(1)
            
            Tools2()

        Tools2()
  
  #If player goes to vent
  def Vent():
    slowprint("You now close to the vent.")
    
    if not player_freed:
      
      slowprint("")
    
    elif player_freed:
      slowprint("But you can't do anything here right now.\n\n")


  #Runs first function of the game
  choose_ts()

#Runs the game
start_game()