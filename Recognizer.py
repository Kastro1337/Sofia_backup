# -*- coding: utf-8 -*-
import serial
import speech_recognition as sr
import Configurações
recog = sr.Recognizer()



def Fala():
    

    with sr.Microphone() as fonte:
        audio = recog.listen(fonte)
    

    try:    
    
        fala = recog.recognize_google(audio, language = 'pt-BR')
        return(fala)
    
    except sr.UnknownValueError:
        print('Desculpe, não entendi')
        fala = ' '
        return(fala)

