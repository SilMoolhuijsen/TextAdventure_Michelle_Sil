import time
import os
import sys
import Classes

txtSpeed5 = ["Very Fast", "very fast", "very Fast", "Very fast", "5"]
txtSpeed4 = ["Fast", "fast", "4"]
txtSpeed3 = ["Normal", "normal", "3"]
txtSpeed2 = ["Slow", "slow", "2"]
txtSpeed1 = ["Very Slow", "very slow", "very Slow", "Very slow", "1"]
txtSpeed6 = ["Fastest", "fastest", "6"]
END_SENTENCE = [".", "!", "?"]
COMMA = ","
AnswerA = ["A", "a", "A.", "a."]
AnswerB = ["B", "b", "B.", "b."]
AnswerC = ["C", "c", "C.", "c."]
AnswerD = ["D", "d", "D.", "d."]
inventory = []

def start_game():
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
    TextSpeed = slowprint("Choose a text speed, Very Slow (1), Slow (2), Normal (3), Fast (4), Very Fast (5) or Fasterst (6): ")
    TextSpeed = input()
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
    
    def start():
      def choose_name():
        slowprint("What's your name?\n")
        user_name = input()
        slowprint("\nOkay " + user_name + ", let's embark on an adventure!")
        time.sleep(1.5)
        os.system('cls' if os.name == 'nt' else "printf '\033c'")
        time.sleep(0.5)
        intro()
      
      def intro():
        slowprint("You're a millionair and retired CIA agent. You were one of the best fighters ofas the entire CIA. But you're not as skillfull as you were 25 years ago. You're 55 years old now. It's been 3 years since you retired. You've just been enjoying life since then. But that is all going to change.\n\n")
        input("[PRESS ENTER TO CONTINUE]")
        slowprint("\nOne morning, you wake up. When you analyse the situation, you notice that you're not in your bed, you're sitting in a chair. Also, you don't know this place. It's a room with no windows. Now, you also feel your ankles and torso have been tied to the chair that you're sitting in. You hear deep voices talking in the background. Maybe they're criminals who kidnapped you for your money. Or perhaps they want classified information about the CIA. You have no idea how or why you're in this situation. But you know that you have to get out of here as soon as possible.\n\n")
        input("[PRESS ENTER TO CONTINUE]")
        slowprint("\nYou don't feel any weapons on you, so you start to examine the room.\n")
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

      def IntroQuestion():
        IntroInput = slowprint("What will you do?\nA. Hop over to machete.\nB. Reach for handgun.\nC. Go to tools.\nD. Move to door and try to open it.\n\nAnswer: ")
        IntroInput = input()
        if IntroInput in AnswerA:
          slowprint("You successfully made it to the table.\n\n")
          input("[PRESS ENTER TO CONTINUE]")
          os.system('cls' if os.name == 'nt' else "printf '\033c'")
          Machete()
        elif IntroInput in AnswerB:
          slowprint("You're at the handgun, but you can't reach it. You'll need to cut the rope and free yourself.\n\n")
          input("[PRESS ENTER TO CONTINUE]")
          os.system('cls' if os.name == 'nt' else "printf '\033c'")
          Handgun()
        elif IntroInput in AnswerC:  
          slowprint("You made it to the tools. There's a screwdriver, hammer, knife and crowbar.\n\n")
          input("[PRESS ENTER TO CONTINUE]")
          os.system('cls' if os.name == 'nt' else "printf '\033c'")
          Tools()
        elif IntroInput in AnswerD:
          slowprint("You bump against the door and it opens. You see two armed men staring down at you.\nYOU WERE KNOCKED UNCONCIOUS\n\n")
          input("[PRESS ENTER TO RESPAWN]")
          os.system('cls' if os.name == 'nt' else "printf '\033c'")
          IntroQuestion()
        else:
          slowprint("Please choose A, B, C or D only.\n\n")
          time.sleep(1)
          IntroQuestion()

      def Machete():
        MacheteInput1 = slowprint("What will you do now?\nA. Kick the table until the machete falls off and cut the rope to free yourself.\nB. Try to grab the machete with your mouth and cut the rope to free yourself.\n\nAnswer: ")
        MacheteInput1 = input()
        if MacheteInput1 in AnswerA:
          slowprint("You hear the deep voices coming closer. You see two armed men enter the room. One runs towards you.\nYOU WENT UNCONCIOUS BY A TASER GUN\n\n")
          input("[PRESS ENTER TO RESPAWN]")
          os.system('cls' if os.name == 'nt' else "printf '\033c'")
          IntroQuestion()
        elif MacheteInput1 in AnswerB:
          inventory.append("Machete")
          slowprint("You acquire the machete and place it in your right hand. You use it to cut the rope. You're now able to move about freely.")
          input("[PRESS ENTER TO CONTINUE]")
          os.system('cls' if os.name == 'nt' else "printf '\033c'")
          MacheteInput2 = slowprint("Where will you go now?\nA. To the handgun.\nB. To the tools\nC. To the door\n\nAnswer: ")
          MacheteInput2 = input()
        else:
          slowprint("Please choose A or B only.")
          time.sleep(1)
          Machete()

      def Handgun():
        print("Handgun")
      def Tools():
        print("Tools")

      choose_name()
    start()
  choose_ts()
start_game()