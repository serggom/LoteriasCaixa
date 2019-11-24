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
import random


# Formato da moeda e região BR
locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

# Dia de Sorte
# Dados obtidos do endereço: http://loterias.caixa.gov.br/wps/portal/loterias/landing/diadesorte

total = ''
jogos = ''
dsorte = ''


def diasorte():
    global total, jogos, dsorte
    lot = 'Dia de Sorte'
    print(f'\033[1;32m Loteria escolhida:\033[0;0m {lot} ')
    dezenas = 0
    while dezenas < 7 or dezenas > 15:
        try:
            dezenas = int(input(' Por favor, digite a quantidade de dezenas que você deseja apostar entre 7 e 15:  '))
        except ValueError:
            print("\033[1;31m ERRO!\033[m Opção inválida, por favor tente novamente... ")
    while True:
        try:
            pa = float(input(' Por favor, informe o valor da aposta única R$ '))
            break
        except ValueError:
            print('\033[1;31m ERRO!\033[m Opção inválida. Por favor, você precisa informar o valor da aposta '
                  'única em R$  ')

    # Aposta com 7 dezenas

    if dezenas == 7:
        def dsorte():
            disorte = list(range(1, 31))
            numbers = []
            for n in range(7):
                shuffle(disorte)
                ds = disorte.pop()
                numbers.append(ds)
            numbers.sort()
            return numbers

        for i in range(7):
            jogos = 1
            total = jogos * pa

    # Aposta com 8 dezenas

    if dezenas == 8:
        def dsorte():
            disorte = list(range(1, 31))
            numbers = []
            for n in range(8):
                shuffle(disorte)
                ds = disorte.pop()
                numbers.append(ds)
            numbers.sort()
            return numbers

        for i in range(8):
            jogos = 8
            total = jogos * pa

    # Aposta com 9 dezenas

    if dezenas == 9:
        def dsorte():
            disorte = list(range(1, 31))
            numbers = []
            for n in range(9):
                shuffle(disorte)
                ds = disorte.pop()
                numbers.append(ds)
            numbers.sort()
            return numbers

        for i in range(9):
            jogos = 36
            total = jogos * pa

    # Aposta com 10 dezenas

    if dezenas == 10:
        def dsorte():
            disorte = list(range(1, 31))
            numbers = []
            for n in range(10):
                shuffle(disorte)
                ds = disorte.pop()
                numbers.append(ds)
            numbers.sort()
            return numbers

        for i in range(10):
            jogos = 120
            total = jogos * pa

    # Aposta com 11 dezenas

    if dezenas == 11:
        def dsorte():
            disorte = list(range(1, 31))
            numbers = []
            for n in range(11):
                shuffle(disorte)
                ds = disorte.pop()
                numbers.append(ds)
            numbers.sort()
            return numbers

        for i in range(11):
            jogos = 330
            total = jogos * pa

    # Aposta com 12 dezenas

    if dezenas == 12:
        def dsorte():
            disorte = list(range(1, 31))
            numbers = []
            for n in range(12):
                shuffle(disorte)
                ds = disorte.pop()
                numbers.append(ds)
            numbers.sort()
            return numbers

        for i in range(12):
            jogos = 792
            total = jogos * pa

    # Aposta com 13 dezenas

    if dezenas == 13:
        def dsorte():
            disorte = list(range(1, 31))
            numbers = []
            for n in range(13):
                shuffle(disorte)
                ds = disorte.pop()
                numbers.append(ds)
            numbers.sort()
            return numbers

        for i in range(13):
            jogos = 1716
            total = jogos * pa

    # Aposta com 14 dezenas

    if dezenas == 14:
        def dsorte():
            disorte = list(range(1, 31))
            numbers = []
            for n in range(14):
                shuffle(disorte)
                ds = disorte.pop()
                numbers.append(ds)
            numbers.sort()
            return numbers

        for i in range(14):
            jogos = 3432
            total = jogos * pa

    # Aposta com 15 dezenas

    if dezenas == 15:
        def dsorte():
            disorte = list(range(1, 31))
            numbers = []
            for n in range(15):
                shuffle(disorte)
                ds = disorte.pop()
                numbers.append(ds)
            numbers.sort()
            return numbers

        for i in range(15):
            jogos = 6435
            total = jogos * pa

# Mês da sorte
    mes = ['Janeiro',
           'Fevereiro',
           'Março',
           'Abril',
           'Maio',
           'Junho',
           'Julho',
           'Agosto',
           'Setembro',
           'Outubro',
           'Novembro',
           'Dezembro']

    print(f'\n\033[1;36m Você apostou na loteria: \033[0;0m{lot}')
    print(f'\033[1;36m Você está apostando com:\033[0;0m {dezenas} dezenas')
    print('\n\033[1;36m Palpite: \033[0;0m ', ' - '.join(map(str, dsorte())))
    print('\033[1;34m O mês da sorte é:\033[0;0m ' + mes[random.randrange(len(mes))])
    if jogos > 1:
        print(f'\n A aposta escolhida corresponde a: {jogos:0,} jogos'.replace(',', '.'))
    elif jogos < 2:
        print(f'\n A aposta escolhida corresponde a: {jogos:0,} jogo'.replace(',', '.'))
    print(' Total a pagar R$ ', locale.currency(total, grouping=True, symbol=None))

# Inicio nova aposta Dia de Sorte

    pergunta = str(input(' Deseja continuar apostando na loteria Dia de Sorte S/N? ')).upper()

    while pergunta not in ('S', 'N'):
        try:
            pergunta = str(input('\033[1;31m ERRO!\033[m Por favor, você precisa digitar S ou N! ')).upper()
        except ValueError:
            print('')
    while pergunta == 'S':
        diasorte()
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
