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

# Lotofácil
# Dados obtidos do endereço: http://loterias.caixa.gov.br/wps/portal/loterias/landing/lotofacil/


total = ''
jogos = ''
lotfacil = ''


def lotofacil():
    global total, jogos, lotfacil
    lot = 'Lotofácil'
    print(f'\033[1;32m Loteria escolhida:\033[0;0m {lot} ')
    dezenas = 0
    while dezenas < 15 or dezenas > 18:
        try:
            dezenas = int(input(' Por favor, digite a quantidade de dezenas que você deseja apostar entre 15 e 18:  '))
        except ValueError:
            print('\033[1;31m ERRO!\033[m Opção inválida, por favor tente novamente... ')
    while True:
        try:
            pa = float(input(' Por favor, informe o valor da aposta única R$ '))
            break
        except ValueError:
            print('\033[1;31m ERRO!\033[m Opção inválida. Por favor, você precisa informar o valor da aposta '
                  'única em R$  ')

    # Aposta com 15 dezenas

    if dezenas == 15:
        def lotfacil():
            lfacil = list(range(1, 25))
            numbers = []
            for n in range(15):
                shuffle(lfacil)
                lf = lfacil.pop()
                numbers.append(lf)
            numbers.sort()
            return numbers

        for i in range(15):
            jogos = 1
            total = jogos * pa

    # Aposta com 16 dezenas

    if dezenas == 16:
        def lotfacil():
            lfacil = list(range(1, 25))
            numbers = []
            for n in range(16):
                shuffle(lfacil)
                lf = lfacil.pop()
                numbers.append(lf)
            numbers.sort()
            return numbers

        for i in range(16):
            jogos = 16
            total = jogos * pa

    # Aposta com 17 dezenas

    if dezenas == 17:
        def lotfacil():
            lfacil = list(range(1, 25))
            numbers = []
            for n in range(17):
                shuffle(lfacil)
                lf = lfacil.pop()
                numbers.append(lf)
            numbers.sort()
            return numbers

        for i in range(17):
            jogos = 136
            total = jogos * pa

    # Aposta com 18 dezenas

    if dezenas == 18:
        def lotfacil():
            lfacil = list(range(1, 25))
            numbers = []
            for n in range(18):
                shuffle(lfacil)
                lf = lfacil.pop()
                numbers.append(lf)
            numbers.sort()
            return numbers

        for i in range(18):
            jogos = 816
            total = jogos * pa

    print(f'\n\033[1;36m Você apostou na loteria: \033[0;0m{lot}')
    print(f'\033[1;36m Você está apostando com:\033[0;0m {dezenas} dezenas')
    print('\n\033[1;36m Palpite: \033[0;0m ', ' - '.join(map(str, lotfacil())))
    if jogos > 1:
        print(f'\n A aposta escolhida corresponde a: {jogos:0,} jogos'.replace(',', '.'))
    if jogos < 2:
        print(f'\n A aposta escolhida corresponde a: {jogos:0,} jogo'.replace(',', '.'))
    print(' Total a pagar R$ ', locale.currency(total, grouping=True, symbol=None))

# Inicio nova aposta Lotofácil

    pergunta = str(input(' Deseja continuar apostando na loteria Dia de Sorte S/N? ')).upper()

    while pergunta not in ('S', 'N'):
        try:
            pergunta = str(input('\033[1;31m ERRO!\033[m Por favor, você precisa digitar S ou N! ')).upper()
        except ValueError:
            print('')
    while pergunta == 'S':
        lotofacil()
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
