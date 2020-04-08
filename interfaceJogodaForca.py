from tkinter import *
from tkinter import messagebox
from string import ascii_uppercase
import random
import Jogo


window = Tk()
window.title("Jogo da Forca")

photos = [PhotoImage(file="/home/marciosaraiva/Desktop/Lets Code/Projetos/Forca/imagens/forca5.png"),
          PhotoImage(file="/home/marciosaraiva/Desktop/Lets Code/Projetos/Forca/imagens/forca6.png"),
          PhotoImage(file="/home/marciosaraiva/Desktop/Lets Code/Projetos/Forca/imagens/forca7.png"),
          PhotoImage(file="/home/marciosaraiva/Desktop/Lets Code/Projetos/Forca/imagens/forca8.png"),
          PhotoImage(file="/home/marciosaraiva/Desktop/Lets Code/Projetos/Forca/imagens/forca9.png"),
          PhotoImage(file="/home/marciosaraiva/Desktop/Lets Code/Projetos/Forca/imagens/forca10.png"),
          PhotoImage(file="/home/marciosaraiva/Desktop/Lets Code/Projetos/Forca/imagens/forca11.png")]

def newGame():
    global the_word_withSpaces
    global numberOfGuesses
    numberOfGuesses = 0
    imgLabel.config(image=photos[0])
    the_word=random.choice(word_list)
    the_word_withSpaces=" ".join(the_word)
    lblWord.set(" ".join("_"*len(the_word)))
    
def inicializa_interface(palavra):
    global the_word_withSpaces
    global numberOfGuesses
    numberOfGuesses = 0
    imgLabel.config(image=photos[0])
    the_word=palavra
    the_word_withSpaces=" ".join(the_word)
    lblWord.set(" ".join("_"*len(the_word)))
    
def guess(letter,frase):
    global numberOfGuesses
    if numberOfGuesses<6:
        txt=list(the_word_withSpaces)
        guessed=list(lblWord.get())
        if the_word_withSpaces.count(letter)>0:
            for c in range(len(txt)):
                if txt[c]==letter:
                    guessed[c]=letter
                lblWord.set("".join(guessed))
                if lblWord.get()==the_word_withSpaces:
                    messagebox.showinfo("Jogo da Forca","Você venceu!")
                    messagebox.showinfo("A frase era...",frase)
                    run()
        else:
            numberOfGuesses+=1
            imgLabel.config(image=photos[numberOfGuesses])
            if numberOfGuesses==6:
                messagebox.showwarning("Jogo da Forca", "Game Over")
                messagebox.showinfo("A frase era...",frase)
                run()

imgLabel=Label(window)
imgLabel.grid(row=1, column=0, columnspan=3, padx=10, pady=40)
imgLabel.config(image=photos[0])

lblWord=StringVar()
Label(window,textvariable=lblWord, font=("Consolas 24 bold")).grid(row=1, column=3, columnspan=6, padx=10)

n=0
for c in ascii_uppercase:
    Button(window, text=c, command=lambda c=c: guess(c,frase), font =("Helvetica 18"), width=4).grid(row=2+n//9, column=n%9)
    n+=1

Button(window, text="Novo\njogo", command=lambda:run(), font=("Helvetica 10 bold")).grid(row=4, column=8, sticky="NSWE")


#Lógica
def run():
    global frase
    forca = Jogo.jogo()
    dica = forca.exibe_dica()
    frase = forca.frase
    messagebox.showinfo("Dica",dica)
    palavra = forca.palavra_limpa
    inicializa_interface(palavra)
    
run()
window.mainloop()
