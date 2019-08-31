# -*- coding: utf-8 -*-
from sys import path
path.append('desfuncs/')
import Configurações 
import Recognizer
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import serial
config_ = Configurações.Config() #Default
loop = 0

print('-' *100)
nome_do_bot = str(input('Como deseja que Bot se chame: '))
print('-' *100)

while loop != 1:
    try:
        porta = str(input('Digite a porta em que está conectado seu arduino '))
        ser = serial.Serial(porta.upper())  # Abre uma porta
        loop = 1
    except:
        print(porta + ' não é uma porta valida, digite-a novamente: ')
        
        


#------------------Treinamento_do_bot---------------------------------
bot = ChatBot(nome_do_bot)          
trainer = ListTrainer(bot)                  
trainer.train([
   'Olá!',
   "Como posso ajuda-lo?",                                                     
   'Bom dia',                                                                                             
   'Tudo bem?'
   'Como?'
   'Sim'
   'Não'
   'Bom'
   'Ruim'
   'Com certeza'
   'Claro'
   'Negativo'
   'Claro que não'
   'Boa noite'
   'Boa tarde'
   'RETARDED'
   'Nazismo'
   'Suicidio, eu apoio!'
 ])                                                                                                 
                                                                                                    
#-----------------------------------------------------------------------------------
print ("Diga Olá!: ")
while True:

    
    if  config_ ==  'Voz':
        print('Ouvindo \n')
        fala = Recognizer.Fala()  # Reconhecimento de voz

        
    else: fala = str(input('Digite sua fala ')) # String de texto (modo sem voz)

    
    print("Você: "+fala)
 

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
    elif fala.lower() == 'configurações': config_ = Configurações.Config('editar')

    if fala.lower() == 'tchau': quit()


    
    else:
        resp = bot.get_response(fala)
        print(nome_do_bot ,':', resp)
        
