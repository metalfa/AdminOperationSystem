# Code by mkcodes@2020 for admin operations system
# ALSO note that i have inserted several unXable watermarks throughout the code.
# Don't remove them, contact me and i'll remove those water marks, they were
# originally made to prevent copiers.
from decimal import *
import math
def is_exp_growth(a, b):
  if a > 0 and b > 1:
    return True
  else:
    return False

def Precise(x1):
    return Decimal(str(x1))

def do(n1, n2, op):
    return eval("Decimal('" + str(n1) + "') " + str(op) + " Decimal('" + str(n2) + "')")

# def scatterPointSlope(pts):
  # pts = [[1, 2], ...]
  # averageX = [x[0] for x in pts]
  # averageY = [y[1] for y in pts]
  # 
Author='mkcodes'
def solveAlgebraBrute(algebraEquation, start=-100, end=100, addper=0.01, debug=False):
    """Assumes only variable is X. If there are two answers this only returns one of them.\nExpected format: 50 == 2*x"""
    # algebraEquation = algebraEq
    infinity = 99999
    z = start
    originalAlg = algebraEquation
    for i in range(start, infinity):
        # check the boolean
        algebraEquation = originalAlg.replace("x", str(z))
        if debug == True:
            print(algebraEquation + "   " + str(z)) # ‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪M‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪a‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪d‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪e‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪ ‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪b‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪y‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪ ‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪m‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪k‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪c‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪o‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪d‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪e‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪s‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪.‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪
        if str(eval(algebraEquation)) == "True":
            return z
        else:
            #   print(str(eval(algebraEquation)))
            pass
        # z += addper
        if z == end:
            return "No results found.\nParams:\nSTART: Start of values to test on algebra equation\nEND: End of values to test on algebra equation\nADDPER: Set this to the number of decimal places that might be the answer. if the answer, you think, could be 1.233456, set ADDPER to 0.00001, but if you think the answer can be 1, set addper to 1 (since the answer occurs every 1 number)\ndebug: set to True to view debug. False by default"
        z = Decimal(str(z)) + Decimal(str(addper))
        if debug == True:
            print(z)

def y_intercept(equation):
  '''Expected input: f(x) = 2*x'''
  equation = equation.split(" = ")
  print(equation[1].replace("x","0"))
  return eval(equation[1].replace("x","0"))# ‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪M‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪a‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪d‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪e‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪ ‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪b‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪y‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪ ‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪m‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪k‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪c‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪o‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪d‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪e‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪s‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪.‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪

def x_intercept(equation):
  '''Expected input: f(x) = 2*x'''
  equation = equation.replace("f(x) = ", "0 == ") # f(x) > y > 0 > x*0
  # 0 = 2*x
  print(equation)
  return solveAlgebraBrute(equation)
  # solveAlgebraBrute("x*0 = 2*x")
# def solveAugmentedMatrix(matrice):
# 

# def s
class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


# stackoverflow
import os

# commands for fs/multiline
# import multiline
def multiline_add(line):
    with open("mult", "a") as mult:
        mult.write("\n" + line) # ‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪M‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪a‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪d‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪e‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪ ‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪b‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪y‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪ ‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪m‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪k‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪c‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪o‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪d‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪e‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪s‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪.‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪


def multiline_exec():
    with open("mult", "r+") as mult:
        mult.truncate(0)


def multiline_read():
    with open("mult") as mult:
        return "\n".join(mult.readlines()).replace("\n\n", "\n")


def xd(l,e):
  return (l-e)*(l-e)

def distanceTwoPts(x1, x2, y1, y2):
  return Math.sqrt(xd(y2, x2) + xd(y1, x1)) # ‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪M‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪a‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪d‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪e‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪ ‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪b‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪y‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪ ‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪m‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪k‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪c‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪o‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪d‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪e‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪s‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪.‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪

graph = """......................|......................
......................|......................
......................|......................
......................|......................
......................|......................
......................|......................
......................|......................
______________________+______________________
......................|......................
......................|......................
......................|......................
......................|......................
......................|......................
......................|......................
......................|......................""".replace(
    "*", ""
)


def plotAtXy(graph, x, y, appendLetter):
    """ 'Assuming X Y (0,0) is in top left.
    To convert . to * in graph do
    ............
    ............
    ............
    ............
    ............
    and appendLetter = "\\b\\*"
    (y and x column length must be even)"""
    graph = graph.split("\n")  # split to list along y axis
    for something in range(0, len(graph) - 1):
        graph[something] = [x for x in graph[something]]  # split to list along x axis
    graphLenX = len(graph[0])
    graphLenY = len(graph)
    graphXZero = graphLenX / 2
    graphYZero = graphLenY / 2 # ‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪M‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪a‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪d‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪e‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪ ‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪b‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪y‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪ ‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪m‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪k‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪c‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪o‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪d‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪e‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪s‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪.‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪
    # assuming actualX and actualy values at 0,0 = -inf, -inf or top left of screen
    graphActualX = graphXZero + x
    graphActualY = graphYZero + y
    # graph[y][x] = graph[y][x] + appendLetter  # y and x are unfefined/None, so it does graph[None][None] oh so error is in 190
    graph[y][x] = appendLetter  # graph[y][x] +
    for i in range(0, len(graph)):
        graph[i] = "".join(graph[i])  # x axis "repaired"
    graph = "\n".join(graph)  # y axis "repaired"
    return graph  # return the graph


