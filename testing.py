this = True

print(this)

def that():
  global this
  this = False

  print(this)

print(this)

that()