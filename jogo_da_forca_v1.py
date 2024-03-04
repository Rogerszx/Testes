import random
from os import system, name

def limpar_tela():
    if name == 'nt':
        p = system('cls')

def mostrar_itens(lista):
    for i in lista:
        print(i, end=' ')

def mostrar_chances():
    mostrar_itens(letras_certas)
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
letras_certas = ['_' for letra in palavra]
# espacos = []
input_letra = False



# for i in range(len(palavra)):
#    i = '_'
#    espacos.append(i)
print('Bem vindo(a) ao Jogo da Forca!')
print('Adivinhe a palavra abaixo:')

nova_palavra = ''

while chances_restantes > 0:
    print(' ')

    mostrar_chances()
    # print(' '.join(letras_certas))
    
    input_letra = str(input('Digite uma letra: '))
    if input_letra in palavra:
        indice = 0
        for letra in palavra:
            if input_letra == letra:
                letras_certas[indice] = letra
            indice += 1
        
    else:
        letras_erradas.append(input_letra)
        chances_restantes -= 1

    limpar_tela()


    if '_' not in letras_certas:
        print(f'Parabéns, você acertou! A palavra era: {palavra}')
        break

    if chances_restantes == 0:
        print(f'Você perdeu! A palavra era: {palavra}')

    

   
            

