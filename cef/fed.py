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

# Loteria Federal
# Dados obtidos do endereço; http://loterias.caixa.gov.br/wps/portal/loterias/landing/federal


def federal():
    lot = 'Loteria Federal'
    print(f'\033[1;32m Loteria escolhida:\033[0;0m {lot} ')

    def lotofederal():
        fed = list(range(0, 99999))
        numbers = []
        for i in range(1):
            shuffle(fed)
            lf = fed.pop()
            numbers.append(lf)
        numbers.sort()
        return numbers

    print(f'\n\033[1;36m Você apostou na loteria: \033[0;0m{lot}')
    print('\n\033[1;36m Palpite: \033[0;0m ', ' - '.join(map(str, lotofederal())))
    print('\n')

# Inicio nova aposta Loteria Federal

    pergunta = str(input(f' Deseja continuar apostando na loteria {lot} S/N? ')).upper()

    while pergunta not in ('S', 'N'):
        try:
            pergunta = str(input('\033[1;31m ERRO!\033[m Por favor, você precisa digitar S ou N! ')).upper()
        except ValueError:
            print('')
    while pergunta == 'S':
        federal()
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
