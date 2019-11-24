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
from random import shuffle


# Formato da moeda e região BR
locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

# Quina
# Dados obtidos do endereço: http://loterias.caixa.gov.br/wps/portal/loterias/landing/quina/


total = ''
jogos = ''
five = ''


def quina():
    global total, jogos, five
    lot = 'Quina'
    print(f'\n\033[1;32m Loteria escolhida:\033[0;0m {lot} ')
    dezenas = 0
    while dezenas < 5 or dezenas > 15:
        try:
            dezenas = int(input(' Por favor, digite a quantidade de dezenas que você deseja apostar entre 5 e 15:  '))
        except ValueError:
            print('\033[1;31m ERRO!\033[m Opção inválida, por favor tente novamente... ')
    while True:
        try:
            pa = float(input(' Por favor, informe o valor da aposta única R$ '))
            break
        except ValueError:
            print('\033[1;31m ERRO!\033[m Opção inválida. Por favor, você precisa informar o valor da aposta '
                  'única em R$  ')

    # Aposta com 5 dezenas

    if dezenas == 5:
        def five():
            cinco = list(range(1, 80))
            numbers = []
            for n in range(5):
                shuffle(cinco)
                quin = cinco.pop()
                numbers.append(quin)
            numbers.sort()
            return numbers

        for i in range(5):
            jogos = 1
            total = jogos * pa

    # Aposta com 6 dezenas

    if dezenas == 6:
        def five():
            cinco = list(range(1, 80))
            numbers = []
            for n in range(6):
                shuffle(cinco)
                quin = cinco.pop()
                numbers.append(quin)
            numbers.sort()
            return numbers

        for i in range(6):
            jogos = 6
            total = jogos * pa

    # Aposta com 7 dezenas

    if dezenas == 7:
        def five():
            cinco = list(range(1, 80))
            numbers = []
            for n in range(7):
                shuffle(cinco)
                quin = cinco.pop()
                numbers.append(quin)
            numbers.sort()
            return numbers

        for i in range(7):
            jogos = 21
            total = jogos * pa

    # Aposta com 8 dezenas

    if dezenas == 8:
        def five():
            cinco = list(range(1, 80))
            numbers = []
            for n in range(8):
                shuffle(cinco)
                quin = cinco.pop()
                numbers.append(quin)
            numbers.sort()
            return numbers

        for i in range(8):
            jogos = 56
            total = jogos * pa

    # Aposta com 9 dezenas

    if dezenas == 9:
        def five():
            cinco = list(range(1, 80))
            numbers = []
            for n in range(9):
                shuffle(cinco)
                quin = cinco.pop()
                numbers.append(quin)
            numbers.sort()
            return numbers

        for i in range(9):
            jogos = 126
            total = jogos * pa

    # Aposta com 10 dezenas

    if dezenas == 10:
        def five():
            cinco = list(range(1, 80))
            numbers = []
            for n in range(10):
                shuffle(cinco)
                quin = cinco.pop()
                numbers.append(quin)
            numbers.sort()
            return numbers

        for i in range(10):
            jogos = 252
            total = jogos * pa

    # Aposta com 11 dezenas

    if dezenas == 11:
        def five():
            cinco = list(range(1, 80))
            numbers = []
            for n in range(11):
                shuffle(cinco)
                quin = cinco.pop()
                numbers.append(quin)
            numbers.sort()
            return numbers

        for i in range(11):
            jogos = 462
            total = jogos * pa

    # Aposta com 12 dezenas

    if dezenas == 12:
        def five():
            cinco = list(range(1, 80))
            numbers = []
            for n in range(12):
                shuffle(cinco)
                quin = cinco.pop()
                numbers.append(quin)
            numbers.sort()
            return numbers

        for i in range(12):
            jogos = 792
            total = jogos * pa

    # Aposta com 13 dezenas

    if dezenas == 13:
        def five():
            cinco = list(range(1, 80))
            numbers = []
            for n in range(13):
                shuffle(cinco)
                quin = cinco.pop()
                numbers.append(quin)
            numbers.sort()
            return numbers

        for i in range(13):
            jogos = 1287
            total = jogos * pa

    # Aposta com 14 dezenas

    if dezenas == 14:
        def five():
            cinco = list(range(1, 80))
            numbers = []
            for n in range(14):
                shuffle(cinco)
                quin = cinco.pop()
                numbers.append(quin)
            numbers.sort()
            return numbers

        for i in range(14):
            jogos = 2002
            total = jogos * pa

    # Aposta com 15 dezenas

    if dezenas == 15:
        def five():
            cinco = list(range(1, 80))
            numbers = []
            for n in range(15):
                shuffle(cinco)
                quin = cinco.pop()
                numbers.append(quin)
            numbers.sort()
            return numbers

        for i in range(15):
            jogos = 3003
            total = jogos * pa

    print(f'\n\033[1;36m Você apostou na loteria: \033[0;0m{lot}')
    print(f'\033[1;36m Você está apostando com:\033[0;0m {dezenas} dezenas')
    print('\n\033[1;36m Palpite: \033[0;0m ', ' - '.join(map(str, five())))
    print(f'\n A aposta escolhida corresponde a: {jogos} jogo(s)')
    if jogos > 1:
        print(f'\n A aposta escolhida corresponde a: {jogos:0,} jogos'.replace(',', '.'))
    if jogos < 2:
        print(f'\n A aposta escolhida corresponde a: {jogos:0,} jogo'.replace(',', '.'))
    print(' Total a pagar R$ ', locale.currency(total, grouping=True, symbol=None))

# Inicio nova aposta Quina

    pergunta = str(input(' Deseja continuar apostando na loteria Dia de Sorte S/N? ')).upper()

    while pergunta not in ('S', 'N'):
        try:
            pergunta = str(input('\033[1;31m ERRO!\033[m Por favor, você precisa digitar S ou N! ')).upper()
        except ValueError:
            print('')
    while pergunta == 'S':
        quina()
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
