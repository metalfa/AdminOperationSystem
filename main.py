import admin_operations_system as aos
import authorize as auth
from chatbot import main
status = auth.AOSauth()
aos.Console.clear
aos.Console.warn("3ème année finance Compétences digitales (Programmation Python)")
aos.Misc.help() #TODO: Ansi, reference as file not PIP for certain modules (user-requested)
aos.Console.commentary("Admin Operations System")
aos.Console.type("Version 1.0\n")
aos.Misc.newline()
aos.Console.type("Project de Mohamed Aziz Ben Sassi ")
aos.Console.type("\Institut Supérieur de Gestion de Tunis /")
aos.Console.type("\Enseignante: Mme. Imen Oueslati\n")
aos.Misc.newline()
main()
