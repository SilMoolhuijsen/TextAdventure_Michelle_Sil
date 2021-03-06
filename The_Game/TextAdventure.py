#imports modules
import time
import os
import sys
import TextData

#This means that we'll only have to type txt. instead of TextData when we're entering text from the TextData file in a printlike statement
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

#List for multiple choice questions
ABCDE = ["A.", "B.", "C.", "D.", "E."]

#Lists with some items
ToolsList = ["SCREWDRIVER", "HAMMER", "CROWBAR"]

#List that stores all of the player's items
player_inventory = []

#Defines RestartAnswer to avoid errors
RestartAnswer = ""

#Function that prints strings letter by letter
def slowprint(s, l = None):
  if l == list:
    for letter in s + "\n":
      sys.stdout.write(letter)

      sys.stdout.flush()

      if letter in COMMA:
        time.sleep(ts * 8)

      elif letter in END_SENTENCE:
        time.sleep(ts * 16)

      else:
        time.sleep(ts)

  else:
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

  a = a.replace(" ", "")
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

  #Tells game that the player started over and has to win again
  global PlayerWon
  PlayerWon = False

  #For if player wants to try again after a game over
  if RestartAnswer == "Y":
    #Clears the player's inventory
    global player_inventory
    player_inventory.clear()
    #Waits for 0.4 seconds
    time.sleep(0.4)
    #Runs introtext3, to skip first part of the intro when player restarts
    introtext3()

  else:
    pass

  #Lets the player choose the game's text speed
  def choose_ts():
    #Globalizes variable 'ts'
    global ts
    #Sets 'ts' to 0.0075 for the start of the game
    ts = 0.005

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

    modified_input(txt.ENTtoCON)

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

      if BorEnter == "B":
        ClearConsole()

        introtext2()

      else:
        #Calls first function with a decision
        Centre()

    #Calls part 1 of the intro
    introtext1()

  #First choice of the game (allows player to move across first area/room)
  global Centre
  def Centre():
    ClearConsole()

    #Question for after the player is freed is a global list so it can be edited more easily
    global MoveQuestion
    global Q, machete, handgun, tools, door, vent
    MoveQuestion = Q, machete, handgun, tools, door, vent = ["Where will you go?", "A. Machete","B. Handgun", "C. Tools","D. Open the door", "E. Vent"]

    #Question if player is freed
    if player_freed:
      #Prints MoveQuestion
      for e in MoveQuestion:
        slowprint(e, list)
      #Stores user input in variable
      IntroInput = modified_input("")

    #Question if player is not freed
    elif not player_freed:
      IntroInput = modified_input(txt.MoveQuestion_NotFreed)

    #Outcomes for valid inputs
    if IntroInput == "A":
      if "MACHETE" in player_inventory:
        slowprint(txt.AlreadyMachete)
        
        modified_input(txt.ENTtoCON)
        
        Centre()

      else:
        Machete()
      
    elif IntroInput == "B":
      if "HANDGUN" in player_inventory:
        slowprint(txt.AlreadyHG)
        
        modified_input(txt.ENTtoCON)
        
        Centre()
      
      else:
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
      ClearConsole()

      slowprint(txt.MacheteKnocked)

      input(txt.PR_ENT)

      #Game over
      #the player has been knocked unconcious
      #Calls 'game_over' function
      game_over()

    elif MacheteInput1 == "B":
      #Adds 'MACHETE' to player_inventory
      global player_inventory
      player_inventory.append("MACHETE")

      #Removes 'MACHETE' from moving question
      global MoveQuestion
      MoveQuestion.remove(machete)

      slowprint(txt.MacheteFreed)

      #Tells the game that the player is now freed
      global player_freed
      player_freed = True

      modified_input(txt.ENTtoCON)

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

      modified_input(txt.ENTtoCON)

    elif player_freed:
      HandgunInput1 = modified_input(txt.Grab_HG)

      if HandgunInput1 in AnsYes:
        global player_inventory
        player_inventory.append("HANDGUN")

        global MoveQuestion
        MoveQuestion.remove(handgun)
        
        slowprint(txt.ProbablyFake)

        modified_input(txt.ENTtoCON)

      elif HandgunInput1 in AnsNo:
        slowprint(txt.Left_HG)

        modified_input(txt.ENTtoCON)

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

      modified_input(txt.ENTtoCON)

    elif player_freed:
      #Checks for any tools in the player's inventory
      ToolCheck = any(tool in player_inventory for tool in ToolsList)

      #If the player doesn't have any tools
      if not ToolCheck:
        
        global ToolGrab
        def ToolGrab():
          ClearConsole()

          ToolsInput1 = modified_input(txt.ChooseTool)

          if ToolsInput1 == "A":
            global player_inventory
            player_inventory.append("SCREWDRIVER")

            slowprint(txt.GotScrewdriver)

            modified_input(txt.ENTtoCON)

          elif ToolsInput1 == "B":
            player_inventory.append("HAMMER")

            slowprint(txt.GotHammer)

            modified_input(txt.ENTtoCON)

          elif ToolsInput1 == "C":
            player_inventory.append("CROWBAR")

            slowprint(txt.GotCrowbar)

            modified_input(txt.ENTtoCON)

          else:
            slowprint(txt.ABC_Only)

            time.sleep(1)

            ToolGrab()
          
          Centre()

        ToolGrab()

      #If the player has a tool
      elif ToolCheck:
        #Finds Tool
        CurrentTool = list(set(player_inventory).intersection(ToolsList))
        
        #Converts tool to a lowercase string
        PlayerTool = str.lower(CurrentTool[0])

        #While loop for question
        while True:
          global SwitchTool
          SwitchTool = False

          #Asks if the player would like to switch tools
          ToolSwitch = modified_input(txt.SwitchTool)

          #If the player wants to switch tools
          if ToolSwitch in AnsYes:            
            player_inventory.remove(str(CurrentTool[0]))

            SwitchTool = True

            #Breaks out of while loop
            break

          #If the player doesn't want to switch tools
          elif ToolSwitch in AnsNo:
            slowprint("You kept the " + PlayerTool + ".")

            modified_input(txt.ENTtoCON)

            break

          else:
            slowprint(txt.ENT_Y_N)

            time.sleep(1)
          
        if SwitchTool:
          ToolGrab()


    Centre()

  #If player decides to go to vent
  def Vent():
    ClearConsole()

    slowprint(txt.atVent)

    #Possible answers
    Chair = ["CHAIR","THECHAIR","ACHAIR"]
    Table = ["TABLE","THETABLE","ATABLE"]

    if player_freed:
      global player_inventory

      #Checks for 'CHAIR_PLACED' in the player's inventory
      if "CHAIR_PLACED" not in player_inventory:
        ClearConsole()
        
        #Sets i to 0
        i = 0

        #While loop
        while True:
          if i == 0:
            GetHigher = modified_input(txt.GetHigher)
            i += 1

          else:
            GetHigher = modified_input(txt.Higher)

          if GetHigher in Chair:
            slowprint(txt.PlacedChair)

            modified_input(txt.ENTtoCON)

            player_inventory.append("CHAIR_PLACED")

            break

          elif GetHigher in Table:
            slowprint(txt.NoTable)

            time.sleep(2)

          else:
            slowprint(txt.CantUse)

            time.sleep(1)

      else:
        while True:
          CurrentTool = list(set(player_inventory).intersection(ToolsList))

          PlayerTool = str.lower(CurrentTool[0])
          
          UseTool = modified_input("Will you use your " + PlayerTool + " to open the vent?\n")

          if UseTool in AnsYes:
            if "CROWBAR" in player_inventory:
              slowprint(txt.VentUsedCrowbar)

              input(txt.PR_ENT)

              global dead
              dead = True

              game_over()

            elif "HAMMER" in player_inventory:
              slowprint(txt.VentUsedHammer)

              modified_input(txt.ENTtoCON)

              break

            elif "SCREWDRIVER" in player_inventory:
              slowprint(txt.VentUsedScrewdriver)

              #Tells the game that the player won
              global PlayerWon
              PlayerWon = True

              modified_input(txt.ENTtoCON)

              game_over()

            else:
              slowprint(txt.NoTools)

              modified_input(txt.ENTtoCON)

          elif UseTool in AnsNo:
            Centre()

          else:
            slowprint(txt.ENT_Y_N)

            time.sleep(1)

    elif not player_freed:
      slowprint(txt.CantDo)

      modified_input(txt.ENTtoCON)

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

        modified_input(txt.ENTtoCON)

        slowprint(txt.DoorHG2)

        global dead
        dead = True

        modified_input(txt.PR_ENT)

      else:
        slowprint(txt.Door_Freed_NoHG)

        dead = True

        modified_input(txt.PR_ENT)

    game_over()

  #Runs first function of the game (choosing the game's text speed)
  choose_ts()


def game_over():
  ClearConsole()

  global player_won
  def player_won():
    ClearConsole()

    try_again = modified_input(txt.Try_Again)

    if try_again in AnsYes:
      global RestartAnswer
      RestartAnswer = "Y"

      start_game()

    elif try_again in AnsNo:
      exit()
    
    else:
      player_won()

  if PlayerWon:
    player_won()

  elif dead:
    slowprint(txt.GAMEOVER_KILLED)

    modified_input(txt.PR_ENT)

    player_won()

  elif not dead:
    slowprint(txt.GAMEOVER_UNCONCIOUS)

    modified_input(txt.ENTtoCON)

    Centre()
  
  input(txt.PR_ENT)

#Runs the game
start_game()