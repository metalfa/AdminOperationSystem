# [ finding my awesome bash script ]
import os, subprocess
import os
color = 'blue'
os.system('setterm -term linux -back $'+color+' -fore white -clear')
# Admin panel
# idk how it would look like
print("AOS: Admin panel")
print("_"*(os.get_terminal_size()[0]))
# i am trying to replace "/home/runner" with ~
# basicaally replace root dir w/ ~
while True:
  xv = input("adminpanel:"+os.getcwd()+">")