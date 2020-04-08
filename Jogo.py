import requests
import random
import unicodedata
import re
from bs4 import BeautifulSoup

class jogo():
    
    def __init__(self):
        self.acertos = 0
        self.erros = 0
        self.palavra_secreta=""
        self.palavra_correta=""
        self.tentativas = []
        
        #self.tema = self.selecionar_tema()
        self.tema="1-Esporte"
        self.frase = self.pega_frase(self.tema)
        self.palavra_suja = self.pega_palavra(self.frase)
        self.palavra_limpa = self.limpa_palavra(self.palavra_suja)
        self.palavra_secreta = "_"* len(self.palavra_limpa)
        
    def selecionar_tema(self):
        temas = ["1-Esporte","2-Novelas", "3-Politica", "4-Mundo", "5-Saude"]
        
        print("Selecione um dos seguintes temas:")
        for t in temas:
            print(t)
        
        tema_escolhido = int(input("Insira o numero:"))
        
        while tema_escolhido not in list(range(1,len(temas)+1)):
            print("Este tema não existe")
            tema_escolhido = input("Insira o numero:")
        
        return temas[tema_escolhido-1]
        
    
    def pega_frase(self,tema):
        try:
            if tema == "1-Esporte":
                url = 'https://www.uol.com.br/esporte'
                page = requests.get(url)
                soup = BeautifulSoup(page.content, 'html.parser')
                frases = soup.find_all('h3', class_="thumb-title")
                return frases[random.randint(0,len(frases)-1)].string
        except Exception as err:
            print(err)
            print("Site fora do ar")
            return("bola")
            
    def pega_palavra(self,frase):
        lista_palavras = frase.split()
        filtro_palavras_permitidas = filter(lambda x : len(x)>3 , lista_palavras)
        lista_palavras_permitidas = [p for p in filtro_palavras_permitidas]
        #for p in filtro_palavras_permitidas:
        #    lista_palavras.append(p)
        p = lista_palavras_permitidas[random.randint(0,len(lista_palavras_permitidas)-1)]
        return p
    
    def limpa_palavra(self,palavra):
        nfkd = unicodedata.normalize('NFKD', palavra)
        palavraSemAcento = u"".join([c for c in nfkd if not unicodedata.combining(c)])
        self.palavra_correta = re.sub('[^a-zA-Z \\\]', '', palavraSemAcento).upper()
        return self.palavra_correta
    
    def exibe_dica(self):
        tracinhos="_ "*len(self.palavra_limpa)
        return self.frase.replace(self.palavra_suja,tracinhos)
    
    def desenho(self):
        print(self.palavra_secreta)
    
    def recebe_letra(self,letter):
        #letra = input("Digite uma letra: ").upper()
        letra = letter
        if letra not in self.tentativas:
            
            self.tentativas.append(letra)
            
            if letra in self.palavra_limpa.upper():
                #print("acertou")
                self.acertos+=1
                self.atualiza_palavra_secreta(letra)
            else:
                #print("errou")
                self.erros+=1
        else:
            self.recebe_letra()
            
    def recebe_letra(self):
        letra = input("Digite uma letra: ").upper()
        #letra = letter
        if letra not in self.tentativas:
            
            self.tentativas.append(letra)
            
            if letra in self.palavra_limpa.upper():
                #print("acertou")
                self.acertos+=1
                self.atualiza_palavra_secreta(letra)
            else:
                #print("errou")
                self.erros+=1
        else:
            self.recebe_letra()
        
    
    def atualiza_palavra_secreta(self,letra):
        for posicao,l in enumerate(self.palavra_correta):
            if l == letra:
                self.palavra_secreta = self.palavra_secreta[:posicao]+letra+self.palavra_secreta[posicao+1:]
        
    def fim_jogo(self):
        if self.erros == 6:
            print("Morreu!")
            print("A palavra correta eh:", self.palavra_correta)
            print(self.frase)
            return 0 
        elif self.palavra_secreta == self.palavra_correta:
            print("Acertou miseravi! Acertou: {} e Errou: {}".format(self.acertos, self.erros))
            #print("A palavra correta eh:", self.palavra_correta)
            print(self.frase)
            return 1
        else:
            return 2
