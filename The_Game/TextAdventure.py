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
def modified_input(s, s_or_l = None):
  if s_or_l is None:
    slowprint(s)

  elif s_or_l == "l":
    for e in s:
      print(e)

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

  #Defines RestartAnswer to avoid errors
  RestartAnswer = ""

  #For if player wants to try again after a game over
  if RestartAnswer == "Y":
    #Clears the player's inventory
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

      if BorEnter == "B":
        ClearConsole()

        introtext2()

      else:
        #Calls first function with a decision
        Centre()

    #Calls part 1 of the intro
    introtext1()

  #First choice of the game (allows player to move across first area/room)
  def Centre():
    ClearConsole()

    #Variable that stores the number of times player has called Centre()
    CentreCounter = 0

    #Question for after the player is freed is a global list so it can be edited more easily
    global MoveQuestion
    global Q, machete, handgun, tools, door, vent
    MoveQuestion = Q, machete, handgun, tools, door, vent = ["Where will you go?", "A. Machete","B. Handgun", "C. Tools","D. Open the door", "E. Vent"]

    #Fixes MoveQuestion
    if CentreCounter > 0:
      global x
      n = 0
      for e in MoveQuestion:
        MoveQuestion.e.replace((l for l in ABCDE), x)

        if n > 0:
          x = ABCDE[n - 1]

        n += 1
    
    #Adds 1 to CentreCounter
    CentreCounter += 1

    #Question if player is freed
    if player_freed:
      #Prints MoveQuestion
        IntroInput = modified_input(MoveQuestion, s_or_l = "l")

    #Question if player is not freed
    elif not player_freed:
      IntroInput = modified_input(txt.MoveQuestion_NotFreed)

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
      ClearConsole()

      slowprint(txt.MacheteKnocked)

      input(txt.PR_ENT)

      #Game over
      #the player has been knocked unconcious
      #Calls 'game_over' function
      game_over()

    elif MacheteInput1 == "B":
      #Adds 'MACHETE' to player_inventory
      player_inventory.append("MACHETE")

      #Removes 'MACHETE' from moving question
      MoveQuestion.remove(machete)

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

        MoveQuestion.remove(handgun)

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
      ToolCheck = any(tool in player_inventory for tool in ToolsList)

      #If the player doesn't have any tools
      if not ToolCheck:

        def ToolGrab():
          ClearConsole()

          ToolsInput1 = modified_input(txt.ChooseTool)

          if ToolsInput1 == "A":
            player_inventory.append("SCREWDRIVER")

            slowprint(txt.GotScrewdriver)

          elif ToolsInput1 == "B":
            player_inventory.append("HAMMER")

            slowprint(txt.GotHammer)

          elif ToolsInput1 == "C":
            player_inventory.append("CROWBAR")

            slowprint(txt.GotCrowbar)

          else:
            slowprint(txt.ABC_Only)

            time.sleep(1)

            ToolGrab()
          
          Centre()

        ToolGrab()

      #If the player has a tool
      elif ToolCheck:
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

  if dead:
    slowprint(txt.GAMEOVER_KILLED)

  elif not dead:
    slowprint(txt.GAMEOVER_UNCONCIOUS)

  global player_won
  def player_won():
    try_again = modified_input(txt.Try_Again)

    if try_again in AnsYes:
      global RestartAnswer
      RestartAnswer = "Y"

    elif try_again in AnsNo:
      exit()

  input(txt.PR_ENT)

#Runs the game
start_game()