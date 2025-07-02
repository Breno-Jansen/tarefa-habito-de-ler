import os

def inicio(): # Aqui estão presentes as entradas como Nome, Idade, Cidade e Estado
    print ('Bem vindo ao Reading Habits!')
    print('Aqui você recebe estatisticas, dicas e estimativas sobre seu hábito de leitura.')
    nome = input('Para começar digite seu nome: ')
    nome = nome.title()
    while True:
        sexo = input('Sexo: \n1. Feminino \n2. Masculino \nOpção (1 ou 2): ')
        if sexo == '1':
            sexo = 'feminino'
            break
        elif sexo == '2':
            sexo = 'masculino'
            break
        else:
            print('Opção inválida.')
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
            print('Estado inválido. Digite um estado do Brasil.')

    cidade =  input('Sua cidade: ')
    cidade = cidade.title()

    dados(nome, sexo, idade, cidade, regiao, media_regiao)


def dados(nome, sexo, idade, cidade, regiao, media_regiao):
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
    print('1. Livro físico, prefiro ler no papel. \n2. Livro digital, gosto de ler nas telas.')
    while True:
        preferencia = input('Opção (1 ou 2): ').strip()
        if preferencia == '1':
            preferencia = '1'
            break
        elif preferencia =='2':
            preferencia = '2'
            break
        else:
            print('Opção inválida')
    limpar_terminal()
    titulo()
    horas_estudo = input('Anotado. \nQuantas horas você passa lendo para estudo por semana: ')
    horas_entretenimento = input('E para o seu entretenimento? ')

    leitura_ano = estimativas(nome, digitais_ano, fisicos_ano, horas_estudo, horas_entretenimento)
    regiao_comparacao(nome, cidade, regiao, media_regiao, leitura_ano)
    dados_sociedade(nome, sexo, idade)
    vantagens_disvantagens(preferencia)


def estimativas(nome, digitais_ano, fisicos_ano, horas_estudo, horas_entretenimento):
    limpar_terminal()
    titulo()
    print(f'Agora vamos trazer algumas estimativas e curiosidades a partir dos seus dados!\n')
    leitura_ano = digitais_ano + fisicos_ano
    leitura_cinco_anos = leitura_ano * 5
    print(f'{nome}, você leu {leitura_ano} livros no último ano.')
    
    print(f'Se continuar nesse ritmo você vai ter lido {leitura_cinco_anos} livros a mais daqui a 5 anos.')
    estudo_ano = int(horas_estudo) * 52
    entretenimento_ano = int(horas_entretenimento) * 52
    print(f'{nome}, em 1 ano você consome em média {estudo_ano} horas em livros para estudar e consome {entretenimento_ano} para seu entretenimento.')
    input('Aperte enter para continuar.')
    return leitura_ano

def regiao_comparacao(nome, cidade, regiao, media_regiao, leitura_ano):
    limpar_terminal()
    titulo()
    print(f'{leitura_ano} livros no total.')
    porcentagem_camparacao = (leitura_ano / media_regiao) * 100
    porcentagem_camparacao = round(porcentagem_camparacao)
    if porcentagem_camparacao > 150:
        print(f'Isso representa {porcentagem_camparacao}% a mais do que a média de livros lidos na região {regiao} da sua cidade {cidade}: {media_regiao}.')
        print(f'Parabéns, {nome}! Você esta acima da média, continue assim.')
    elif porcentagem_camparacao < 70:
        print(f'Isso representa {porcentagem_camparacao}% da média de livros lidos na região {regiao} da sua cidade {cidade}: {media_regiao}.')
        print(f'{nome}, leia mais. A média anual dos brasileiros é considerada baixa.')
    else:
        print(f'Isso representa {porcentagem_camparacao}% da média de livros lidos na região {regiao} da sua cidade {cidade}: {media_regiao}.')
        print(f'Você está perto da média. Considere ler mais, {nome}.')
    input('Aperte enter para continuar.')

