# S.o.f.i.a   /config\
# -*- coding: utf-8 -*-


linguagem = 'pt-BR'
reconhecimento = 2
lig_c = 0 

def Config(x):
    global lig_c
    global linguagem 
    global reconhecimento
    
    if x == 'default':
        return (reconhecimento , linguagem)

    elif x == 'editar':
        print('\n' * 40)
        print ('--' * 30)
        print(' Configurações do programa - Pessione o numero correspondente para alterar as conguraçoes')
        print('(1) - Ligar/desligar   Reconhecimento de voz \n(2) - Portugues/Ingles  \n(Sair) - Para sair')
        con = str(input())
        if con == '1': reconhecimento += 1 # Se for impar Alterna entre ativo e não ativo
        elif con == '2' :  lig_c += 1
        elif con.lower == 'sair' : None        


        if lig_c % 2 == 0:
            linguagem = 'pt-BR'
        
        else:
            linguagem = "en-US"

    return (reconhecimento, linguagem)  