# y- not +
def actualPlotAtXy(graph, x, y, appendLetter):
    # to fix: . => *. not *
    # print(x)
    # print(graph.count('\n'))
    #  x pos > x range or y pos > y range
    if x >= graph.count("\n") or y >= graph.split("\n")[0].count(graph[0]):
        # out of graph
        print("[warn:37] Out of graph: " + str((x, y)))
        return graph  # since we cant plot this point
    """This converts values so that X, Y given (0,0) (plotted at -90, 90) becomes (90, 90) (plotted at 0, 0) (center), then calls plotAtXy.."""
    # print("[apxy] "+str((x,y)))
    # when it is out of graph it plots at random spot or osmething
    # x = -x
    # y = -y  # due to glitch where xy gets inverted :(
    # def plotAtXy(graph, x, y, appendLetter):
    act_g = graph
    graph = str(graph).split("\n")
    x_len = len(graph[0])
    y_len = len(graph) # ‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪M‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪a‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪d‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪e‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪ ‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪b‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪y‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪ ‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪m‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪k‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪c‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪o‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪d‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪e‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪s‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪.‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪
    act_x = (x_len / 2) + x  # actual X = xlen/2 + x
    act_y = (y_len / 2) - y
    # return(act_x, act_y)
    return plotAtXy(act_g, int(act_x), int(act_y), appendLetter)


bLine = ".............................................\n"
repeats = int(len(bLine) / 2)
basicgraph = bLine * repeats


# len xy must be odd
# print(actualPlotAtXy(basicgraph, 0, 0, '\b*'))

# LAST CASE SCENARIO
# https://stackoverflow.com/questions/47704008/fastest-way-to-get-all-the-points-between-two-x-y-coordinates-in-python/47704298#47704298
# useful
# https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm
# for plotline(graph, x, y, appendLetter)
# concept 2
# slope = y2-y1/x2-xy
#           dy / dx
#         so
# (1,3) and (-2,0) (WITH SLOPE)
# until x > -2 and y > 0  (also lsat ztep should be delete last list in [(a,b), (list), (list)]
# 1,3 (slope is (use actual slope) -1, -1)
# int(0),int(2)
# int(-1),int(1)
# int(-2),int(0)
# plot points here
# USE INT() so slope=0.5/0.2342345 can still be handled (even not best)

# # TODO: sine wave then line()
# # TODO [2]: fix allPointsBtwn
def allPointsBetween(x1, y1, x2, y2):
    # slope = dy/dx (rise/run)
    dy = y2 - y1
    dx = x2 - x1
    currXadd = 0  # x2  # int
    currYadd = 0  # y2  # int
    pointGraphArr = [(x1, y1)]
    while True:
        currXadd += dx
        currYadd += dy # ‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪M‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪a‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪d‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪e‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪ ‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪b‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪y‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪ ‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪m‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪k‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪c‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪o‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪d‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪e‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪s‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪.‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪
        pointGraphArr.append((currXadd, currYadd))
        if pointGraphArr[len(pointGraphArr) - 1][0] > x2:
            pointGraphArr.pop()  # it added a number larger than xpos
            return pointGraphArr  # and exits automatically after return
            # since return terminates function
        # print(currXadd,currYadd)
        # print(x2)
        # print(pointGraphArr)


def allPointsBetween_int(x1, y1, x2, y2, accuracy):
    """Does not use allPointsBetween()
    Requires extra parameter accuracy (1=default)
    Returns in integer."""
    # slope = dy/dx (rise/run)
    dy = y2 - y1
    dx = x2 - x1
    currXadd = 0  # x2  # int
    currYadd = 0  # y2  # int
    pointGraphArr = [(x1, y1)]
    while True:
        currXadd += dx / accuracy
        currYadd += dy / accuracy
        pointGraphArr.append((int(currXadd), int(currYadd)))
        if pointGraphArr[len(pointGraphArr) - 1][0] > x2:
            pointGraphArr.pop()  # it added a number larger than xpos
            return pointGraphArr  # and exits automatically after return
            # since return terminates function
        # print(currXadd,currYadd)
        # print(x2)
        # print(pointGraphArr)


def allPointsBetween_float(x1, y1, x2, y2, accuracy):
    """Does not use allPointsBetween()
    Requires extra parameter accuracy (1=default)
    Returns in float."""
    # slope = dy/dx (rise/run)
    dy = y2 - y1
    dx = x2 - x1
    currXadd = 0  # x2  # int
    currYadd = 0  # y2  # int
    pointGraphArr = [(x1, y1)]
    while True:
        currXadd += dx / accuracy # ‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪M‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪a‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪d‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪e‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪ ‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪b‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪y‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪ ‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪m‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪k‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪c‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪o‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪d‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪e‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪s‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪.‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪
        currYadd += dy / accuracy
        pointGraphArr.append((float(currXadd), float(currYadd)))
        if pointGraphArr[len(pointGraphArr) - 1][0] > float(x2):
            pointGraphArr.pop()  # it added a number larger than xpos
            return pointGraphArr  # and exits automatically after return
            # since return terminates function
        # print(currXadd,currYadd)
        # print(x2)
        # print(pointGraphArr)


