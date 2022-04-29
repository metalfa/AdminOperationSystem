import admin_operations_system as aos
import authorize as auth
from chatbot import main
status = auth.AOSauth()
aos.Console.clear
aos.Console.warn("OWNED BY [VIR]\nVisions Into Reality")
aos.Misc.help() #TODO: Ansi, reference as file not PIP for certain modules (user-requested)
aos.Console.commentary("Admin Operations System")
aos.Console.type("Version 1.0\n")
aos.Misc.newline()
aos.Console.type("Here are available CDNs for installing AOS as well as docs and our discord server: ")
aos.Console.type("\nDeadWither's CDN for installation: https://aos-installer.deadwither.repl.co/")
aos.Console.type("\n[NOT UPDATED] Mkcodes CDN w/ markdown file from deadwither: https://aos-docs.mkcodes.repl.co/.\n")
aos.Console.warn("DISCORD SERVER: https://discord.gg/5p2ej78b6K")
aos.Misc.newline()
main()
