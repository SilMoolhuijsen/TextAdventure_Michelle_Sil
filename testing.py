import time

class keyboardDisable():
    def __init__(self):
        self.on = False
        global msvcrt
        import msvcrt
        
    def start(self):
        self.on = True

    def stop(self):
        self.on = False

    def __call__(self): 
        while self.on:
            msvcrt.getwch()

disable = keyboardDisable()
disable.start()
time.sleep(10)
disable.stop()