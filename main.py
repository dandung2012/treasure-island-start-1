print('''
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                                                 
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

name = input("let us begin with your name\n") #input name
destiny = name.count('a')

if destiny % 2 == 0:
  print("great name, your name is your destiny and it will take you inside") #% 0
  path = input("this is game of your life, choose one path, left/right \n") 
  if path == 'right':
    print("welcome wise man, your next step will be more dangerous") #opsikiri
    palace = input("this is our holy palace, would you wait for our king \n") #yes/no"
    if palace == 'yes':
      print("thanks peasant, you can wait here") #opsiyes
      gift = input("by the way prepare your gift to our king \n")
      if gift == 'pisang':
        print("ahhaha.. this is the most wonderfull yellow.. so this is our gold and diamond for you, take it as you want") #pisang
      elif gift == 'baterai':
        print("what is this?, you make fool of our king!? DIE YOU") #baterai
      elif gift == 'korek':
        print("ohh.. dont show me this, the light, the fire, i hate this, aaaAARRggghh") #korek api
    else:
      print("as you wish, so u will be servant of this palace forever with me.. HAahahahaHAHA!!! ") #opsi no
  else:
    print("you will burn to ashes because you are greedy") #opsikanan
else:
  print("you shall not pass, you will succed at other place. take your fried here and say their name") #% 1