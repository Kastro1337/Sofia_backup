# -*- coding: cp1252 -*-
import Configurações
import Pesqusia
import Recognizer
import Resposta
import serial
from Tts import BERRO

config_ = Configurações.Config() #Default


print('-' *100)
nome_do_bot = str(input('Como deseja que Bot se chame: '))
print('-' *100)


try:
    porta = str(input('Digite a porta em que está conectado seu arduino '))
    ser = serial.Serial(porta.upper())  # Abre uma porta

except:
    porta = str(input(porta + ' não é uma porta valida, digite-a novamente: '))
    ser = serial.Serial(porta.upper())



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
    elif 'pesquise sobre' in fala.lower():
        fala = fala.strip('pesquise sobre')
        Pesquisa.pesquisa(fala)    

        
    elif fala.lower() == 'configurações': config_ = Configurações.Config('editar')

    if fala.lower() == 'tchau': quit()


    
    else:
        maquinaApredendo(fala)
        print(nome_do_bot ,':', resp)
        BERRO(resp)
        
