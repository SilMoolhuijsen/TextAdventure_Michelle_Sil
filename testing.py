import os

def a():
  os.system('cls' if os.name == 'nt' else "printf '\033c'")

  print()