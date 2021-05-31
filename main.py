#imports modules
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
    
    elif letter in END_SENTENCE:
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
  os.system('cls' if os.name == 'nt' else "printf '\033c'")

  #Tells game that the player is not freed at the beginning
  global player_freed
  player_freed = False

  #Tells game that the player is not dead at the beginning
  global dead
  dead = False

  #Function for if player wants to try again after game over
  global Restart
  def Restart():
    os.system('cls' if os.name == 'nt' else "printf '\033c'")

    global dead
    dead = False

    global player_freed
    player_freed = False
    
    player_inventory.clear()

    time.sleep(0.4)

    introtext3()

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
      slowprint("\nThat is not a valid text speed. Choose from Very Slow (1), Slow (2), Normal (3), Fast (4) or Very Fast (5).\n\n")

      time.sleep(0.5)

      choose_ts()
    
    choose_name()
  
  #Lets the player choose their name
  def choose_name():
    slowprint("What's your name?\n")

    player_name = input()

    slowprint("\nOkay " + player_name + ", let's embark on an adventure!\n\n")

    input("[PRESS ENTER TO CONTINUE]")
 
    os.system('cls' if os.name == 'nt' else "printf '\033c'")

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

      ENTER_or_B = modified_input("[ENTER B FOR LAST PAGE / PRESS ENTER FOR NEXT PAGE]\n")

      os.system('cls' if os.name == 'nt' else "printf '\033c'")

      if ENTER_or_B == "B":
        introtext1()
      
      else:
        introtext3()

    global introtext3
    def introtext3():
      slowprint("You don't feel any weapons on you, so you start to examine the room.\n")
      slowprint("You find you're sitting exactly in the centre of the room.\n")
      slowprint("You see a machete on the table against the wall approximately 2 metres to your left. One of the kidnappers must have forgotten about it.\n")
      slowprint("There's a handgun on the ground about 1,5 metres in front of you.\n")
      slowprint("And some tools hanging from the wall roughly 2 metres to your right-hand side.\n")
      slowprint("There's two possible exits, the wall in front you has a door on the right side. And there is a vent in the ceiling close to where the handgun is located.\n\n")

      ENTER_or_B = modified_input("[ENTER B FOR LAST PAGE / PRESS ENTER TO START ADVENTURE]\n")

      os.system('cls' if os.name == 'nt' else "printf '\033c'")

      if ENTER_or_B == "B":
        introtext2()
      
      else:
        Centre()
    
    introtext1()

  #First choice of the game (allows player to move across first area/room)
  def Centre():
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    
    if not player_freed:
      IntroInput = modified_input("What will you do?\nA. Hop over to the machete\nB. Reach for the handgun\nC. Go to the tools\nD. Move to the door and try to open it\nE. Go to the vent\n")

    elif player_freed:
      global MoveQuestion
      global Q, machete, handgun, tools, door, vent
      MoveQuestion = Q, machete, handgun, tools, door, vent = ["What will you do?", "A. Walk to the machete", "B. Go to the handgun", "C. Walk over to the tools", "D. Move to the door and try to open it", "E. Go to the vent"]
      
      for element in MoveQuestion:
        IntroInput = modified_input(element)

    if IntroInput == "A":
      Machete()

    elif IntroInput == "B":
      Handgun()

    elif IntroInput == "C":  
      Tools()

    elif IntroInput == "D":
      Door()

    elif IntroInput == "E":
      Vent()

    else:
      slowprint("\nPlease choose A, B, C, D or E only.")

      time.sleep(1)
      
      Centre()


  #If player chose to go to machete 
  def Machete():
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    
    slowprint("You successfully made it to the table.\n\n")
    
    MacheteInput1 = modified_input("What will you do now?\nA. Kick the table until the machete falls off and cut the rope to free yourself.\nB. Try to grab the machete with your mouth and cut the rope to free yourself.\n")

    if MacheteInput1 == "A":
      slowprint("You hear the deep voices coming closer. You see two armed men enter the room. One runs towards you.\nYOU WENT UNCONCIOUS BY A TASER GUN AND SHOT WITH A HANDGUN!\n\n")

      input("[PRESS ENTER]")

      global dead
      dead = True

      game_over()
    
    elif MacheteInput1 == "B":
      player_inventory.append("MACHETE")
      
      MoveQuestion.remove(Machete)

      slowprint("You've acquired the machete! You place it in your right hand and use it to cut the rope. You're now able to move about freely.")

      global player_freed
      player_freed = True

      input("[PRESS ENTER TO CONTINUE]")
    
    else:
      slowprint("\nPlease choose A or B only.")

      time.sleep(1)
      
      Machete()
    
    Centre()


  #If player decided to go to handgun
  def Handgun():
    os.system('cls' if os.name == 'nt' else "printf '\033c'")

    slowprint("You're at the handgun.\n\n")

    if not player_freed:
      slowprint("You can't reach it. You'll need to cut the rope to free yourself.\n\n")
    
    elif player_freed:
      HandgunInput1 = modified_input("Will you grab the it? [Y/N]\n")

      if HandgunInput1 in AnsYes:
        player_inventory.append("HANDGUN")

        MoveQuestion.remove("handgun")

        slowprint("You're pretty sure it's a fake, but you take it anyways.")
      
      elif HandgunInput1 in AnsNo:
        slowprint("You left the handgun on the ground")
      
      else:
        slowprint("\nPlease choose Yes or No only.")

        time.sleep(1)
      
        Handgun()
      
    Centre()


  #If player decided to go to tools
  def Tools():
    slowprint("You made it to the tools.\n\n")

    slowprint("There's screwdrivers, hammers and crowbars.\n\n")

    if not player_freed:
      slowprint("But unfortunately, you aren't able to grab any of them now. You'll need to free yourself first.")
    
    elif player_freed:
      ToolCheck = any(item in player_inventory for item in ToolsList)

      if ToolCheck is False:
        def ToolGrab():
          os.system('cls' if os.name == 'nt' else "printf '\033c'")

          ToolsInput1 = modified_input("You're only able to hold one tool at a time. Which tool will you grab?\nA. Screwdriver\nB. Hammer\nC. Crowbar\n")

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
            slowprint("\nPlease choose A, B or C only.")

            time.sleep(1)
            
            ToolGrab()

      elif ToolCheck is True:
        ToolSwitch = modified_input("Would you like to switch?\n")

        if ToolSwitch in AnsYes:
          player_inventory.remove(tool for tool in ToolsList in player_inventory)
            
          ToolGrab()

        elif ToolSwitch in AnsNo:
          slowprint("You kept the " + tool for tool in ToolsList in player_inventory + ".")

    Centre()


  #If player decided to go to vent
  def Vent():
    os.system('cls' if os.name == 'nt' else "printf '\033c'")

    slowprint("You're now close to the vent.")
    
    if not player_freed:
      
      slowprint("")
    
    elif player_freed:
      slowprint("But you can't do anything here right now.\n\n")

      Centre()
    


  #If player chose to go to door
  def Door():
    os.system('cls' if os.name == 'nt' else "printf '\033c'")

    if not player_freed:
      slowprint("You bump against the door and it opens. You see two armed men staring down at you.\nYOU WERE KNOCKED UNCONCIOUS WITH A WOODEN BASEBALL BAT!\n\n")

      input("[PRESS ENTER]")
          
    elif player_freed:
      if "HANDGUN" in player_inventory:
        slowprint("When get closer to the door, you notice the deep voices getting louder, so you get ready. You grab your probably fake handgun with your right hand and tighly grasp your machete with with the other.\n\n")
        
        input("[PRESS ENTER TO CONTINUE]\n\n")

        slowprint("You storm into the room on the other side of the door and see two armed men. You act as if your sure your handgun is real and aim it at the right man's head. But before you can plan your next action, your throat is slit by a third man you didn't notice.\n\nYOUR THROAT WAS SLIT USING A DAGGER!\n\n")

        global dead
        dead = True

        input("[PRESS ENTER]")
      
      else:
        slowprint("You open the door cautiously and see two startled armed men.\nYOU WERE SHOT AT AGGRESSIVELY WITH A SILENCED RIFLE!\n\n")

        global dead
        dead = True
        
        input("[PRESS ENTER]")

    game_over()  

  #Runs first function of the game (choosing the game's text speed)
  choose_ts()

def game_over():
  os.system('cls' if os.name == 'nt' else "printf '\033c'")

  if dead is True:
    slowprint("You were killed!\n\nGAME OVER")
  
  if dead is False:
    slowprint("You were knocked unconcious!\n\nGAME OVER")

  try_again = modified_input("Would you like to try again? [Y/N]\n")

  if try_again in AnsYes:
    Restart()

  if try_again in AnsNo:
    pass

#Runs the game
start_game()