l1 = ["yes", "no"]

def yesl1():
  global yes_in_l1
  if "yes" in l1:
    yes_in_l1 = True
  if "no" in l1:
    yes_in_l1 = False

yesl1()

if yes_in_l1:
  print("yes_in_l1")

if not yes_in_l1:
  print("no yes_in_l1")