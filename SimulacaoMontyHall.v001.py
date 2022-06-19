from random import randint
from emoji import emojize
from time import sleep
def titulo(tit='ESCOLHA O TÍTULO', tam=100):
    '''
    → Desenvolvido por Matheus Venancio
    :param tit: mensagem de título
    :param tam: valor da centralização
    :return: título formatado
    '''
    print('=' * tam)
    print(tit.center(tam))
    print('=' * tam)


def apenasInt(qualquer):
    '''
    → Desenvolvido por Matheus Venancio
    :param qualquer: recebe qualquer string
    :return: retorna apenas números inteiros
    '''
    while True:
        try:
            qc = input(qualquer)
        except KeyboardInterrupt:
            print('\n\033[31mERRO: O usuário interrompeu o programa de forma forçada.\033[m')
            exit()
        else:
            if qc.isnumeric():
                return int(qc)
            print('\033[31mERRO: Você não digitou um número inteiro\033[m')


def apenas1e2(qualquer):
    '''
    → Desenvolvido por Matheus Venancio
    :param qualquer: recebe qualquer string
    :return: retorna apenas números inteiros 1 ou 2
    '''
    while True:
        try:
            qc = input(qualquer)
        except KeyboardInterrupt:
            print('\n\033[31mERRO: O usuário interrompeu o programa de forma forçada.\033[m')
            exit()
        else:
            if qc.isnumeric():
                qc = int(qc)
                if qc == 1 or qc == 2:
                    return qc
                print('\033[31mERRO: Opção inválida. Escolha [1] ou [2]\033[31m')
                continue
            print('\033[31mERRO: Você não digitou um número inteiro\033[m')
