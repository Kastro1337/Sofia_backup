# S.o.f.i.a   /config\
# -*- coding: utf-8 -*-



reconhecimento = 2


def Config(x = 'default'):
    
    global reconhecimento
    
    if x == 'default':
        return (reconhecimento)  #Configurações Padrão ( Reconhecimento por voz , em PT-Br)
#---------------------------------------------------------------------------------------------------------------------------------------------------------
    elif x == 'editar':
    
        print ('\n' * 40 , '--' * 30, )
        print(' Configurações do programa - Pessione o numero correspondente para alterar as conguraçoes')
        print('(1) - Ligar/desligar   Reconhecimento de voz  \n(Sair) - Para sair')
        con = str(input())
        if con == '1': reconhecimento += 1 # Se for impar Alterna entre ativo e não ativo
        elif con.lower() == 'sair' : None
        else: Config('editar')
#-------------------------------------------------------------------------------------------------------------------------------------------------------
    if reconhecimento % 2 == 0: return 'Voz'
    else: return 'Texto'
