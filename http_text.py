import uasyncio
from microdot_asyncio import Microdot
from atom.matrix import Matrix
from atom.button import Button
import network
import secrets
from wekan import Wekan

def button_pressed(btn):
    print("Button pressed")
    matrix.fill((10,0,0))
    #last_card = taches.get_last_card(secrets.wekan_board, secrets.wekan_todolist)
    #card_info = taches.get_card_info(secrets.wekan_board, secrets.wekan_todolist, last_card)
    #card_info = card_info.json()
    #matrix.text_color((0,0,10))
    #matrix.text(card_info["title"])
    #matrix.last_card = last_card

def button_hold(btn):
    print("Button holded")
    matrix.fill((0,10,0))
    #taches.add_time(secrets.wekan_board, secrets.wekan_todolist, matrix.last_card)
    #matrix.text("")

ip = network.WLAN().ifconfig()[0]
app = Microdot()

matrix = Matrix()

button = Button()
button.handler.set_press_handler(button_pressed)
button.handler.set_hold_handler(button_hold)

#taches = Wekan(secrets.wekan_url, secrets.wekan_username, secrets.wekan_password) 

# Type : http://ip/show?text=Hello
@app.route("/show")
async def change_text(request):
    print(request.args)
    try:
        print(request.args["text"])
        matrix.text_color((10,0,0))
        matrix.text(request.args["text"])
    except:
        print("No text")
    return "OK"

matrix.text(ip)
uasyncio.create_task(app.run(port=80, debug=True))

