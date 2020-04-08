import Jogo

forca = Jogo.jogo()
print(forca.exibe_dica())

while forca.fim_jogo()==2:
    forca.desenho()
    forca.recebe_letra()
    
    
    
