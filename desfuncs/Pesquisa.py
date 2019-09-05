#Pesquisa bixo Kkkkkkkkkkkkkkkk
from googlesearch import search
import webbrowser

def  pesquisa(tema_da_pesquisa):
     for url in search(tema_da_pesquisa, stop= 1):
          #print (url)
          webbrowser.open(url)
