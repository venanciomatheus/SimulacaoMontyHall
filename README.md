Esse programa pretende simular o Problema de Monty Hall:
Considerando que em um programa de tevisão o participante (jogador)
sempre precisa escolher abrir 1 de 3 portas, de modo que:
1. Em apenas 1 das portas existe um prêmio (nas outras 2 não existe prêmio)
2. O apresentador conhece o que tem atrás de cada porta 
3. O apresentador sempre abrirá uma das portas sem prêmio após
o jogador ter tomado sua decisão incial
4. O apresentador sempre dará a oportunidade do jogador trocar a
porta escolhida após uma das portas sem o prêmio ter sido aberta
------------------------------------------------------------------------------------
Apesar da melhor escolha do jogador (entre trocar ou não a decisão incial)
não ser tão trivial, matematicamente sempre será vantajo para o jogador
trocar a porta escolhida incialmente. Sabe-se que a probabilidade do jogador
ganhar alterando a porta é de 66,66%, caso ele não realize a troca a
probabilidade de ganhar é de apenas 33,33%.
------------------------------------------------------------------------------------
Assim, esse programa pretende utilizar uma sequência de testes forçados
para verificar se a probabilidade do jogador ganhar realmente será algo
próximo de 66,66% caso o jogador sempre altere a porta inicial. Vale destacar
que quanto maior a quantidade de testes (qnt) que o usuário escolher,
consequentemente o teste de simulação ficará mais preciso.
------------------------------------------------------------------------------------
    Programa: SimulacaoMontyHall.v001.19062022

        Desenvolvido em: 19/06/2022

            Por: Matheus Venancio