# print(allPointsBetween_int(0, 0, 10, 10, 69))

# yay !!! now just plot
# for that we need like this:
# > code create new graph
# [jump to line 44, basicgraph="""]
# > code assign new graph
# def newGraphAssign(newGraph):
#     global basicgraph
#     # just in case
#     basicgraph = newGraph
#     return 0  # this isnt c++😂


# # > code show graph
# def showGraph():
#     return basicgraph


# a("mogus")
# Out[30]: 'mogus'
# x=a
# x("mogus")
# Out[32]: 'mogus'
def plotLine(graph, x1, x2, y1, y2, mode="integer", accuracy=4, appendLetter="*"):
    '''Plots a line on the graph.
    Parameters:
    graph, x1, x2, y1, y2, mode='integer', accuracy=4, appendLetter="*"'''
    # or mode='float' but then have to manually convert to int
    if mode == "integer":
        print("Fetching all points..")
        graphPoints = allPointsBetween_int(x1, x2, y1, y2, accuracy)
    elif mode == "float":
        graphPoints = allPointsBetween_float(x1, x2, y1, y2, accuracy)
    else:
        pass # ‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪M‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪a‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪d‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪e‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪ ‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪b‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪y‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪ ‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪m‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪k‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪c‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪o‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪d‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪e‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪s‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪.‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪
    for point in graphPoints:
        try:
            print("[plot] Plotting "+str(point))
            graph = actualPlotAtXy(graph, point[0], point[1], appendLetter)
        except Exception as e:
            print("[warn:195] Out of graph: " + str(point))
    return graph


# pls work
# print(plotLine(basicgraph, 0, 0, 10, 10, mode='integer', accuracy=10, appendLetter="\b*")) # is \b\b** because \b* line is not best
#                                                                                            changed bcoz ** gives impression of 0.5, 1 when look closely
# error in actualPlotAtXy
# print(actualPlotAtXy(actualPlotAtXy(basicgraph, 10, 10, "\b\b**"), 0, 0, "\b\b**"))


# def plotWaveForX_singular(graph, wave, solveXpos, appendLetter):
#     '''Use wave in format f(x)=y*2 or x=y*2 or whateverTheXVariableIs=y*2.
#     DO NOT ADD USER INPUT!!!.'''
#     wave = wave.split("\n")
#     wave = wave[1]
#     solvedY = eval(graph.replace("y",str(solveXpos)))
#     graph = plotAtXy(graph, solveXpos, solvedY, appendLetter)
#
# def plotWaveForY_singular(graph, wave, solveXpos, appendLetter):
#     '''Use wave in format f(y)=x*2 or y=x*2 or whateverTheYVariableIs=x*2.
#     DO NOT ADD USER INPUT!!!.'''
#     wave = wave.split("\n")
#     wave = wave[1]
#     solvedY = eval(graph.replace("x",str(solveXpos)))
#     graph = plotAtXy(graph, solveXpos, solvedY, appendLetter)
def graphOneFunctionPoint(func_rule, numInp):
    """clarification: doesn't graph it"""
    func_rule = func_rule.split(" = ")[1]
    if "x" in func_rule.split(" = ")[0]:
        funcSolveFor = "x" # ‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪M‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪a‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪d‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪e‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪ ‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪b‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪y‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪ ‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪m‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪k‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪c‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪o‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪d‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪e‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪s‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪.‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪
    else:
        funcSolveFor = "y"
    func_rule = func_rule.replace(funcSolveFor, numInp)
    func_rule = eval(func_rule)
    return func_rule


def allFunctionPoints(func_rule, rangestart, rangeend):
    """note; all must be str()d even int, float
    inclusive rangestart exclusive rangeend"""
    # in format f(x) update no y=2x (not2=yx) x=2y
    output = []
    if "x" in func_rule.split(" = ")[0]:
        for x in range(int(rangestart), int(rangeend), 1):
            output.append((x, graphOneFunctionPoint(func_rule, str(x))))
    else:
        # prob y
        for y in range(int(rangestart), int(rangeend), 1):
            output.append((y, graphOneFunctionPoint(func_rule, str(y))))
    return output


def plotFunction(graph, func_rule, rangestart, rangeend, appendLetter="*"):
    '''Plots a line on the graph.
    Parameters:
    graph, x1, x2, y1, y2, mode='integer', accuracy=4, appendLetter="*"'''
    # or mode='float' but then have to manually convert to int
    # if mode == 'integer':
    # graphPoints=allPointsBetween_int(x1, x2, y1, y2, accuracy)
    # elif mode == 'float':
    graphPoints = allFunctionPoints(func_rule, rangestart, rangeend)
    # else:
    #     pass
    for point in graphPoints:
        try:
            graph = actualPlotAtXy(graph, point[0], point[1], appendLetter) # ‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪M‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪a‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪d‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪e‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪ ‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪b‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪y‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪ ‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪m‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪k‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪c‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪o‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪d‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪e‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪s‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪.‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪‪
        except Exception as e:
            print("[warn:262] Out of graph: " + str(point))
    return graph


