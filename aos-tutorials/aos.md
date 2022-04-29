# AOS (Admin Operations System)

> Made by Delight Studio's PyPro. Give credit when using, or we will sue. Ultrox, mkcodes, IanTang2, DeadWither, MacrosMacDonald, give credit when using:


- [AOS (Admin Operations System)](#aos--admin-operations-system-)
  * [What is AOS](#what-is-aos)
    + [Setting Up:](#setting-up-)
      - [Using the direct classes from AOS](#using-the-direct-classes-from-aos-)
      - [Defining Classes with the AOS classes](#defining-classes-with-the-aos-classes)
      - [Setting up graphics (optional)](#setting-up-graphics--optional-)
  + [Classes](#classes)
      - [Data](#data)
      - [Console](#console)
      - [Misc](#misc)
      - [System](#system)
      - [Storage](#storage)
      - [Graphics engine](#graphics-engine)
  * [A Program with AOS](#a-program-with-aos)
  * [Other Sources](#srcaos)



Typed by DeadWither and mkcodes:


## What is AOS

AOS is a module/library made for easy coding in Python. It  has some simple but useful commands.  Here are some reasons why you should use  AOS:

- Easy to use! Even beginners can ace this library

- Simple commands that are essential for good Python programs

- Free to use! However just type this in your description

"Credits: ... and @Ultrox, @mkcodes and @DeadWither for AOS, check AOS here: https://replit.com/@Ultrox/Admin-Operations-System-V009?
"

That's it! Let's get to coding!

### Setting Up:

AOS is easy to set up, since AOS is a replit library, you need to copy admin_operations_system.py and copy to your
repl.
Now there are 2 ways of setting AOS up:

>https://aos-installer.deadwither.repl.co/ was made so now you can install AOS.py and the graphics so you can upload them to replit whenever you want. Not copy it and paste it
#### Using the direct classes from AOS:
```py
import admin_operations_system as AOS
AOS.class.function("parameter") #This is a fake command
```

or:

#### Defining Classes with the AOS classes
```py
import admin_operations_system as AOS
class = AOS.class
class.function("parameter")
```



#### Setting up graphics (optional)
After you've copied the Python file "graphics_engine.py" to your project, there are 2 ways to use graphics.
```py
# Method 1
import graphics_engine as aos_graphics
# Method 2 (unstable)
import admin_operations_system as aos
aos.graphix.importGraphics()
```
> DeadWither's Note:  Method 1 works! ~~Method 2 works as well~~

Reason:
Method 2 imports the graphics to the AOS source. AOS has
no in-built function to process mkcodes's graphics.

---

> Watch the Video Tutorial made by DeadWither for help!


(BetterTutorial.webm)
---

Obviously the second way is better, you need to type
```py
AOS.class.function("parameter") 
```

for the first way, but the second way is easier,
```py
class.function("parameter")
```

What this does is, it makes a class with the same code as the AOS classes.

---

### Classes
These are the classes:
- Data
- Console
- Misc
- System
- Storage
- Graphics

---
#### Data
Note: we are using the second way to call functions

- Save
```py
Data.save(file, data,new=None)
```

This saves some text into a file, if file is not found, 
it will make a new one

The 'file' parameter must be a str or variable with a file 
prefix. It is the file where the data will be stored

The 'data' parameter can be any data type. It is what we 
print into the file

The 'new' parameter can be any type and anything, it can 
be ignored but writing something in it will make sure it
erases any data before storing data

Credits: Made by Ultrox, updated by DeadWither

---

- Load
```py
Data.load(file)
```
The 'file' parameter must be a str or variable with a file 
prefix. It is the file where the data will be printed out

Credits: Made by Ultrox, updated by DeadWither

---

- DirMake
```py
Data.dirMake(name)
```
The 'name' parameter must be a str or variable. It 
is the name of a new folder/directory that will be created

Credits: Made by DeadWither

---
---

#### Console

- Type
```py
Console.type(words,secs=None)
```
This prints 'words' letter by letter. The 'secs' parameter
is optional, by default, it is 0.1 seconds but can be 
changed to any int or float. Giving str will raise error

Credits: Made by Ultrox

- Clear
```py
Console.clear
```
This function clears the console. No need for brackets.

Credits: Made by Ultrox


- Command Prompt
```py
Console.commandPrompt(key,function,ask,invalidFunc=None)
```
This function asks 'ask' then if the user input is 'key' 
it will call 'function', if not, it calls 'invalidFunc'
this is optional.

Credits: Made by Ultrox, updated by DeadWither

- Commentary
```py
Console.commentary("text")
```
Prints 'text' in a light black dim style

Credits: Made by Ultrox

- Warn
```py
Console.warn(text)
```
Prints 'text' in a red colour as a Warning.

Credits: Made by Ultrox

---
---

#### Misc

- Wait
```py
Misc.wait(interval)
```
Pauses for 'interval' secs

Credits: Made by Ultrox

- Help
```py
Misc.help()
```
Prints AOS setting up details

Credits: Made by Ultrox

- Contributors
```py
Misc.contributors()
```
Prints AOS contributors

Credits: Made by DeadWither

- Graphics Note
```py
Misc.graphics_README()
```
Prints AOSGraphix details

Credits: Made by mkcodes

- Version
```py
Misc.version()
```
Prints AOS version

- Newline
```py
Misc.newline(width=None, char="_")
```
Prints a newline. Set width=.. and char=.. to set character and width of newline.

<br>
Helps to see if ther is new versions published on <br>
https://AOS-Installer.deadwither.repl.co

Credits: Made by DeadWither

---
---

#### System

- Stop
```py
System.stop(reason)
```
Exits the program for 'reason', this will be printed 
when the program stops

Credits: Made by DeadWither 

- Set Run File
```py
System.setProjPoint(files)
```
Changes so that when you run project again, it runs `files` not `main.py`

Credits: Made by DeadWither

---
---


#### Storage

Storage is a class to store key value data. It does not work like 
the other functions.

- Making a Key with Value
```py
<keyName> = Storage(<keyValue>)
Example:

data = Storage("data002")
```
Now me made a key named `data` with the value of `data002`

- Getting the value
```py
value = data.getVal()
print(value)
#This will output "data002"
```

- Changing the value
```py
data.changeVal("data003")
value = data.getVal()
print(value)
#This will output "data003"
```
Now me changed the value of the key named `data`
from the value of `data002` to `data003`


Made by DeadWither (Whole Class)

---
---

#### Graphics engine

Let's discuss all the commands available in graphics_engine.py.

First of all, (available in `graphics_engine.graphics_README`), you should
do ctrl+- and set your terminal to fullscreen. This should solve some terminal glitches
across most platforms. (Assuming your terminal is in a window - Fullscreen not tested.)

Now, let's get started. (I've discussed importing the graphics engine at the very top of this manual).

First of all, we have `setBG(char)`. Here is an example of usage:

```py
columns = 3 # os.get_terminal_size()[0]
rows = 3 # os.get_terminal_size()[1]
myMap = setBG(" ")
```

This creates map, myMap, with a background of the character in `setBG(char)` - in this case a space.

There are also generatable blank maps via `generateMap(xrng,yrng)` where `xrng` and `yrng` are how big you want the map to be on the x/y coordinates.

Let's speed through the rest. Note that most things depend on the order you call functions: If you call MAKE A LINE then WRITE TEXT OVER THE LINE it would look like
" TEXT -------" however if you did it reverse it would just be a line - "---------".

- `getCharAtXY(x, y, map1)`: Takes characters at X, Y of MAP1.
- `getSegment(startx,endx,starty,endy,wintermap1)`: Gets a segment from (Startx, Endx) and (Starty, Endy) of Wintermap1.
- `setCharAtXY(x, y, map1, char)`: Sets character (x, y) to char in the map map1. Usage: `map1 = setCharAtXy(3, 4, map1, "x")`
- `writeAtXy(map1, x, y, txt)`: Write text at (x, y).
- `horizontal_line(map1, x1, x2, y, char)`: Make a horizontal line in map1 from x1 to x2 in y axis y. Character set would be char.
- `vertical_line(map1, y1, y2, x, char)`: Make a vertical line in map1 from y1 to y2 in x axis x. Character set would be char.
- `square(map1, x1, y1, x2, y2, joiner="+", vertical="=", horizontal="|")`: Make a square in map1 from (x1, y1) to (x2, y2). The corners are `joiner`, Vertical lines are made via character `vertical`, and same goes for the horizontal lines (horizontal lines are set to variable `horizontal`)
- `__allocate__(map1)`: Allocate map1 as the map to be displayed when `__display__` is called.
- `__display__(map1)`: Display map you just created.

Example:
```py
# screen1
map1 = square(map1, 0, 0, 50, 10, joiner="+", vertical="=", horizontal="|")
map1 = writeAtXy(map1, 1, 1, "welcome to wbltz")
map1 = writeAtXy(map1, 1, 2, "graphics engine by @mkcodes for admins operations system")
map1 = horizontal_line(map1, 1, 50, 3, "_")
map1 = writeAtXy(map1, 1, 4, "[press ENTER to contiue]")
__allocate__(map1)
__display__(map1)
input('') # screen-2
map2 = square(map1, 0, 0, 50, 10, joiner="+", vertical="=", horizontal="|")
map2 = writeAtXy(map2, 1, 1, "you pressed enter  ")
map2 = writeAtXy(map2, 1, 2, "very sus                           ")
map2 = horizontal_line(map2, 1, 50, 3, "_")
map2 = writeAtXy(map2, 1, 4, "[insert screen here]    ")
# __allocate__(map2)
__display__(map2)
# DO NOT REMOVE THIS!
# This will fix glitch of empty lines.
os.system("tput cuu 999            # move cursor up 999")
```
 (TODO: slope) 


Credits: Made by mkcodes( entire class)

---
---
---

Credits: Typed by DeadWither<br>graphics docs added by 
mkcodes

## A Program with AOS
> Coded by DeadWither

```py
#Password Checker with AOS

#Importing
import admin_operations_system as AOS

#Setting Up
system = AOS.System
console = AOS.Console
misc = AOS.Misc
data = AOS.Data

#Program
console.commandPrompt("topsecretpassword",granted(),"Enter the Password: ","firstDenied()")

def granted():
  console.type("Correct Password! Access Granted")
  misc.wait(2)
  system.stop("You did what you had to do.")

def firstDenied():
  console.warn("Invaild Password. Another Invalid will call the FBI")
  console.commandPrompt("topsecretpassword",granted(),"Enter the Password: ","denied()")

def denied():
  console.warn("Calling FBI! Alert! Alert! Intruder in the system")
  system.stop("You are arrested")
```

## Output:
> The bold text is printed. The normal text is user text:
> The warning is italic

**Enter the Password:** topsecret <br>
*Invalid Password. Another Invalid will call the FBI* <br>
**Enter the Password:** topsecretpassword <br>
**Correct Password! Access Granted** <br>
**You did what you had to do** <br>
**repl process died unexpectedly: exit status 1** <br>

---
---
---

## Other Sources:
AOS additional/helpful sources:

https://aos-installer.deadwither.repl.co/
<br/>
https://aos-docs.mkcodes.repl.co/ [ Markdown code is borrowed from DeadWither ]
<br/>
https://aos-docs.mkcodes.repl.co/cdn_AOS1.py
<br/>
https://aos-docs.mkcodes.repl.co/cdn_AOS1GRAPHICS.py

---
---

I hoped you enjoyed this markdown tutorial. Get started now!
<br>

Typed by DeadWither (Graphics typed by mkcodes):
<br>https://replit.com/@DeadWither

Contributors:
- DeadWither
https://replit.com/@DeadWither
- mkcodes
https://replit.com/@mkcodes
- Ultrox (Owner)
https://replit.com/@Ultrox
- MarcosMacDonald 
https://replit.com/@MarcosMacDonald 
- IanTang2 
https://replit.com/@IanTang2 

---

---
---
