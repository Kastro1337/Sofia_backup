# -*- coding: utf-8 -*-
import speech_recognition as sr
#import Configurações
import Tts as tts
recog = sr.Recognizer()



def Fala():
    

    with sr.Microphone() as fonte:
        recog.adjust_for_ambient_noise(fonte) # Ajuste de ruido
        audio = recog.listen(fonte)           #
        
    

    try:    
        #linguagem = Configurações.Config('x')
        #print(linguagem[1])
        fala = recog.recognize_sphinx(audio, language = "pt-BR")
        
        return(fala)
    
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        # da documentacao

    except:
        print('Desculpe , não entendi')
        tts.BERRO('Desculpe, não entendi')
        fala = ' '
        return(fala)
    