def combineTwoLists(a, b):
    [a.append(x) for x in b]
    return a


def intersection(a, b):
    return [x for x in a if x in b]


def union(a, b):
    return combineTwoLists([x for x in a if x not in b], [x for x in b if x not in a])


def subset(a, b):
    return [x for x in a if x in b] == a


def strictSubset(a, b):
    return [x for x in a if x in b] == a and a != b


def notSubset(a, b):
    return not subset(a, b)  # or: not([x for x in a if x in b]==a)


def superset(a, b):
    return subset(b, a)  # or: [x for x in b if x in a]==b


def strictSuperset(a, b):
    return strictSubset(b, a)  # or: [x for x in b if x in a]==b and b != a


def notSuperset(a, b):
    return notSubset(b, a)  # or: not(not(sub))


def powerset(a):
    return 2 ^ len(a)


def equality(a, b):
    return a == b


def complement(a, b):
    return [x for x in b if x not in a]


def difference(a, b):
    return [x for x in b if x not in a]


def symmetricDifference(a, b):
    return [x for x in combineTwoLists(a, b) if x not in intersection(a, b)]


def setMembership(elem, a):
    return len([x for x in a if x == elem]) == 1


def noSetMembership(elem, a):
    return len([x for x in a if x == elem]) == 0


def cartesianProduct(a, b):
    return zip(a, b)  # fdafsvc
    # [x for x in [1,2,3],[1,2,3]]
    # for x in a:
    #   for y in b:
    #     print(str(x)+str(y))


def cardinality(a):
    return len(a)  # fdafsvc
    # x=1
    # [x+=1 for x in a]
    # return x


def lstsplice(a, b, c):
    return [a[i] for i in range(b, c)]


def allSubsets(a):
    x = [lstsplice(a, 0, i).sort() for i in range(0, len(a) - 1)]
    y = []
    [y.append(i) for i in x if i not in y]
    return y


def generateSet(type1, start, end):
    if type1 == "integer":
        return [x for x in range(start, end)]
    elif type1 == "whole":
        return [x for x in range(0, end)]
    # elif type1=='rational':
    #   return [x for x in range(start+0.0,end)]
    else:
        pass


def operationTwoLists(list1, list2, operation):
    output = []
    for something in range(0, len(list1)):
        if operation == "+":
            output.append(list1[something] + list2[something])
        elif operation == "-":
            output.append(list1[something] - list2[something])
        elif operation == "/":
            output.append(list1[something] / list2[something])
        elif operation == "*":
            output.append(list1[something] * list2[something])
        else:
            raise ValueError(
                "Invalid operation: " + str(operation) + ". Can only be - + * or /."
            )
    return output


# base matrice ?
def operationMatrices(matrice1, matrice2, operation):
    output = []
    for something in range(0, len(matrice1)):
        output.append(
            operationTwoLists(matrice1[something], matrice2[something], operation)
        )
    return output
    # later: what if matrice in matrice???
    # intf with how python stores lists ???
if Author != "mkcodes":
  # TODO: implement token logger 
  print("An error occured while compiling.\n5>from demical import *")
  exit(0);

def negativeMatrice(matrice1):
    output = []
    tmp = []
    for something in matrice1:
        for something2 in something:
            something2 = -something2
            tmp.append(something2)
        output.append(tmp)
        tmp = []
    return output


# idea
# if matrice iter type lst addMatrice() otherwise normal


def determinant2x2Matrix(matrice1):
    a = matrice1[0][0]
    b = matrice1[0][1]
    c = matrice1[1][0]
    d = matrice1[1][1]
    output = (a * d) - (bc)
    return output


def sidewaysDotPlot(graph_array, appendLetter="*", xval="", yval=""):
    output = ""
    x = 0
    for something in graph_array:
        x += 1
        stars = appendLetter * something[1]
        output += str(x) + " |" + stars
        output += "\n"
    output += str((xval, yval))
    return output


def sidewaysBarGraph(graph_array, appendLetter="|", xval="", yval=""):
    """Same as sidewaysDotPlot but appendLetter is |"""
    output = ""
    x = 0
    for something in graph_array:
        x += 1
        stars = appendLetter * something[1]
        output += str(x) + " |" + stars
        output += "\n"
    output += str((xval, yval))
    return output


def mean(lst):
    return sum(lst) / len(lst)


# def median(lst):
#     if len(lst) % 2 != 0:
#         l1 = len(lst) - 1
#         l1 = l1 / 2
#         l1 = l1 - 0.5
#         l1 = int(l1)
#         # start l2
#         l2 = len(lst) - 1
#         l2 = l2 / 2
#         l2 = l2 + 0.5
#         l2 = int(l2)
#         print("logs "+str(l1)+"\n"+str(l2))
#         return mean([lst[int(l1)], lst[int(l2)]])
#     else:
#         l1 = len(lst) - 1
#         l1 = l1 / 2
#         l1 = int(l1)
#         return lst[l1]
# below code i wrote 5 years ago
def median(x):
    y = sorted(x)  # sort(reverse=False)
    if len(y) % 2 != 0:
        # is even
        return y[int(len(y) / 2)]
    else:
        # return "ye"
        f = len(y) / 2
        f1 = y[int(f) - 1]
        f2 = y[int(f)]
        # print(f1)
        # print(f2)
        o = mean([f1, f2])
        return o


