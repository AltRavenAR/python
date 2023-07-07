import time
import random
from readchar import readchar
from alive_progress import alive_bar




'''-----------------------------------------------'''
#Making playable characters
class Character:
  race = 'Human' #Characters race will always be human (for now)
  state = True #Characters are alive until..they aren't
  def __init__ (self, name, age, stat):
    self.name=name
    self.age=age
    self.stat=stat
    
    # is this character/ being dead or alive?
    state = True or False
    #if they are dead then exit program
    if state == False:
      exit()
    else:
      pass

'''-------------------------------------------------'''
class Stats():
  def __init__(self,Str, Aim, Int, Mana, Will):
      self.Str=Str
      self.Aim=Aim
      self.Int=Int
      self.Mana=Mana
      self.Will=Will
      #self.state=state

'''-------------------------------------------------'''
  #making the user
class User(Character):
  pass
'''-------------------------------------------------'''
  #pre-made dialogue goes here
def Age(Character):
  return f"{Character.name} is {Character.age} years old"
def EtienneSpeak(Character, sound):
  return f"{Character.name} says {EtienneRandomDialogue}"
def LeonelSpeak(Character, sound):
  return f"{Character.name} says {LeonelRandomDialogue}"
def WhatStats(Character):
  return f"{Character.name}'s stats are {Character.Str},{Character.Aim},{Character.Int},{Character.Mana},{Character.Will}."

   #dialogue list and random speaking setup
EtienneDialogueList = ['"Dear, Leonel, have you ever wondered if we are inside a video game?"','"Leonel? Are you there?"']
LeonelDialogueList = ['-stares at you-']

EtienneRandomDialogue=random.choice(EtienneDialogueList)
LeonelRandomDialogue=random.choice(LeonelDialogueList)

#------------------stats setup------'''
Etienne = Character('Etienne',21, None)
Etienne = Stats(7,1,9,8,9) #Str, Aim, Int, Mana, Will

Leonel = Character('Leonel',21, None)
Etienne = Stats(2,6,6,9,7) #Str, Aim, Int, Mana, Will

#What do we do if we want to call a specific stat?
'''-------------------------------------------------'''

#start screen 😀

print("")		 
print("Version: Alpha\nUpdate: Leonia frame rework")
time.sleep(1)
print("Update: Playable characters are Etienne and Leonel")



print("------------------")
def loading():
  time.sleep(1)
  with alive_bar(300, bar='smooth', spinner='dots_waves', title='Loading...') as bar:
      for i in range(300):
          time.sleep(.005)
          bar()
  
  time.sleep(1)
loading()
print("------------------")

#building again from scratch
print("Press any key to start")
StartKeyPressed = readchar()
print()
print('type "skip" or "continue"')
user = input("Would you like to see the story or skip to the gameplay?:  ")


if user == "continue":
  #story telling skills 0.0
  print("There is a city that is always cloudy. In this city, not too long ago, something called 'dungeons' started to appear.\n Multiple agencies emerged to fight the supernatural beings that came from these dungeons.\n The most promenient one would be the 'official guild of Leonia'")
  print()
  print("are you with me? (press any key to continue)")
  StartKeyPressed = readchar()
  print("Then, another company appeared, well I wouldn't call it a company, but more of a establishment?\n Anyways, this establishment made most of the modern technology we use today in Leonia.")
  print()
  print("However, the establishment (It is known as i-engineering)\n got too 'powerful' so the guilds and citizens were scared of their power, they needed to do something about it.\n And soon the government of Leonia was involved.")
  print()
  print("Besides the politics, most people go in dungeons to get stronger or richer, just like we will right now!.")
  print()
  print("It is time to start the game! \nI'm going to be your guide! It's time to choose your character.")
  print()
  print()
  #choosing character
  print("The available characters are Etienne or Leonel")
  print()
  time.sleep(1)
  print("Etienne:\n Job: Actor\n Strengths: Persuasion\n Age: 21\n Personality: Kind\n Hair color: Dark brown\n Eye color: Brown\n Height: Tall\n")
  print("Leonel:\n Job: Homemaker and Painter\n Strengths: Art\n Age: 21\n Personality: Calm\n Hair color: Blue\n Eye color: Blue\n Height: Medium\n")
  
else:
  print("skipping is not available at the moment")
  

