# -*- coding: utf-8 -*-
import serial
import speech_recognition as sr
import Configurações
recog = sr.Recognizer()



def Fala():
    

    with sr.Microphone() as fonte:
        audio = recog.listen(fonte)
    

    try:    
        linguagem = Configurações.Config('x')
        #print(linguagem[1])
        fala = recog.recognize_google(audio, language = linguagem[1])
        return(fala)
    
    except:
        print('Desculpe , não entendi')
        fala = ' '
        return(fala)