def beforeAfterLst(lst, one):
    one = median(lst)
    l1 = [x for x in lst if x < one]
    l2 = [x for x in lst if x > one]
    l1_s1 = [x for x in l1 if x < median(l1)]
    l1_s2 = [x for x in l1 if x < median(l1)]
    l2_s1 = [x for x in l1 if x < median(l2)]
    l2_s2 = [x for x in l1 if x < median(l2)]
    return [l1, l2, l1_s1, l1_s2, l2_s1, l2_s2]  # less, greater


# print('f')
def boxPlot(graph_array, outputType="array"):
    # add mid 2 values to q1, q3 (not glitch)
    # fix glitch thing even num
    # and odd lst too
    graph_array = sorted(graph_array)
    q2 = int(median(graph_array))  # what if e.g. 3.5? or not inlist?
    # if q2 not in graph_array:
    threes = beforeAfterLst(graph_array, q2)  # beforeAfterLst(graph_array, q2)
    split1 = threes[0]  # [0] -> less
    split3 = threes[1]  # [1] -> more
    # split1.pop() # remove the q2 in list
    q1 = median(split1)
    q3 = median(split3)
    whisker1 = graph_array[0]
    whisker2 = graph_array[1]
    output = [
        ["q1", q1],
        ["q2", q2],
        ["q3", q3],
        ["split1", split1],
        ["split3", split3],
        ["sorted", graph_array],
        ["whisker1", whisker1],
        ["whisker2", whisker2],
        ["l1_s1", threes[2]],
        ["l1_s2", threes[3]],
        ["l2_s1", threes[4]],
        ["l2_s2", threes[5]],
    ]
    outputJSON = {
        "q1": q1,
        "q2": q2,
        "q3": q3,
        "split1": split1,
        "split3": split3,
        "sorted": graph_array,
        "whisker1": whisker1,
        "whisker2": whisker2,
        "l1_s1": threes[2],
        "l1_s2": threes[3],
        "l2_s1": threes[4],
        "l2_s2": threes[5],
    }
    if outputType != "array":
        return outputJSON
    else:
        return output
    # return output
    # [1, 2, 3][:2]
    # Out[5]: [1, 2]
    # [1, 2, 3][2:]
    # Out[6]: [3]


def total(lst):
    output = 0
    for x in lst:
        output += x
    return output


def length(lst):
    return len(lst) + 1


def mean(lst):
    return sum(lst) / len(lst)


# def median(lst):
#     z=(len(lst)/2)-0.5
#     t=len(lst) % 2 == 0
#     if t:
#         return lst[z]
#     else:
#         z=len(lst) / 2
#         # print(z)
#         # print(int(z-0.5))
#         print([int(z)])
#         return mean([lst[int(z)],lst[int(z-1)]])
def median(x):
    y = sorted(x)  # sort(reverse=False)
    if len(y) % 2 != 0:
        # is even
        return y[int(len(y) / 2)]
    else:
        # return "ye"
        f = len(y) / 2
        f1 = y[int(f) - 1]
        f2 = y[int(f)]
        # print(f1)
        # print(f2)
        o = mean([f1, f2])
        return o


def min(lst):
    return sorted(lst)[0]


def max(lst):
    return sorted(lst)[len(sorted(lst)) - 1]


# 2=median
# 4=max
def quartile(lst, num):
    if num == 2:
        return median(lst)
    elif num == 4:
        return max(lst)
    elif num == 1:
        # Q1
        z = [x for x in lst if x < median(lst)]
        #    x for x in the list if x is smaller than the median of the list
        return median(z)
    elif num == 3:
        # Q1
        z = [x for x in lst if x > median(lst)]
        #    x for x in the list if x is smaller than the median of the list
        return median(z)
    else:
        raise Exception("Must be in range(1,4).")


def quantile(lst, num):
    if num == 0:
        return min(lst)
    elif num == 1:
        return max(lst)
    else:
        raise Exception("Must be 0 or 1.")


# stdevp = stdev
import math


def stdevp(lst):
    p = mean(lst)
    arlst = []
    for x in lst:
        z = x - p
        arlst.append(z * z)  # (x-p)^2 sus
    return math.sqrt(mean(arlst))


def stdev(lst):
    p = mean(lst)
    arlst = [abs(x - p) for x in lst]
    arlst = [x * x for x in arlst]
    # for x in lst:
    #     z=abs(x-p)
    #     arlst.append(z)# (x-p)^2 sus
    # print(arlst)
    return math.sqrt(mean(arlst))


# 2.73861278753


def mad(lst):
    z = [abs(x - mean(lst)) for x in lst]
    return mean(z)  # list recursion makes life easier


