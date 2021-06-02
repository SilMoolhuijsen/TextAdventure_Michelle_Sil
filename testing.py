import time

class keyboardDisable():

  def start(self):
    self.on = True

  def stop(self):
    self.on = False

  def __call__(self):
    while self.on:
      msvcrt.getch()


  def __init__(self):
    self.on = False
    import msvcrt

keyboardDisable.start()
time.sleep(10)
keyboardDisable.stop()