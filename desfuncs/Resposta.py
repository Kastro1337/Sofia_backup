# Teste 4 Machine learning eu acho
from similarity.normalized_levenshtein import NormalizedLevenshtein
normalized_levenshtein = NormalizedLevenshtein()

##perguntas_respostas = {'olá' : 'Como posso ajuda-lo?',
##                                            'bom dia' : 'Bom Dia!!',
##                                            'qual é seu filme preferido' :' Ex Machina!',
##                                             ' ' : ' ',
##                                             ' ' : ' ',
##                                             ' ' : ' ',
##                                             ' ' : ' ',
##                                             ' ' : ' ',
##                                             ' ' : ' ',
##                                             ' ' : ' ',
##                                             ' ' : ' '
##                           
##                           
##                           }

from similarity.normalized_levenshtein import NormalizedLevenshtein
normalized_levenshtein = NormalizedLevenshtein()

import os

pr_file = './perguntas_respostas.p'
import pickle
if os.path.isfile(pr_file):
    with open(pr_file, 'rb') as p:
        perguntas_respostas = pickle.load(p)


def maquinaAprendendo(fala):

    usuario = list(perguntas_respostas.keys())
    bot = list(perguntas_respostas.values())
   



    for i in range(len(usuario)):
      pergunta = usuario[i]
      #print(normalized_levenshtein.similarity(pergunta, fala))
      if (normalized_levenshtein.similarity(pergunta, fala)) >= 0.60:
          
          
          return perguntas_respostas[pergunta]
    
    #Não entendi
    adicionar = str(input('Não entendi, Como deseja que eu responda isso?'))
    perguntas_respostas.update({fala : adicionar})
    with open(pr_file, 'ab') as p:
        pickle.dump(perguntas_respostas, p)
