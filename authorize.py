#sha512 usage?
import os

def isadmin(user):
  return os.environ['REPL_OWNER'] == user


#Lol, that is an authorizer?

def AOSauth():
  admin = ["mkcodes", "DeadWither"]
  worker = ["TheDiamondKing", "IanTang2","MarcosMacDonald"] 
  if os.environ['REPL_OWNER'] == "Ultrox":
    return "Owner"
  elif os.environ['REPL_OWNER'] in admin:
    return "Admin"
  elif os.environ['REPL_OWNER'] in worker:
    return "Worker"
  else:
    return "User"