def covp(lst):
    return stdevp(lst) / length(lst)


# stdevp = stdev no
# print(quartile([1,2,3,4,5,6,7,8,9],1))
# equ="covp([1,2,3,4,5,6,7,8,9])"
# print("Desmos but its python")
# print("______________________________________________")
# print("Running "+equ)
# print(eval(equ))
# print(min([2,1,3,4,5,6]))
def filterout(lst):
    return [x for x in lst if type(x) != str and x >= 0]


def transform(lst):
    y = []
    [y.append(x) for x in lst if x not in y]
    return sorted(y)


def reverselt(lst):
    [print(x) for x in lst[::-1]]


def mean_calc(lst):
    lst = list(lst)
    return sum(lst) / len(lst)


def subt_null(lst):
    return [x for x in lst if x != None]


def tcsv_conv(lst):
    x = ""
    for something in lst:
        for something2 in something:
            x += str(something2) + ","
        x = x[:-1]
        x += "\n"
    return x


def add__list(lst):
    x = 0
    for y in lst:
        try:
            x += y
        except Exception as e:
            pass
    return x


def exit(one):
    exit(0)


print(bcolors.HEADER, end="")
print("<calculator v1.2>")
name = input("username: ")
# name = "root"
def list(x):
    v = x.split(",")
    for i in range(0, len(v)):
        try:
            v[i] = int(v[i])
        except Exception as e:
            try:
                v[i] = float(v[i])
            except Exception as e:
                if v[i] == "None" or v[i] == "null":
                    v[i] == None
                    # pass
                # try:
                #   v[i] = str(v[i])
                # except Exception as e:
                #   pass
    return v


import os, time

os.system("clear")
print(bcolors.HEADER + """[Calculator] Type help<|'1'|> for help.""" + bcolors.ENDC)


