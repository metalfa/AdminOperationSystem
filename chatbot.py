#IMPORTS

from random import randint
import os
import time

#VARIABLES
isWindows = True

defaultMessage = """
Merci de saisir votre choix :
['1']: Ajouter les produits ainsi que les quantités dans le stock
['2']: Modifier les produits ainsi que les quantités dans le stock
['3']: Consulter la liste des produits
['4']: Quitter

"""










defaultResponses = ["Yes", "No", 'Ja Ja', "Hmm", "Ugh", "*Hangs Up*"]
defaultPunctuation = ['.', '?', '!', '...']
callGreeting = ["Hello", "Who is there", "Hands up, you sussy impasta", "Hewo UWU"]

#FUNCTIONS
def randomize(array):
  return array[randint(0, len(array)-1)]
def createQuestion():
  response = int(input(defaultMessage))
  return response
def clear():
  os.system("clear")
def wait(interval=0.001):
  time.sleep(interval)
def call():
  while True:
    
    a = randomize(defaultResponses)
    print(f"Botty: \"{a + randomize(defaultPunctuation)}\"")
   
    if a == "*Hangs Up*":
      break
    else:
      input("You: ")
def main():
  while True:
    clear()
    question = createQuestion()
  
    if question == 1:
      clear()
      input(f"Botty: \"{randomize(callGreeting) + randomize(defaultPunctuation)}\"\n You: ")
      call()
      wait(2.5)
      
    elif question == 2:
      clear()
      dog = input("You: ")
      print(f"Botty: \"{dog}\"")
      wait(2.5)
    elif question == 3:
      print("You're mean.")


#main()
  