# Definindo emojis
IV_carros = emojize(' :money_bag:') * 4
IV_cabras = emojize(':goat: ') * 4
porta = emojize(':door:')
alerta = emojize(':warning:')
lapis = emojize(':pencil:')
balao = emojize(':speech_balloon:')
# Lógica do Problema de Monty Hall
'''
Esse programa pretende simular o Problema de Monty Hall:
> Considerando que em um programa de tevisão o participante (jogador)
sempre precisa escolher abrir 1 de 3 portas, de modo que:
    1. Em apenas 1 das portas existe um prêmio (nas outras 2 não existe prêmio)
    2. O apresentador conhece o que tem atrás de cada porta 
    3. O apresentador sempre abrirá uma das portas sem prêmio após
    o jogador ter tomado sua decisão incial
    4. O apresentador sempre dará a oportunidade do jogador trocar a
    porta escolhida após uma das portas sem o prêmio ter sido aberta
------------------------------------------------------------------------------------
> Apesar da melhor escolha do jogador (entre trocar ou não a decisão incial)
não ser tão trivial, matematicamente sempre será vantajo para o jogador
trocar a porta escolhida incialmente. Sabe-se que a probabilidade do jogador
ganhar alterando a porta é de 66,66%, caso ele não realize a troca a
probabilidade de ganhar é de apenas 33,33%.
------------------------------------------------------------------------------------
> Assim, esse programa pretende utilizar uma sequência de testes forçados
para verificar se a probabilidade do jogador ganhar realmente será algo
próximo de 66,66% caso o jogador sempre altere a porta inicial. Vale destacar
que quanto maior a quantidade de testes (qnt) que o usuário escolher,
consequentemente o teste de simulação ficará mais preciso.
------------------------------------------------------------------------------------
'''
# Programa em loop para entregar a oportunidade de continuar novos testes
while True:
    titulo(f'\033[1;33m{IV_carros} PROBLEMA DE MONTY HALL {IV_cabras}\033[m')
    # Possibilita uma exlicação do Problema de Monty Hall
    ler_contexto = apenas1e2('\033[92mVocê gostaria de ler a lógica do Problema de Monty Hall?\n'
                             'Digite [1] para SIM ou [2] para NÃO\n'
                             '>> \033[m')
    if ler_contexto == 1:
        sleep(1)
        # Texto explicando a lógica do Problema de Monty Hall
        print('''\033[mEsse programa pretende simular o Problema de Monty Hall:
> Considerando que em um programa de tevisão o participante (jogador)
sempre precisa escolher abrir 1 de 3 portas, de modo que:
    1. Em apenas 1 das portas existe um prêmio (nas outras 2 não existe prêmio)
    2. O apresentador conhece o que tem atrás de cada porta 
    3. O apresentador sempre abrirá uma das portas sem prêmio após
    o jogador ter tomado sua decisão incial
    4. O apresentador sempre dará a oportunidade do jogador trocar a
    porta escolhida após uma das portas sem o prêmio ter sido aberta
------------------------------------------------------------------------------------
> Apesar da melhor escolha do jogador (entre trocar ou não a decisão incial)
não ser tão trivial, matematicamente sempre será vantajo para o jogador
trocar a porta escolhida incialmente. Sabe-se que a probabilidade do jogador
ganhar alterando a porta é de 66,66%, caso ele não realize a troca a
probabilidade de ganhar é de apenas 33,33%.
------------------------------------------------------------------------------------
> Assim, esse programa pretende utilizar uma sequência de testes forçados
para verificar se a probabilidade do jogador ganhar realmente será algo
próximo de 66,66% caso o jogador sempre altere a porta inicial. Vale destacar
que quanto maior a quantidade de testes (qnt) que o usuário escolher,
consequentemente o teste de simulação ficará mais preciso.
------------------------------------------------------------------------------------\033[m''')
    # Definir a quantidade de testes
    while True:
        qnt = apenasInt('Digite a quantidade de testes: ')
        if qnt >= 3:
            if qnt <= 100:
                print(f'\033[36mEu NÃO RECOMENDO que você utilize menos de 100 testes.'
                      f' Mas vamos lá...{alerta}\033[m')
            break
        print(f'\033[91mVocê está pedindo apenas {qnt} teste(s), por favor'
              f' utilize pelo menos 3 testes\033[m')
    sleep(1)
    print(f'\033[32mOk, o programa irá considerar {qnt} testes.')
    sleep(0.5)
    # Quantidade de escolhas por porta
    p1 = p2 = p3 = 0
    # Quantidade de portas premiadas por porta
    pp1 = pp2 = pp3 = 0
    # Contador de escolhas vencedoras
    g1 = g2 = 0 # g1 equivale a escolha inicial e g2 equivale a escolha secundária
    # Pergunta se o jogador vai querer trocar de porta
    while True:
        resp = apenas1e2('\033[mDurante a simulação você quer SEMPRE trocar a porta escolhida INICALMENTE?\n'
                         f'Essa escolha servirá para todos os {qnt} jogos...\n'
                         f'Digite [1] para SIM ou [2] para NÃO:\n>> \033[m')
    # Escolha aleatória
    # Tratamento de erro por ocasião do usuário não esperar os cálculos
        try:
            print(f'Estou calculando...{balao}{lapis}')
            for c in range(0, qnt):
                escolha_inicial = randint(1, 3) # Representação de PORTA 1, PORTA 2, PORTA 3
                # Definindo a porta premiada
                premio = randint(1, 3) # Representação de PORTA 1, PORTA 2, PORTA 3
                if resp == 1:
                # Definindo a troca de porta
                # Considerando que o jogador inicialmente ESTAVA com a porta premiada
                    if escolha_inicial == premio:
                        while True:
                            escolha_secundaria = randint(1, 3)
                            if escolha_secundaria != escolha_inicial:
                                break
                    # Considerando que o jogador NÃO ESTAVA inicialmente com a porta premiada
                    else:
                        # Perceba que nesse caso o jogador é "obrigado" a trocar para a porta premiada
                        escolha_secundaria = premio
                # Contador de portas premiadas por porta
                if premio == 1:
                    pp1 += 1
                elif premio == 2:
                    pp2 += 1
                else:
                    pp3 += 1
                # Contador de escolhas por porta
                if escolha_inicial == 1:
                    p1 += 1
                elif escolha_inicial == 2:
                    p2 += 1
                else:
                    p3 += 1
                # Verificar se o jogador ganhou
                if escolha_inicial == premio:
                    g1 += 1
                if resp == 1 and escolha_secundaria == premio:
                    g2 += 1
        except KeyboardInterrupt:
            print('\n\033[31mERRO: O usuário não esperou os cálculos e interrompeu'
                  ' oprograma de forma forçada.\033[m')
            exit()
        else:
            sleep(0.75)
            print(f'\033[94mConsiderando {qnt} jogos, eu escolhi:\n'
                  f'{porta} Porta 1 [{p1/qnt:.2%}]: {p1}x\n'
                  f'{porta} Porta 2 [{p2/qnt:.2%}]: {p2}x\n'
                  f'{porta} Porta 3 [{p3/qnt:.2%}]: {p3}x\033[m')
            print('-' * 100)
            sleep(0.75)
            print(f'\033[93mConsiderando {qnt} jogos, a proporção de portas premiadas foi:\n'
                  f'{porta} Porta 1 [{pp1/qnt:.2%}]: {pp1}x\n'
                  f'{porta} Porta 2 [{pp2/qnt:.2%}]: {pp2}x\n'
                  f'{porta} Porta 3 [{pp3/qnt:.2%}]: {pp3}x\033[m')
            print('-' * 100)
            sleep(0.75)
            print(f'\033[95mConsiderando que NÃO troquei minha escolha nos {qnt} jogos,'
                  f' os jogos vencedores totalizaram:\n'
                  f'{g1} jogos = {g1/qnt:.2%} dos jogos.\033[m')
            print('-' * 100)
            if resp == 1:
                sleep(0.75)
                print(f'\033[96mConsiderando que TROQUEI de escolha nos {qnt} jogos,'
                      f' os jogos vencedores totalizaram:\n'
                      f'{g2} jogos = {g2/qnt:.2%} dos jogos.\033[m')
                print('-' * 100)
            continuar = apenas1e2(f'\033[mDigite [1] para ENCERRAR o programa ou [2] para'
                                  f' CONTINUAR novos testes.\n'
                                  f'>> ')
            if continuar == 1:
                sleep(.5)
                print('Encerrando o programa... ')
                sleep(.5)
                titulo('>>> PROGRAMA ENCERRADO, Volte sempre! <<<')
                break