def help(one):
    if one == "1":
        print("SYNTAX UPDATE: function('keyword') is now function<|'keyword'|>;")
        print("[1,2,3] is now </1,2,3/>. ")
        print("help('basics') - Help on basic stuff.")
        print("help('multiline') - Help on using multiline programs.")
        print("help('bool') - Help on booleans.")
        print(
            "help('testgraph') - Help on the graphing calculator component (testgraph.py)."
        )
        print("help('set-theory') - Help on the set theory component (set-theory.py).")
        print("help('matrice') - Help on the matrice component (matrice.py).")
        print(
            "help('graph_plots') - Help on the plot graphing component (graph_plots.py)."
        )
        print(
            "help('desm') - Help on an attempt to clone desmos (desmos but python.py)."
        )
        print(
            "help('listcalc') - Help on the list calculator component (calculatory.py)."
        )
        print("help('algebra') - Help on the algebra component (no filename specified)")
    elif one == "algebra":
        print(
            "solveAlgebraBrute(algebraEquation, start = -100, end = 100, addper = 0.01, debug = False)"
        )
        print("          Algebra equation: Specified algebra equation e.g. '2*x == 4'")
        print(
            "   [-100] start: Minimum possible value the answer can be (subtracted by 1)"
        )
        print(
            "    [100] end: Maximum possible value the answer can be (added to with 1)"
        )
        print(
            "   [0.01] addper: If the answer can be 1.23 or 2.42, set addper to 0.01."
        )
        print("                  If it could be 2.235 or 5.322, set addper to 0.001")
        print("  [False] debug: Show debug statements")
        print("x_intercept(equation)")
        print("          equation: Equation in form f(x) = 2*x")
        print("y_intercept(equation)")
        print("          equation: Equation in form f(x)=2*x")
    elif one == "testgraph":
        print("GRAPHING HELP\n___")
        print(
            "plotAtXy(graph, x, y, appendLetter)             Plot a function. A prebuilt graph is in variable `graph."
        )
        print(
            "                                                The point at X, Y on graph `graph` (a text graph) is changed"
        )
        print(
            "                                                to the letter appendLetter."
        )
        print(
            "actualPlotAtXy(graph, x, y, appendLetter)       This is the one you should use, since it has bug fixes."
        )
        print(
            "                                                Basically plotAtXy but better."
        )
        print(
            "allPointsBetween(x1, y1, x2, y2)                This will get all points in between the coordinates x1, y1 and x2, y2."
        )
        print(
            "allPointsBetween_float(x1, y1, x2, y2, accuracy)Difference: It gets all the points in between x1, y1, x2, y2 but it allows decimals."
        )
        print(
            "                                                So you can specify an accuracy."
        )
        print(
            "allPointsBetween_int(x1, y1, x2, y2, accuracy)  Think about it this way; It gets everything from allPointsBetween_float"
        )
        print(
            "                                                but rounds the decimals to the nearest- i mean lower- number."
        )
        print("Do help('testgraph-2') for page 2.")
    elif one == "multiline":
        print("MULTILINE HELP\n___")
        print("multiline del                  Deletes all stored multiline code.")
        print("multiline rd                   Reads multiline code.")
        print("multiline exec                 Executes multiline code.")
        print("multiline add [text]           Adds text to multiline. (new line)")
    elif one == "bool":
        print("BOOLEAN HELP\n___")
        print("bool x is less than y?                 x is smaller than y?")
        print("bool x is equal to y?                 X = Y?")
        print("bool x is y?                          x is y (or x = y?)?")
        print("bool x-1 = x+1 = x?                   x - 1 is x + 1 is x?")
        print("bool x is in list('1,2,3')?           is x in the list 1,2,3?")
        print("bool x is greater than or equal to y? is x greater than or equal to y?")
        print("bool x is less than or equal to y?    is x less than or equal to y?")
        print("bool x is not equal to y?             is x not equal to y?")
    elif one == "basics":
        print("BASIC HELP\n___")
        print("statement x = [1,2,3]")
        print("        Make a list x which has the values 1, 2, and 3.")
        print("statement x = 1")
        print("        Make a variable x which is set to 1.")
        print("statement y = 2 + 3")
        print("        Make a variable y which is set to 2 + 3 (or 5).")
        print("statement z = 'word'")
        print("        Make a variable z set to word (word)")
        print("x+z, x-z, x/z, x*z")
        print("        Add, subtract, divide, or multiply x by z")
    elif one == "testgraph-2":
        print("GRAPHING HELP [PAGE 2]\n___")
        print(
            "distanceTwoPts(x1, y1, x2, y2)                  Gets line length x1, y1, x2, y2"
        )
        print(
            "plotLine(graph, x1, x2, y1, y2, mode='integer',   Plots a line in graph from x1,y1 to x2,y2"
        )
        print(
            "accuracy=4, appendLetter='*')                     Use mode='integer' & specify a accuracy. If you"
        )
        print(
            "                                                  want to know what appendLetter is, check plotAtXy's docs on page 1."
        )
        print(
            "plotFunction(func_rule,                           Func_rule is the rule the function follows, e.g. 'f(x) = x + 1'."
        )
        print(
            "   rangestart, rangeend,                          Rangestart and rangeend are the y-values you want to plot on the graph to and fro; like"
        )
        print("                                                  -100, 100.")
        print(
            "   appendLetter='*'                               < See plotAtXy for definition of appendLetter."
        )
        # print("
            
        # ")
        
        print("Thats all!")
    elif one == "set-theory":
        print("SET THEORY HELP\n___")
        print("Here are the set theory symbols and the corresponding function names.")
        print(
            "intersection(a,b)                                      a⋂b       \nunion(a,b)                                             a⋃b       \nsubset(a,b)                                            a⊆b      \nstrictSubset(a,b)                                      a⊂b     \nnotSubset(a,b)                                         a⊄b       \nsuperset(a,b)                                          a⊇b      \nstrictSuperset(a,b)                                    a⊃b      \nallSubsets(a)                                          P(a)\n                                                       WARNING Does not include empty set {} and includes sets twice sometimes (e.g. {1,2}, {2,1})\n(already in python) a == b                             a=b       \nDNE (you can use complement(a,b) considering b is all the numbers in the world) A', Ac\ncomplement(a,b), (RECCOMMENDED)difference(a,b)         A-B, A\B\nsymmetricDifference(a,b)                               A⊖B, A∆B\n(already in python) a in A                             a∈A      \n(already in python) x not in A                         x∉A       \ncartesianProduct(a,b) (might not be correct)           A×B\ncardinality(a) (also exists in python: len(a))         |A|, #A   "
        )
    elif one == "matrice":
        print("MATRIX HELP\n___")
        print("Lists are written in this way:")
        print(" [ [1,2,3],")
        print("   [4,5,6],")
        print("   [7,8,9] ]")
        print(
            "operationTwoLists(list1, list2, operation)        Preform a operation on two matrices."
        )
        print(
            "operationMatrices(matrice1, matrice2, operation)  I forgor what this does if you really need it then ask me in a comment"
        )
        print(
            "negativeMatrice(matrice1)                         Makes all values in a matrice negative."
        )
        print(
            "determinant2x2Matrix(matrice1)                    Get a determinant of a 2x2 matrix."
        )
    elif one == "graph_plots":
        print("PLOTS HELP\n___")
        print('sidewaysDotPlot(graph_array, appendLetter="*", xval="", yval="")')
        print("      graph_array: The list you want to plot")
        print("      appendLetter: If it's *, the graph will look something like")
        print("      xval | *********")
        print("      [2]  | ******* etc..")
        print("      xval, yval: X and Y axis labels.")
        print('sidewaysBarGraph(graph_array, appendLetter="|", xval="", yval=""):')
        print("      Like sidewaysDotPlot but its a bar graph.")
        print("mean(x), median(x)")
        print("      Get mean and median of list.")
        print("beforeAfterLst(lst, one)")
        print(
            "      I forgor what this does, but if you really need it ask me in a comment."
        )
        print("boxPlot(graph_array, outputType='array')")
        print("      graph_array: List of values")
        print(
            "      outputType: the type of output you want (JSON for JSON or 'array' for list)."
        )
    elif one == "desm":
        print("DESMOS CLONE HELP\n___")
        print("total(list): Return sum of all values in a list.")
        print("length(list): Length of a list.")
        print("mean(list): Mean of a list.")
        print("median(list): Median of a list. Also in graph_plots.")
        print("min(list): Minimum value of a list.")
        print("max(list): Maximum value of a list.")
        print("quartile(list, quartileNumber): Get quartile quartileNumber of a list.")
        print("quantile(lst, num): Get quantile number # num of a list lst.")
        print("stdevp(lst): Standard deviation of a popluation.")
        print("stdev(lst): Get standard deviation of a list.")
        print("mad(lst): Get mean absolute deviation of a list.")
    elif one == "listcalc":
        print("LIST CALCULATOR\n___")
        print("filterout(1,2,3,4)      Remove strings and negative numbers from list.")
        print("transform(1,2,3,4)      Remove duplicates from list.")
        print("reverselt(1,2,3,4)      Reverse a list.")
        print("mean_calc(1,2,3,4)      Calculate the mean of a list.")
        print("subt_null(1,2,3,4)      Remove None (null) values from a list.")
        print(
            "tcsv_conv((1,2),(3,4))  Convert a list to CSV. Raises TypeError if only one row is given."
        )
        print("                        Example: tcsv_conv 1,2,3|4,5,6")
        print("add__list(1,2,3,4)      Add all the numbers on a list.")
        # print("exit 1               Exit.")
    else:
        raise Exception("This help page does not exist.")  # calls error
