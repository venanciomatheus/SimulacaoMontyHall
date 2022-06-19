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