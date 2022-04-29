# Code by mkcodes@2020 for admins operations system
import os,re # This code must be refactored

def graphics_README():
  print("Before I start the docs, I should tell you that in order for AOS_GRAPHICS_ENGINE.py")
  print("to work, you must do ctrl+- once and ctrl shift 0 for it to work. Also maximize the temrinal to go over the editor.")
  print("Docs: Major WIP")
columns = 3 # os.get_terminal_size()[0]
rows = 3 # os.get_terminal_size()[1]

def setBG(char):
  # Char Str
  global myBackground
  myBackground = ((char*(columns))+"\n")*rows

# def __display__():
  # os.system("clear")
  # global myBackground
  # print(myBackground)

# setBG()
# __display__()

def generateMap(xrng, yrng):
  return ((" "*xrng)+"\n")*yrng

map1 = generateMap(150, 20)

def getCharAtXY(x, y, map1):
    map1 = map1.split('\n')
    map1 = [[y for y in x] for x in map1]
    return map1[y][x]

def getSegment(startx,endx,starty,endy,wintermap1):
  wintermap1 = wintermap1.split("\n")
  wintermap1 = [[x for x in y] for y in wintermap1]
  wintersegment = [wintermap1[x] for x in range(starty, endy)]
  try:
    tempsegment = wintersegment
    for x in range(0, len(wintersegment)):
      for y in range(0, len(wintersegment[x])):
        wintersegment[y] = [wintersegment[y][x] for x in range(startx, endx)]
  except Exception as e:
    pass
  wintersegment = ["".join(f) for f in wintersegment]
  wintersegment = "\n".join(wintersegment)
  return wintersegment

def setCharAtXY(x, y, map1, char):
    map1 = map1.split('\n')
    map1 = [[y for y in x] for x in map1]
    map1[y][x] = char
    map1 = ["".join(v) for v in map1]
    map1 = "\n".join(map1)
    return map1

def writeAtXy(map1, x, y, txt):
  for i in range(0, len(txt)):
      map1 = setCharAtXY(x+i, y, map1, txt[i])
  return map1
#TODO: add slope line for graphics engine
def horizontal_line(map1, x1, x2, y, char):
  # map1
  for i in range(x1, x2):
    map1 =setCharAtXY(i, y, map1, char)
  # [map1 = setCharAtXY(i,y,map1,char) for i in range(x1, x2)]
  return map1

def vertical_line(map1, y1, y2, x, char):
  # map1
  for i in range(y1, y2):
    map1 = setCharAtXY(x, i, map1, char)
  # [map1 = setCharAtXY(x,i,map1,char) for i in range(y1, y2)]
  return map1

# x <> y ^v
def square(map1, x1, y1, x2, y2, joiner="+", vertical="=", horizontal="|"):
    oldh=horizontal
    oldv=vertical
    vertical=oldh
    horizontal=oldv # we need swap them
    map1 = vertical_line(map1, y1, y2, x1, vertical)
    map1 = vertical_line(map1, y1, y2, x2, vertical)
    map1 = horizontal_line(map1, x1, x2, y1, horizontal)
    map1 = horizontal_line(map1, x1, x2, y2, horizontal)
    map1 = setCharAtXY(x1, y1, map1, joiner) # joint-1: topleft
    map1 = setCharAtXY(x1, y2, map1, joiner) # joint-2: topright
    map1 = setCharAtXY(x2, y1, map1, joiner) # joint-1: bottomleft
    map1 = setCharAtXY(x2, y2, map1, joiner) # joint-2: bottomright
    return map1

def __allocate__(map1):
  global default
  default = map1

def __display__(map1):
  global default
  __allocate__(map1)
  outputFlusher = os.system('clear')
  default = default.replace("\n\n","\n"), # end="\b"
  for x in default:
    if x.replace(" ", "") != "":
      # print(re.escape(x))
      print(x)
      # print(len(x))

# screen1
# map1 = square(map1, 0, 0, 50, 10, joiner="+", vertical="=", horizontal="|")
# map1 = writeAtXy(map1, 1, 1, "welcome to wbltz")
# map1 = writeAtXy(map1, 1, 2, "graphics engine by @mkcodes for admins operations system")
# map1 = horizontal_line(map1, 1, 50, 3, "_")
# map1 = writeAtXy(map1, 1, 4, "[press ENTER to contiue]")
# # __allocate__(map1)
# __display__(map1)
# input('') # screen-2
# map2 = square(map1, 0, 0, 50, 10, joiner="+", vertical="=", horizontal="|")
# map2 = writeAtXy(map2, 1, 1, "you pressed enter  ")
# map2 = writeAtXy(map2, 1, 2, "very sus                           ")
# map2 = horizontal_line(map2, 1, 50, 3, "_")
# map2 = writeAtXy(map2, 1, 4, "[insert screen here]    ")
# # __allocate__(map2)
# __display__(map2)

# # DO NOT REMOVE THIS!
# # This will fix glitch of empty lines.
# os.system("tput cuu 999            # move cursor up 999")