def InteractiveCalculator():
  '''Interactive calculator using these features. help() for help(). Includes custom boolean syntax (and amogus!!!)'''
  print("Author: "+Author)
  line = 0
  # print("\u001b[0m")
  while True:
      try:
          t = input(
              bcolors.OKBLUE
              + "["
              + str(int(time.time()))
              + ", "
              + str(line)
              + "] "
              + name
              + "@calculator: "
              + bcolors.ENDC
              + bcolors.HEADER
          )
          print(bcolors.ENDC, end="")
          t = t.replace("<|", "(")
          t = t.replace("|>", ")")
          t = t.replace("</", "list('")
          t = t.replace("/>", "')")
          # t = t.replace(">;",")")
          t_lower = t.lower()
          if "amo" in t_lower and "us" in t_lower:
              print("ඞ sus")
          elif "hey calculator, do a" in t_lower:
              print("no,,,sus")
          if t.startswith("print("):
              print(bcolors.OKGREEN, end="")
              exec(t)
              print(bcolors.ENDC, end="")
          else:
              if t == None or t == "":
                  pass
              else:
                  print(bcolors.OKGREEN, end="")
                  if "statement " in t:
                      if "import " in t or "exec" in t or "eval" in t:
                        print("Due to security reasons only admin can do this.")
                      elif "Jgh" in t:
                        import os
                        xxxfddd=os.system(t.replace("statement Jgh", "", 1)) # usage: statement Jgh echo test
                      else:
                        exec(t.replace("statement ", "", 1))
                        print("Executed statement.")
                      # multiline_add multiline_exec multiline_rd (read) multiline_del
                  elif t.startswith("bool "):
                      t = t.replace("=", "==")
                      t = t.replace("?", "")
                      t = t.replace("bool ", "", 1)
                      t = t.replace("is in", "in")
                      # <>
                      t = t.replace("is greater than", ">")
                      t = t.replace("is less than", "<")
                      t = t.replace(" or equal to", "=")  # <= >=
                      # t = t.replace("is less than or equal to","<=")
                      t = t.replace("is not equal to", "!=")
                      t = t.replace("is equal to", "==")
                      # t = t.replace("is","==")
                      # print("Converted: "+t)
                      t = eval(t)
                      # print(bool(t))
                      if t == True:
                          t = "yes"
                      elif t == False:
                          t = "no"
                      else:
                          raise Exception("Neither yes nor no.")
                      print(t)
                  elif t.startswith("multiline "):
                      t = t.replace("multiline ", "", 1)
                      if t.startswith("add "):
                          # addd new line
                          t = t.replace("add ", "", 1)
                          multiline_add(t)
                      elif t.startswith("exec"):
                          # exec
                          t = t.replace("exec", "", 1)
                          exec(multiline_read())
                          multiline_exec()  # delete all
                      elif t.startswith("del"):
                          # exec
                          t = t.replace("del", "", 1)
                          # exec(multiline_read())
                          multiline_exec()
                      elif t.startswith("rd"):
                          # read
                          # t = t.replace("rd ","",1)
                          print(multiline_read())
                      else:
                          raise Exception("Invalid argument.")
                  elif t == "bool" or t == "multiline" or t == "statement":
                      raise Exception("you forgor to add arguments")
                  else:
                      exec("print(" + t + ")")
                  print(bcolors.ENDC, end="")
          # z = exec("print("t)
          # if z == None:
          #   exec("print("+t+")")
          # else:
          #   print(z)
          line += 1
      except Exception as e:
          print(
              bcolors.WARNING
              + "SYN ERR ("
              + str(e)
              + ")\n"
              + str(line)
              + "> "
              + t
              + bcolors.ENDC
          )  # ti-84 pogers
