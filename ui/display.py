from pyfiglet import Figlet

class Ui():

    def display(self):
        f = Figlet(font="slant") 
        print(f.renderText("NORTH"))

        print("Iniciando a IA...")
        print("")
        print("Para sair digite (exit)")
        print("")
