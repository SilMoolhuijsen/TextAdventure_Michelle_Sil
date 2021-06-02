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

    #Valid textspeeds
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
    #If input was invalid
    else:
      slowprint(txt.Invalid_ts)

      time.sleep(0.5)

      #Recalls 'choose_ts' function
      choose_ts()
    
    #Calls next function in the game
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
    #First part of the intro
    def introtext1():
      slowprint(txt.IntroText1)

      input(txt.EnterForNextPage)
      
      ClearConsole()

      introtext2()

    #Second part of the intro
    def introtext2():
      slowprint(txt.IntroText2)

      ENTER_or_B = modified_input(txt.B_or_ENTER)

      ClearConsole()

      if ENTER_or_B == "B":
        introtext1()
      
      else:
        introtext3()

    #Third part of the intro (global)
    global introtext3
    def introtext3():
      slowprint(txt.IntroText3)

      BorEnter = modified_input(txt.B_or_start)

      ClearConsole()

      if BorEnter == "B":
        introtext2()
      
      else:
        #Calls first function with a decision
        Centre()
    
    #Calls part 1 of the intro
    introtext1()

  #First choice of the game (allows player to move across first area/room)
  def Centre():
    ClearConsole()
    
    #Question if player is not freed
    if not player_freed:
      IntroInput = modified_input(txt.MoveQuestion_NotFreed)

    #Question if player is freed
    elif player_freed:
      #Global question is a list so it can be edited more easily
      global MoveQuestion
      global Q, machete, handgun, tools, door, vent
      MoveQuestion = Q, machete, handgun, tools, door, vent = ["What will you do?", "A. Walk to the machete", "B. Go to the handgun", "C. Walk over to the tools", "D. Move to the door and try to open it", "E. Go to the vent"]
      
      for element in MoveQuestion:
        IntroInput = modified_input(element)

    #Outcomes for valid inputs
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

    #If input was invalid
    else:
      slowprint(txt.ABCDE_Only)

      time.sleep(1)
      
      Centre()


  #If player chooses to go to machete 
  def Machete():
    ClearConsole()
    
    slowprint(txt.MacheteTable)
    
    MacheteInput1 = modified_input(txt.MacheteQuestion)

    #Outcomes for valid inputs
    if MacheteInput1 == "A":
      slowprint(txt.MacheteDead)

      input(txt.PR_ENT)

      global dead
      dead = True
      
      #Game over
      #the player has died / been knocked unconcious
      #Calls 'game_over' function
      game_over()
    
    elif MacheteInput1 == "B":
      #Adds 'MACHETE' to player_inventory
      player_inventory.append("MACHETE")
      
      #Removes 'MACHETE' from moving question
      MoveQuestion.remove(Machete)

      slowprint(txt.MacheteFreed)

      #Tells the game that the player is now freed
      global player_freed
      player_freed = True

      input(txt.ENTtoCON)
    
    else:
      slowprint(txt.AB_Only)

      time.sleep(1)
      
      Machete()
    
    Centre()


  #If player decides to go to handgun
  def Handgun():
    ClearConsole()

    slowprint(txt.atHG)

    if not player_freed:
      slowprint(txt.HG_NotFreed)
    
    elif player_freed:
      HandgunInput1 = modified_input(txt.Grab_HG)

      if HandgunInput1 in AnsYes:
        player_inventory.append("HANDGUN")

        MoveQuestion.remove("handgun")

        slowprint(txt.ProbablyFake)
      
      elif HandgunInput1 in AnsNo:
        slowprint(txt.Left_HG)
      
      else:
        slowprint(txt.ENT_Y_N)

        time.sleep(1)
      
        Handgun()
      
    Centre()


  #If player decides to go to tools
  def Tools():
    ClearConsole()

    slowprint(txt.atTools)

    slowprint(txt.TheTools)

    if not player_freed:
      slowprint(txt.Tools_NotFreed)
    
    elif player_freed:
      #Checks for any tools in the player's inventory
      ToolCheck = any(item in player_inventory for item in ToolsList)

      #If the player doesn't have any tools
      if ToolCheck is False:
        def ToolGrab():
          ClearConsole()

          ToolsInput1 = modified_input()

          if ToolsInput1 == "A":
            player_inventory.append("SCREWDRIVER")

            slowprint()

          elif ToolsInput1 == "B":
            player_inventory.append("HAMMER")

            slowprint()

          elif ToolsInput1 == "C":
            player_inventory.append("CROWBAR")

            slowprint()

          else:
            slowprint()

            time.sleep(1)
            
            ToolGrab()
        
        ToolGrab()

      #If the player has a tool
      elif ToolCheck is True:
        #While loop for question
        while True:
          #Asks if the player would like to switch tools
          ToolSwitch = modified_input(txt.SwitchTool)

          #If the player wants to switch tools
          if ToolSwitch in AnsYes:
            player_inventory.remove(tool for tool in ToolsList in player_inventory)
            
            ToolGrab()

          #If the player doesn't want to switch tools
          elif ToolSwitch in AnsNo:
            slowprint("You kept the " + tool for tool in ToolsList in player_inventory + ".")

            time.sleep(1)

            #Breaks out of while loop
            break
          
          else:
            slowprint(txt.ENT_Y_N)

            time.sleep(1)

    Centre()


  #If player decides to go to vent
  def Vent():
    ClearConsole()

    slowprint(txt.atVent)
    
    if player_freed:
      #Checks for 'CHAIR_PLACED' in the player's inventory
      if "CHAIR_PLACED" not in player_inventory:
        #While loop
        while True:

          GetHigher = modified_input(txt.Higher)

          if GetHigher == "CHAIR" or "THECHAIR" or "ACHAIR":
            slowprint(txt.PlacedChair)

            break
          
          elif GetHigher == "TABLE" or "THETABLE" or "ATABLE":
            slowprint(txt.NoTable)
          
          else:
            slowprint(txt.CantUse)

            time.sleep(1)
          
          player_inventory.append("CHAIR_PLACED")
      
      else:
        while True:
          UseTool = modified_input("Will you use your" + str.lower(any(tool for tool in ToolsList in player_inventory)) + "to open the vent?")

          if UseTool in AnsYes:
            if "CROWBAR" in player_inventory:
              slowprint(txt.VentUsedCrowbar)

              input(txt.PR_ENT)

              global dead
              dead = True

              game_over()

            elif "HAMMER" in player_inventory:
              slowprint(txt.VentUsedHammer)
              
              time.sleep(1)

              break

            elif "SCREWDRIVER" in player_inventory:
              slowprint(txt.VentUsedScrewdriver)

              player_won()
              

            else:
              slowprint(txt.NoTools)

          elif UseTool in AnsNo:
            Centre()

          else:
            slowprint(txt.ENT_Y_N)

            time.sleep(1)
    
    elif not player_freed:
      slowprint(txt.CantDo)

      time.sleep(1)
 
    Centre()


  #If player chooses to go to door
  def Door():
    ClearConsole()

    if not player_freed:
      slowprint(txt.Door_NotFreed)

      input(txt.PR_ENT)

    elif player_freed:
      if "HANDGUN" in player_inventory:
        slowprint(txt.DoorHG1)
        
        input(txt.ENTtoCON)

        slowprint(txt.DoorHG2)

        global dead
        dead = True

        input(txt.PR_ENT)
      
      else:
        slowprint(txt.Door_Freed_NoHG)

        dead = True
        
        input(txt.PR_ENT)

    game_over()

  #Runs first function of the game (choosing the game's text speed)
  choose_ts()

def game_over():
  ClearConsole()

  if dead is True:
    slowprint(txt.GAMEOVER_KILLED)
  
  if dead is False:
    slowprint(txt.GAMEOVER_UNCONCIOUS)

  global player_won
  def player_won():
    try_again = modified_input(txt.Try_Again)

    if try_again in AnsYes:
      Restart()

    if try_again in AnsNo:
      exit()

#Runs the game
start_game()