def dados_sociedade(nome, sexo, idade):
    limpar_terminal()
    titulo()
    print(f'{nome}, aqui vão mais dados:')
    
    if idade < 11:  # Pesquisa 'Retratos da leitura no Brasil' de 2016 realizado pelo Instituto Pró-Livro
        print('Você está na terceira faixa etária que mais lê. 67% das crianças com 10 ou menos são leitores.')
    elif 10 < idade <= 14:
        print('Você está na faixa etária que mais lê. 84% das pessoas entre 11 e 14 são leitores.')
    elif 14 < idade < 18:
        print('Você está na segunda faixa etária que mais lê. 75% das pessoas entre 14 e 17 são leitores.')
    elif 17 < idade < 41:
        print('Metade das pessoas na sua faixa etária (18 até 40) são leitores no Brasil.')
    elif 40 < idade < 71:
        print('Menos da metade das pessoas da sua faixa etária (40 até 70) são leitores.')
    else:
        print('Apenas 27% das pessoas da sua faixa etaria (+70) são leitores no país.')

    if sexo == 'feminino': # Também da pesquisa Retratos da leitura no Brasil, mas de 2024
        print('As mulheres costumam ler mais do que os homens no Brasil.')
        print('Você faz parte de 49% das mulheres do país. Cerca de 50,4 milhões de leitoras.')
    else:
        print('Os homens costumam ler menos do que as mulheres no Brasil.')
        print('Você faz parte de 44% dos homens do país. Cerca de 42,9 milhões de leitores.')
    input('Aperte enter para continuar')

def vantagens_disvantagens(preferencia):
    limpar_terminal()
    if preferencia == '1':
        print('Aqui estão algumas vantagens e desvantagens da sua preferência de leitura (Livro físico):')
        print('𝐕𝐚𝐧𝐭𝐚𝐠𝐞𝐧𝐬:')
        print('1. Experiência Sensorial: Sentir o cheiro e virar as páginas do livro trazem uma melhor experiência.')
        print('2. Colecionar: Ter uma estante de livros a seu dispor é útil, além de uma boa decoração.')
        print('3. Objeto social: Pode levar para qualquer lugar, sem precisar de uma bateria ou internet. E ainda é uma ótima opção de presente.\n')
        print('𝐃𝐞𝐬𝐯𝐚𝐧𝐭𝐚𝐠𝐞𝐧𝐬:')
        print('1. Peso e tamanho: Uma bolsa fica muito pesada com muitos livros, dependendo do tamanho pode não caber tudo.')
        print('2. Impacto na natureza: Quantas árvores cairam para se obter uma estante cheia de livros?')
        print('3. Preço: Os livros físicos são mais caros do que os digitais.')
    else: 
        print('Aqui estão algumas vantagens e desvantagens da sua preferência de leitura (Livro digital):')
        print('𝐕𝐚𝐧𝐭𝐚𝐠𝐞𝐧𝐬')
        print('1. Praticidade: É muito mais fácil acessar seus livros todos em um só lugar.')
        print('2. Pouco espaço: Você só precisa de um aparelho para ler, não é pesado e é pequeno.')
        print('3. Facilidade na compra: É possivel começar a ler qualquer livro agora, sem precisar encomendar ou ir para uma loja, além de um preço melhor.\n')
        print('𝐃𝐞𝐬𝐯𝐚𝐧𝐭𝐚𝐠𝐞𝐧𝐬')
        print('1. Estante vazia: Não é possivel colecionar ou ver os livros sem seu aparelho ligado.')
        print('2. Cansaço visual: Muitas horas na tela podem preudicar sua visão.')
        print('3. Bateria e wi-fi: Os livros digitais precisam de um aparelho carregado e conctado à internet.')


    
def titulo():
    print('🇷​​​​​ 🇪​​​​​ 🇦​​​​​ 🇩​​​​​ 🇮​​​​​ 🇳​​​​​ 🇬​​​​​    🇭​​​​​ 🇦​​​​​ 🇧​​​​​ 🇮​​​​​​​​​​ 🇹​​​​​ 🇸​​​​​')

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    limpar_terminal()
    inicio()
if __name__ == '__main__':
    main()  
