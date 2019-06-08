import Configurações 
import Recognizer
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import serial
config_ = Configurações.Config('default') #Default



print('-' *100)

nome_do_bot = str(input('Como deseja que Bot se chame: '))

print('-' *100)

porta = str(input('Digite a porta serial em que esta conectado seu arduino: ')).upper()

bot = ChatBot(nome_do_bot)
#trainer = ChatterBotCorpusTrainer(bot)
#trainer.train([
#  'Oi',
#   'Olá!'
# ])

ser = serial.Serial(porta)  # Abre uma porta


print ("Diga Olá!: ")
while True:

    
    if  config_[0] % 2 == 0:
        print('"Ouvindo"')
        fala = Recognizer.Fala()  # Reconhecimento de voz
        
    else: fala = str(input('Digite sua fala ')) # String de texto (modo sem voz)

    
    print("Você: "+fala)

    if fala.lower() == "tchau":
        print(nome_do_bot , ': Tchau! ')
        quit()

    #------------------------------------------------------------------------------------------------
    elif fala.lower() == 'ligar luz' or fala.lower() == "ligue a luz":  ser.write(b"\x01")

    elif fala.lower() == "desligar luz" or fala.lower() == "desligue a luz":     ser.write(b"\x00")

        
    #------------------------------------------------------------------------------------------------
    elif fala.lower() == 'configurações': config_ = Configurações.Config('editar')
    
    else:
        resp = bot.get_response(fala)
        print(nome_do_bot ,':', resp)
        
