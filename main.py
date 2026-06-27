from ui.display import Ui
from core.cliente import Cliente


while True:
    
    display = Ui.display()
    chat = Cliente.chat()

    message = input("> ")
    if str(message).strip() == "exit":
        break

    
   

        