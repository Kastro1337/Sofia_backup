import Configurações 
import Recognizer
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import serial
config_ = Configurações.Config('default') #Default

print('-' *100)
nome_do_bot = str(input('Como deseja que Bot se chame: '))
print('-' *100)

try:
    porta = str(input('Digite a porta serial em que esta conectado seu arduino: ')).upper()
    ser = serial.Serial(porta)  # Abre uma porta

except:
    porta = str(input(porta + ' não é uma porta valida, digite-a novamente: ')).upper()
    ser = serial.Serial(porta)
    
    

#------------------Treinamento_do_bot---------------------------------
bot = ChatBot(nome_do_bot)          
trainer = ListTrainer(bot)                  
trainer.train([
   'Olá!',
   "Como posso ajuda-lo?"
 ])

#-----------------------------------------------------------------------------------
print ("Diga Olá!: ")
while True:

    
    if  config_[0] % 2 == 0:
        print('~Ouvindo')
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
        
