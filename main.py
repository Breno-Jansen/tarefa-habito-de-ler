import os

def inicio(): # Aqui estão presentes as entradas como Nome, Idade, Cidade e Estado
    print ('Bem vindo ao Reading Habits!')
    print('Aqui você recebe estatisticas, dicas e estimativas sobre seu hábito de leitura')
    nome = input('Para começar digite seu nome: ')
    nome = nome.capitalize()
    while True:
        sexo = input('Sexo: \n1. Feminino \n2. Masculino \nOpção (1 ou 2): ')
        if sexo == '1':
            sexo = 'feminino'
            break
        elif sexo == '2':
            sexo = 'masculino'
            break
        else:
            print('Opção inválida')
    while True:
        try:
            idade = int(input('Idade: '))
            break                        # Tratamento de erro para só receber numeros
        except ValueError:
            print('Resposta inválida: digite o número correspondente a sua idade: ')

    while True:
        estado = input('Seu estado (Sigla. Exemplo: PE): ').strip()
        estado = estado.upper()
    
        nordeste = ['PE','MA','PI','CE','RN','PB','AL','SE','BA']
        norte = ['AC','AP','AM','PA','RO','RR','TO']
        centro = ['GO','MT','MS','DF']                # Separando estados pelas regiões
        sudeste = ['ES','MG','RJ','SP']
        sul = ['PR','SC','RS']
        
        if estado in nordeste:
            regiao = 'Nordeste'
            media_regiao = 2.9
            break
        elif estado in norte:
            regiao = 'Norte'
            media_regiao = 3.4
            break
        elif estado in centro:          # Achando a região do estado digitado.
            regiao = 'Centro Oeste'     
            media_regiao = 3.8          # Média de leitura por ano, por região retirada
            break
        elif estado in sudeste:         # da Pesquisa Retratos da Leitura no Brasil 2024.
            regiao = 'Sudeste'
            media_regiao = 4.5
            break
        elif estado in sul:
            regiao = 'Sul'
            media_regiao = 5
            break
        else:
            print('Estado inválido. Digite um estado do Brasil')

    cidade =  input('Sua cidade: ')

    menu(nome, sexo, idade, regiao, media_regiao)


def menu(nome, sexo, idade, regiao, media_regiao):
    limpar_terminal()
    titulo()
    print(f'{nome}, nos conte mais sobre seus dias de leitura:')
    while True:
        try:
            digitais_ano = int(input('Quantos livros digitais você leu no ultimo ano? '))
            break               # Tratamento de erro para só receber numeros
        except ValueError:
            print('Resposta inválida: digite um número: ')
    
    while True:
        try:
            fisicos_ano = int(input('E quantos físicos? '))
            break               # Tratamento de erro para só receber numeros
        except ValueError:
            print('Resposta inválida: digite um número: ')
    
    print('Qual estilo você prefere?')
    print('1. Livro físico, prefiro ler no papel \n2. Livro digital, gosto de ler nas telas')
    while True:
        preferencia = input('Opção (1 ou 2): ').strip()
        if preferencia == '1' or '2':
            break
        else:
            print('Opção inválida')
    limpar_terminal()
    titulo()
    horas_estudo = input('Anotado. \nQuantas horas você passa lendo para estudo por semana: ')
    horas_entretenimento = input('E para o seu entretenimento? ')

    leitura_ano = estimativas(nome, digitais_ano, fisicos_ano, horas_estudo, horas_entretenimento)
    regiao_comparacao(nome, regiao, media_regiao, leitura_ano)
    media_idade(nome, sexo, idade)


def estimativas(nome, digitais_ano, fisicos_ano, horas_estudo, horas_entretenimento):
    limpar_terminal()
    titulo()
    print(f'Agora vamos trazer algumas estimativas e curiosidades a partir dos seus dados!\n')
    leitura_ano = digitais_ano + fisicos_ano
    leitura_cinco_anos = leitura_ano * 5
    print(f'{nome}, você leu {leitura_ano} livros no último ano')
    
    print(f'Se continuar nesse ritmo você vai ter lido {leitura_cinco_anos} livros a mais daqui a 5 anos')
    estudo_ano = int(horas_estudo) * 52
    entretenimento_ano = int(horas_entretenimento) * 52
    print(f'{nome}, em 1 ano você consome em média {estudo_ano} horas em livros para estudar e consome {entretenimento_ano} para seu entretenimento')
    input('Aperte qualquer tecla para continuar')
    return leitura_ano

def regiao_comparacao(nome, regiao, media_regiao, leitura_ano):
    limpar_terminal()
    titulo()
    print(f'{leitura_ano} livros no total')
    porcentagem_camparacao = (leitura_ano / media_regiao) * 100
    porcentagem_camparacao = round(porcentagem_camparacao)
    if porcentagem_camparacao > 150:
        print(f'Isso representa {porcentagem_camparacao}% a mais do que a média de livros lido na sua região {regiao}: {media_regiao}')
        print(f'Parabéns, {nome}! Você esta acima da média, continue assim.')
    elif porcentagem_camparacao < 70:
        print(f'Isso representa {porcentagem_camparacao}% da média de livros lido na sua região {regiao}: {media_regiao}')
        print(f'{nome}, leia mais. A média anual dos brasileiros é considerada baixa.')
    else:
        print(f'Isso representa {porcentagem_camparacao}% da média de livros lido na sua região {regiao}: {media_regiao}')
        print(f'Você está perto da média. Considere ler mais, {nome}')
    input('Aperte qualquer tecla para continuar')

def media_idade(nome, sexo, idade):
    limpar_terminal()
    titulo()
    print(nome, sexo, idade)

    
def titulo():
    print('🇷​​​​​ 🇪​​​​​ 🇦​​​​​ 🇩​​​​​ 🇮​​​​​ 🇳​​​​​ 🇬​​​​​    🇭​​​​​ 🇦​​​​​ 🇧​​​​​ 🇮​​​​​​​​​​ 🇹​​​​​ 🇸​​​​​')

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    limpar_terminal()
    inicio()
if __name__ == '__main__':
    main()  