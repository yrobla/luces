#####################################################
## Wrapper module for PiGlow to be used by chidren ##
##                                                 ##
## Written by Yolanda Robla  -  v0.1               ##
##            info@ysoft.biz                       ##
#####################################################
##
## v0.1 - Initial release                    - 15/08/13
##

from piglow import PiGlow
import math
import time

class Luces:
    def __init__(self):
        self.piglow = PiGlow()

    def get_intensity(self, value):
        pass
            
    def encenderblanco(self, value=100):
        self.piglow.white(value)

    def apagarblanco(self):
        self.piglow.white(0)

    def parpadearblanco(self, tiempo=1, value=100):
        self.encenderblanco(value)
        time.sleep(tiempo)
        self.apagarblanco()

    def encenderazul(self, value=100):
        self.piglow.blue(value)

    def apagarazul(self):
        self.piglow.blue(0)

    def parpadearazul(self, tiempo=1, value=100):
        self.encenderazul(value)
        time.sleep(tiempo)
        self.apagarazul()

    def encenderverde(self, value=100):
        self.piglow.green(value)

    def apagarverde(self):
        self.piglow.green(0)

    def parpadearverde(self, tiempo=1, value=100):
        self.encenderverde(value)
        time.sleep(tiempo)
        self.apagarverde()

    def encenderamarillo(self, value=100):
        self.piglow.yellow(value)

    def apagaramarillo(self):
        self.piglow.yellow(0)

    def parpadearamarillo(self, tiempo=1, value=100):
        self.encenderamarillo(value)
        time.sleep(tiempo)
        self.apagaramarillo()

    def encendernaranja(self, value=100):
        self.piglow.orange(value)

    def apagarnaranja(self):
        self.piglow.orange(0)

    def parpadearnaranja(self, tiempo=1, value=100):
        self.encendernaranja(value)
        time.sleep(tiempo)
        self.apagarnarnanja()

    def encenderrojo(self, value=100):
        self.piglow.red(value)

    def apagarrojo(self):
        self.piglow.red(0)

    def parpadearrojo(self, tiempo=1, value=100):
        self.encenderrojo(value)
        time.sleep(tiempo)
        self.apagarrojo()

    def encendertodas(self, value=100):
        self.piglow.all(value)

    def apagartodas(self):
        self.piglow.all(0)

    def parpadeartodas(self, tiempo=1, value=100):
        self.encendertodas(value)
        time.sleep(tiempo)
        self.apagartodas()

    def encenderbrazo(self, arm, value=100):
        self.piglow.arm(arm, value)

    def apagarbrazo(self, arm):
        self.piglow.arm(arm, 0)

    def parpadearbrazo(self, arm, tiempo=1, value=100):
        self.encenderbrazo(arm, value)
        time.sleep(tiempo)
        self.apagarbrazo(arm)

    def encenderbrazo1(self, value=100):
        self.piglow.arm1(value)

    def apagarbrazo1(self):
        self.piglow.arm1(0)

    def parpadearbrazo1(self, tiempo=1, value=100):
        self.encenderbrazo1(value)
        time.sleep(tiempo)
        self.apagarbrazo1()

    def encenderbrazo2(self, value=100):
        self.piglow.arm2(value)

    def apagarbrazo2(self):
        self.piglow.arm2(0)

    def parpadearbrazo2(self, tiempo=1, value=100):
        self.encenderbrazo2(value)
        time.sleep(tiempo)
        self.apagarbrazo2()

    def encenderbrazo3(self, value=100):
        self.piglow.arm3(value)

    def apagarbrazo3(self):
        self.piglow.arm3(0)

    def parpadearbrazo3(self, tiempo=1, value=100):
        self.encenderbrazo3(value)
        time.sleep(tiempo)
        self.apagarbrazo3()

    def encendercolor(self, colour, value=10):
        if colour == 1 or colour == "blanco":
            self.piglow.colour("white", value)
        elif colour == 2 or colour == "azul":
            self.piglow.colour("blue", value)
        elif colour == 3 or colour == "verde":
            self.piglow.colour("green", value)
        elif colour == 4 or colour == "amarillo":
            self.piglow.colour("yellow", value)
        elif colour == 5 or colour == "naranja":
            self.piglow.colour("orange", value)
        elif colour == 6 or colour == "rojo":
            self.piglow.colour("red", value)
        else:
            print "Solo los colores de 1 - 6 o los nombres de colores estan permitidos"

    def apagarcolor(self, colour):
        value = 0

        if colour == 1 or colour == "blanco":
            self.piglow.colour("white", value)
        elif colour == 2 or colour == "azul":
            self.piglow.colour("blue", value)
        elif colour == 3 or colour == "verde":
            self.piglow.colour("green", value)
        elif colour == 4 or colour == "amarillo":
            self.piglow.colour("yellow", value)
        elif colour == 5 or colour == "naranja":
            self.piglow.colour("orange", value)
        elif colour == 6 or colour == "rojo":
            self.piglow.colour("red", value)
        else:
            print "Solo los colores de 1 - 6 o los nombres de colores estan permitidos"

    def parpadearcolor(self, colour, tiempo=1, value=100):
        self.encendercolor(colour, value)
        time.sleep(tiempo)
        self.apagarcolor(colour)

    def encenderluz(self, led, value=100):
        self.piglow.led(led, value)

    def apagarluz(self, led):
        self.piglow.led(led, 0)

    def parpadearluz(self, led, tiempo=1, value=100):
        self.encenderluz(led, value)
        time.sleep(tiempo)
        self.apagarluz(led)
