import os

command = input ("command:")
  
if command == "help":
  os.system('python pypc-help.py')

if command == "firefox":
  os.system('python pypc-firefox.py')

if command == "logout":
  os.system('python main.py')

if command == "echo":
  os.system('python pypc-echo.py')

if command == "cinfo":
  os.system('python pypc-cinfo.py')
  
if command == "pwdn":
  os.system('python pypc-pwdn.py')

if command == "txtedit":
  os.system('python pypc-txtedit.py')

if command == "appmenu":
  os.system('python pypc-appmenu.py')