import luces
from time import sleep

luces=luces.Luces()

while True:
    luces.encendertodas()
    sleep(1)
    luces.apagartodas()
    sleep(1)
