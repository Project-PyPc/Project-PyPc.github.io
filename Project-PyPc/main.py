import os

user = input ("login:")
if user == "root":
  password1 = input ("Password = ")
elif user == "Vacuum":
    password2 = input ("Password = ")
elif user == "Veer":
  password3 = input ("Password = ")
elif user == "nolancraft":
  passwordn = input ("Password = ")
else:
  exit()

if password1 == "Ir0n_m@n42":
  os.system('python pypc-main.py')
elif password2 == "Meow2349":
  os.system('python pypc-main.py')
elif password3 == "YousaInSeventhNow":
  os.system('python pypc-main.py')
elif passwordn == "5654":
  os.system('python pypc-main.py')
else:
  exit()