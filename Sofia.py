# -*- coding: cp1252 -*-
import Configura��es 
import Recognizer
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import serial
from tts_Dispatch import BERRO
config_ = Configura��es.Config() #Default

print('-' *100)
nome_do_bot = str(input('Como deseja que Bot se chame: '))
print('-' *100)


try:
    porta = str(input('Digite a porta em que est� conectado seu arduino '))
    ser = serial.Serial(porta.upper())  # Abre uma porta

except:
    porta = str(input(porta + ' n�o � uma porta valida, digite-a novamente: '))
    ser = serial.Serial(porta.upper())


#------------------Treinamento_do_bot---------------------------------
bot = ChatBot(nome_do_bot)          
trainer = ListTrainer(bot)                  
trainer.train([
   'Ol�!',
   "Como posso ajud�-lo?",                                                     
   '',                                                                                             
   'Bom dia'                                                                                            
 ])                                                                                                 
                                                                                                    
#-----------------------------------------------------------------------------------
print ("Diga Ol�!: ")
while True:

    
    if  config_ ==  'Voz':
        print('Ouvindo \n')
        fala = Recognizer.Fala()  # Reconhecimento de voz
        
    else: fala = str(input('Digite sua fala ')) # String de texto (modo sem voz)

    
    print("Voc�: "+fala)
 

    #------------------------------------------------------------------------------------------------
    if "deslig" in fala.lower() or 'apag' in fala.lower():
        if 'luz' in fala.lower() or 'rele um' in fala.lower(): ser.write(b"\x00")
        if 'ventilador' in fala.lower() or 'rele dois' in fala.lower(): ser.write(b'\x02')
        #
        #
    
    elif  "lig" in fala.lower() or 'acend' in fala.lower():
        if 'luz' in fala.lower() or 'rele um' in fala.lower(): ser.write(b"\x01")
        if 'ventilador' in fala.lower() or 'rele dois' in fala.lower(): ser.write(b'\x03')
        #
        #


        
    #------------------------------------------------------------------------------------------------
    elif fala.lower() == 'configura��es': config_ = Configura��es.Config('editar')

    if fala.lower() == 'tchau': quit()


    
    else:
        resp = bot.get_response(fala)
        print(nome_do_bot ,':', resp)
        Berro(resp)
        
