import luces
import time
quecolor=raw_input("que color?")
tiempo=raw_input("cuanto tiempo?")
tiempo=int(tiempo)
quecolorb=raw_input("que color2?")
tiempod=raw_input("cuanto tiempo?")
tiempod=int(tiempod)                    
luces=luces.Luces()
luces.encendercolor(quecolor,tiempo)
time.sleep(tiempo)
luces.apagarcolor(quecolor)
luces.encendercolor(quecolorb,tiempod)
time.sleep(tiempod)
luces.apagarcolor(quecolorb)
