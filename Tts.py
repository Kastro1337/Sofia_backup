'''
Criado pelo Kastro pq eu to pistol e nao consegui usar PYTTSX
Essa merda serve pra falar em voz alta
        github.com/Kastro1337/
'''

from win32com.client import Dispatch
voz = Dispatch("SAPI.SpVoice")

def BERRO(besteira): #INSPIRADOR
    voz.speak(str(besteira))

# BTW so funfa no uindouns, pnc do linux
