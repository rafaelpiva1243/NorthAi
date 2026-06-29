from ui.display import Ui
from core.context import Context
from core.chat import Chat

display = Ui().display()
context_obj = Context()
chat = Chat()

while True:
    message = input("> ")
    if str(message).strip() == "exit":
        break

    context, completo = context_obj.message(message)

    if completo:
        res = chat.context(message)
        for a in res:
            print(a.text)
    else:
        res = chat.no_context(message)
        for b in res:
            print(b.text)     