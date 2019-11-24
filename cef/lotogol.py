#!/usr/bin/python3.7
# -*- coding: utf-8
"""
 MegaLotto
 Versão 2.0.0A+ - Novembro 2019

 Este programa gera apostas para as loterias da Caixa Econômica Federal listadas abaixo. Para gerar este script foram utilizados
 dados obtidos no site da Caixa Econômica Federal. Qualquer dúvida sobre a utilização deste script ou para relatar possíveis
 bugs favor entrar em contato via e-mail

 ATENÇÃO! Este script não garante que o apostador ganhará algum prêmio e Eu me isento de qualquer responsabilidade ou dano físico e
 financeiro que este programa possa causar ao usuário.

 Autor: Dalilo Sérgio Gomes Rosas
 serggom@yahoo.com.br
 São Paulo/SP - Brazil


 Built by Jetbrains Pycharm Community - https://www.jetbrains.com/pycharm/
 Thank you Jetbrains for your support.

 Licença MIT
"""

import os
import time
import locale
import random

# Formato da moeda e região BR
locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

# Lotogol
# Dados obtidos do endereço: http://loterias.caixa.gov.br/wps/portal/loterias/landing/lotogol


def lotogol():
    lot = 'Lotogol'
    print(f'\033[1;32m Loteria escolhida:\033[0;0m {lot} ')
    print('\033[1;31m ATENÇÃO!\033[0;0m Nesta modalidade de aposta o computador escolherá o resultado dos '
          'jogos para você..')
    clube = ['0', '1', '2', '3', '+']

    ap = 0
    while ap < 1 or ap > 4 or ap == 3:
        try:
            ap = int(input(' Por favor, digite a quantidade de apostas iguais 1, 2 ou 4:  '))
        except ValueError:
            print('\033[1;31m ERRO!\033[m Opção inválida, por favor tente novamente... ')
    while True:
        try:
            pa = float(input(' Por favor, informe o valor da aposta única R$ '))
            break
        except ValueError:
            print('\033[1;31m ERRO!\033[m Opção inválida. Por favor, você precisa informar o valor da aposta '
                  'única em R$  ')

    print('\n Jogo 1')
    print('\033[1;32m time 1:\033[0;0m ' + clube[random.randrange(len(clube))])
    print('\033[1;32m time 2:\033[0;0m ' + clube[random.randrange(len(clube))])
    print('\n Jogo 2')
    print('\033[1;32m time 1:\033[0;0m ' + clube[random.randrange(len(clube))])
    print('\033[1;32m time 2:\033[0;0m ' + clube[random.randrange(len(clube))])
    print('\n Jogo 3')
    print('\033[1;32m time 1:\033[0;0m ' + clube[random.randrange(len(clube))])
    print('\033[1;32m time 2:\033[0;0m ' + clube[random.randrange(len(clube))])
    print('\n Jogo 4')
    print('\033[1;32m time 1:\033[0;0m ' + clube[random.randrange(len(clube))])
    print('\033[1;32m time 2:\033[0;0m ' + clube[random.randrange(len(clube))])
    print('\n Jogo 5')
    print('\033[1;32m time 1:\033[0;0m ' + clube[random.randrange(len(clube))])
    print('\033[1;32m time 2:\033[0;0m ' + clube[random.randrange(len(clube))])
    if ap == 1:

        print(f'\n\033[1;36m Você está apostando na loteria:\033[0;0m {lot}')
        print(f'\033[1;36m Quantidade de aposta igual:\033[0;0m {ap}')
        print('\n A aposta escolhida corresponde a: 1 jogo')
        print(' Total a pagar R$ ', locale.currency((1 * pa), grouping=True, symbol=None))
    elif ap == 2:
        print(f'\n\033[1;36m Você está apostando na loteria:\033[0;0m {lot}')
        print(f'\033[1;36m Quantidade de apostas iguais:\033[0;0m {ap}')
        print('\n A aposta escolhida corresponde a: 2 jogos')
        print(' Total a pagar R$ ', locale.currency((2 * pa), grouping=True, symbol=None))
    elif ap == 4:
        print(f'\n\033[1;36m Você está apostando na loteria:\033[0;0m {lot}')
        print(f'\033[1;36m Quantidade de apostas iguais:\033[0;0m {ap}')
        print('\n A aposta escolhida corresponde a: 4 jogos')
        print(' Total a pagar R$ ', locale.currency((4 * pa), grouping=True, symbol=None))

# Inicio nova aposta Lotogol

    pergunta = str(input(' Deseja continuar apostando na loteria Dia de Sorte S/N? ')).upper()

    while pergunta not in ('S', 'N'):
        try:
            pergunta = str(input('\033[1;31m ERRO!\033[m Por favor, você precisa digitar S ou N! ')).upper()
        except ValueError:
            print('')
    while pergunta == 'S':
        lotogol()
        break
    else:
        print(f' Obrigado por apostar na Loteria {lot} ')

        pergunta = str(input(' Deseja apostar em outra loteria S/N? ')).strip().upper()[0]

        if pergunta == 'S':
            from cef.lib.interface import menu
            menu()
        else:
            print(' Obrigado, volte sempre! ')
            print('\n')
            print('\033[0;32m[-=-=-=-=-=-=- Por favor, aguarde o encerramento.-=-=-=-=-=-=-=-=-]\033[0;0m')
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
