# -*- coding: utf-8 -*-
import serial
import speech_recognition as sr
import Configurações
recog = sr.Recognizer()



def Fala():
    

    with sr.Microphone() as fonte:
        audio = recog.listen(fonte)
    

    
    linguagem = Configurações.Config('x')
    #print(linguagem[1])
    fala = recog.recognize_google(audio, language = linguagem[1])
    return(fala)
    
    

