# -*- coding: utf-8 -*-
import speech_recognition as sr
import Configurações
import Tts as tts
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
        tts.BERRO('Desculpe, não entendi')
        fala = ' '
        return(fala)

