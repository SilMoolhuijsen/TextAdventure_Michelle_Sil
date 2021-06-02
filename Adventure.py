#imports modules
import time
import os
import sys
import TextData

txt = TextData

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
def modified_input(s):
  slowprint(s)

  a = input()

  a = a.replace(" ","")
  a = a.upper()
  
  return a

#Function that clears the console
def ClearConsole():
  os.system('cls' if os.name == 'nt' else "printf '\033c'")

#Function to (re)run the game
def start_game():
  ClearConsole()

  #Tells game that the player is not freed at the beginning
  global player_freed
  player_freed = False

  #Tells game that the player is not dead at the beginning
  global dead
  dead = False

  #Global function for if player wants to try again after a game over
  global Restart
  def Restart():
    ClearConsole()

    #Tells game that player is alive again
    global dead
    dead = False

    #Tells game that player is tied up again
    global player_freed
    player_freed = False
    
    #Clears Players
    player_inventory.clear()

    #Waits for 0.4 seconds
    time.sleep(0.4)

    #Runs introtext3, to skip first part of the intro when player restarts
    introtext3()

  #Lets the player choose the game's text speed
  def choose_ts():
    #Globalizes variable 'ts'
    global ts
    #Sets 'ts' to 0.0075 for the start of the game
    ts = 0.0075

    #Variable that stores the player's chosen text speed
    TextSpeed = modified_input(txt.WhichTextSpeed)
    
    ClearConsole()

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
      slowprint(txt.Invalid_ts)

      time.sleep(0.5)

      #Recalls function
      choose_ts()
    
    #Calls next function
    choose_name()
  
  #Lets the player choose their name
  def choose_name():
    slowprint(txt.Ask_Name)

    #Stores player's username
    player_name = input()

    slowprint("\nOkay " + player_name + txt.LetsGo)

    input(txt.ENTtoCON)

    ClearConsole()

    intro()

  #Introduction to the text adventure
  def intro():
    def introtext1():
      slowprint(txt.IntroText1)

      input(txt.EnterForNextPage)
      
      ClearConsole()

      introtext2()
        


    def introtext2():
      slowprint(txt.IntroText2)

      ENTER_or_B = modified_input(txt.B_or_Enter)

      ClearConsole()

      if ENTER_or_B == "B":
        introtext1()
      
      else:
        introtext3()

    global introtext3
    def introtext3():
      slowprint(txt.IntroText3)

      BorEnter = modified_input(txt.B_or_start)

      ClearConsole()

      if BorEnter == "B":
        introtext2()
      
      else:
        Centre()
    
    introtext1()

  #First choice of the game (allows player to move across first area/room)
  def Centre():
    ClearConsole()
    
    if not player_freed:
      IntroInput = modified_input(txt.MoveQuestion_PlayerNotFreed)

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
    ClearConsole()
    
    slowprint(txt.MacheteTable)
    
    MacheteInput1 = modified_input(txt.MacheteQuestion)

    if MacheteInput1 == "A":
      slowprint(txt.MacheteDead)

      input(txt.PR_ENT)

      global dead
      dead = True

      game_over()
    
    elif MacheteInput1 == "B":
      player_inventory.append("MACHETE")
      
      MoveQuestion.remove(Machete)

      slowprint(txt.MacheteFreed)

      global player_freed
      player_freed = True

      input(txt.ENTtoCON)
    
    else:
      slowprint("\nPlease choose A or B only.")

      time.sleep(1)
      
      Machete()
    
    Centre()


  #If player decided to go to handgun
  def Handgun():
    ClearConsole()

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
          ClearConsole()

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
    ClearConsole()

    slowprint("You're now close to the vent.\n")
    
    if player_freed:
      if "CHAIR_PLACED" not in player_inventory:
        while True:
          GetHigher = modified_input("But you can't reach it. What will you use to get higher?")

          if GetHigher == "CHAIR" or "THECHAIR":
            slowprint("You placed the chair underneath the vent. You can reach it now!")

            break
          
          else:
            slowprint("You can't use that!\nPlease try again.")

            continue
          
          player_inventory.append("CHAIR_PLACED")
      
      else:
        while True:
          UseTool = modified_input("Will you use your" + str.lower(any(tool for tool in ToolsList in player_inventory)) + "to open the vent?")

          if UseTool in AnsYes:
            if "CROWBAR" in player_inventory:
              slowprint("You used the crowbar to open the vent. However, you were too loud. Two armed men storm through the door.\nYOU WERE SHOT AT AGGRESIVELY WITH A SILENCED RIFLE!")

              input("[PRESS ENTER]")

              global dead
              dead = True
              game_over()

            elif "HAMMER" in player_inventory:
              slowprint("You can't use the hammer to open the vent. Try a different tool.")
              
              break

            elif "SCREWDRIVER" in player_inventory:
              slowprint("You carefully loosened the screws of the vent. You succesfully managed to climb into the vent. You start to crawl, and slowly, you see light appearing from the end of the vent.\n\nYOU MADE IT OUT!\n\nCONGRATULATIONS, YOU'VE WON!")

              player_won()
              

            else:
              slowprint("You don't have any tools on you!")

          elif UseTool in AnsNo:
            Centre()

          else:
            slowprint("Please enter either yes or no.")

            time.sleep(1)

            continue

    
    elif not player_freed:
      slowprint("But you can't do anything here right now.\n\n")

      Centre()
    


  #If player chose to go to door
  def Door():
    ClearConsole()

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

        dead = True
        
        input("[PRESS ENTER]")

    game_over()  

  #Runs first function of the game (choosing the game's text speed)
  choose_ts()

def game_over():
  ClearConsole()

  if dead is True:
    slowprint("You were killed!\n\nGAME OVER")
  
  if dead is False:
    slowprint("You were knocked unconcious!\n\nGAME OVER")

  global player_won
  def player_won():
    try_again = modified_input("Would you like to try again? [Y/N]\n")

    if try_again in AnsYes:
      Restart()

    if try_again in AnsNo:
      pass

#Runs the game
start_game()