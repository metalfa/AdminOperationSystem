#Version 0.1

import os
import time
try:
    import colorama
except Exception as e:
    os.system("pip install colorama")
    import colorama  # Try installing then importing if error
import sys
import re
# import graphics_engine as graphix
#^^^Does this mean aos.graphix.AmongUS calls function AmongUS from graphics_engine.py?


class Data:
    def save(file, data, new=None):
        if new == None:
            trueFile = open(file, "a+")
            trueFile.write(data)
            trueFile.close()
        else:
            trueFile = open(file, "w+")
            trueFile.write(data)
            trueFile.close()

    '''
  def load(file, data):
    trueFile = open(file)
    trueFile.readline(100)
    trueFile.close()
  '''

    def load(file):
        try:
            trueFile = open(file, "r")
            lines = trueFile.readlines()
            for x in lines:
                print(x.strip())
            trueFile.close()
        except FileNotFoundError:
            raise FileNotFoundError("AOS does not detect that file")

    def dirMake(name):
        os.mkdir(name)


class Console:
    def type(words, secs=None):
        if type(secs) == str:
            try:
                secs = float(secs)
                raise ValueError(
                    "[WARN] AOS requested int or float for Console.type. Autoconverted str."
                )
            except Exception as e:
                raise ValueError(
                    "AOS requested int or float or float as a string for Console.type. An invalid "
                    + str(type(1)).replace("<class '", "").replace("'>", "") +
                    " was passed: " + str(secs))
        if secs == None:
            wait = 0.1
        else:
            wait = secs
        punctuation = ['.', ',', '!', ';', ':']
        for char in words:
            if char in punctuation:
                time.sleep(wait)
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.25)
            else:

                time.sleep(wait)
                sys.stdout.write(char)
                sys.stdout.flush()

    def clear(isServer=True):
        os.system("clear")

    def commandPrompt(key, function, ask, invalidFunc=None):
        main = input(ask)
        if main == key:
            try:
                function()
            except:
                raise NameError("No such function as " + function)
        else:
            if invalidFunc == None:
                pass
            else:
                invalidFunc()

    def commentary(text):
        print(colorama.Style.DIM + text + colorama.Style.NORMAL)

    def warn(text):
        print(colorama.Fore.RED + text + colorama.Fore.RESET)


# class Graphix:
class Misc:
    def newline(width=None, char="_"):
        if width == None:
            print(char * (os.get_terminal_size()[0]))
        else:
            print(char * round(int(width)))

    def wait(interval):
        time.sleep(interval)

    def help():
        type(
            "Admin Operations System is a library created 10-21-2021 and was updated 11-26-2021. AOS exists to help make Python better, easier to use, and to help with the world!\n\n\n"
        )
        print("""
    USAGE:
    import admin_operations_system as aos
    console = aos.Console
    misc = aos.Misc
    commentary = console.Commentary
    commentary(\"This is a comment in text?!\")
        """)

    def graphics_README():
        print(
            "Before I start the docs, I should tell you that in order for AOS_GRAPHICS_ENGINE.py"
        )
        print(
            "to work, you must do ctrl+- once and ctrl shift 0 for it to work. Also maximize the temrinal to go over the editor."
        )
        print("Docs: Major WIP")

    def contributors():
        print(''' 
    Contributors:
     - Ultrox
     He/she came up with AOS and started it
     - mkcodes
     He made the graphics engine, calculator engine, and Misc.newline(). 
     - DeadWither
     He/she made the System and Storage classes and typed 
     the markdown. Also updated some functions.
     - MarcosMacMacdonald and IanTang2
     Helped with the code
    ''')

    def version():
        print("V0.1")


class System:
    def stop(reason):
        exit(reason)

    def setProjPoint(files):
        if os.path.isfile(files) == True:
            pass
        else:
            raise FileNotFoundError(
                f"File {files} is not found by Pythus in this repl's directory, make sure you put the directory name with a '/' as  well if it belongs in directories"
            )
        file = open(".replit", "a+")
        file.write(f"entrypoint = '{files}'")
        file.close()


class Storage():
    def __init__(self, value):
        self.value = value

    def getVal(self):
        return self.value

    def changeVal(self, val):
        self.value = val


class aosgraphix:
    def importGraphics():
        try:
            import graphics_engine as aos_graphics
        except Exception as e:
            #^pyflakes
            print(
                "Copy over the graphics_engine.py file to your project, then retry this command."
            )


# class Math:
#   abs = abs()
#   def sq(x):
#     return x*x
#   def sqrt(x):
#     (x*x)/x
