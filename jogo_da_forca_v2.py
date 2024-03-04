import random
from os import system, name

def visual_forca(chances):
    niveis = [
         """  
         ________
        |       |
        |      \O/
        |       |
        |      /|\  
        |        
        |         
    """,
      """  
         ________
        |       |
        |       O/
        |       |
        |      /|\  
        |        
        |         
    """,
      """  
         ________
        |       |
        |       O
        |       |
        |      /|\  
        |        
        |         
    """,
        """  
         ________
        |       |
        |       O
        |       |
        |       |\  
        |        
        |         
    """,  
       """  
         ________
        |       |
        |       O
        |       |
        |       |
        |        
        |         
    """ ,
      """  
         ________
        |       |
        |       O
        |       |
        |     
        |        
        |         
    """ ,
         """   
         ________
        |       |
        |       O
        |
        |
        |
        |         
    """,
    """  
         ________
        |       |
        |   
        |
        |
        |
        |         
    """,    
     """  
         ________
        |       
        |   
        |
        |
        | 
        |         
    """    
  ]
    print(niveis[chances])

def limpar_tela():
    if name == 'nt':
        p = system('cls')

def mostrar_itens(lista):
    for i in lista:
        print(i, end=' ')

def mostrar_chances():
    mostrar_itens(espacos)
    print(' ')
    print(f'Chances restantes = {chances_restantes}')
    print(f'Letras erradas:{letras_erradas}')

######################################################################################################
    
lista_palavras = [
'pao', 'televisao', 'filme', 'flamingo', 'batata',  'mao', 'sapo', 'nenhum', 'parede',
'sogra', 'maravilha','aguaceiro','perigo', 'piscar', 'cotovelo', 'retrato', 'bondade'
]

palavra = random.choice(lista_palavras)
chances_restantes = 8
letras_erradas = []
espacos = []


for i in range(len(palavra)):
   i = '_'
   espacos.append(i)
print('Bem vindo(a) ao Jogo da Forca!')
print('Adivinhe a palavra abaixo:')


while chances_restantes > 0:
    print(' ')

    mostrar_chances()

    
    input_letra = str(input('Digite uma letra: '))

    if input_letra in palavra:
        indice = 0

        for letra in palavra:
            if input_letra == letra:
                espacos[indice] = letra
            indice += 1
        
    else:
        letras_erradas.append(input_letra)
        visual_forca(chances_restantes)
        chances_restantes -= 1

    
    limpar_tela()

    visual_forca(chances_restantes)

    if '_' not in espacos:
        print(f'Parabéns, você acertou! A palavra era: {palavra}')
        break

    if chances_restantes == 0:
        print(f'Você perdeu! A palavra era: {palavra}')
