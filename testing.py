global yes
yes = False

def wow():
  global yes
  yes = False

  def wow2():
    global yes
    yes = True
  
  wow2()
wow()

print(yes)