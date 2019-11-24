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

# Timemania
# Dados obtidos do endereço: http://loterias.caixa.gov.br/wps/portal/loterias/landing/timemania/

total = ''
jogos = ''
timania = ''


def timemania():
    global total, jogos, timania
    lot = 'Time Mania'
    print(f'\n\033[1;32m Loteria escolhida:\033[0;0m {lot} ')
    print('\n\033[1;31m ATENÇÃO!\033[0;0m Nessa loteria o computador escolherá 10 dezenas para você!')

    while True:
        try:
            pa = float(input(' Por favor, informe o valor da aposta única R$ '))
            break
        except ValueError:
            print('\033[1;31m ERRO!\033[m Opção inválida. Por favor, você precisa informar o valor da aposta '
                  'única em R$  ')

    def timania():
        timeMania = list(range(1, 80))
        numbers = []
        for n in range(10):
            shuffle(timeMania)
            ms = timeMania.pop()
            numbers.append(ms)
        numbers.sort()
        return numbers
    for i in range(10):
        jogos = 1
        total = jogos * pa

    print('\n\033[1;36m Palpite:\033[0;0m ', ' - '.join(map(str, timania())))
    equipe = ['ABC - RN',
              'América - MG',
              'América - RJ',
              'América - RN',
              'Americano - RJ',
              'Atlético - GO',
              'Atlético - MG',
              'Atlético - PR',
              'Avai - SC',
              'Bahia - BA',
              'Bangu - RJ',
              'Barueri - SP',
              'Botafogo - PB',
              'Botafogo - RJ',
              'Bragantino - SP',
              'Brasiliense - DF',
              'Ceará - CE',
              'Corinthians - SP',
              'Coritiba - PR',
              'CRB - AL',
              'Criciúma - SC',
              'Cruzeiro - MG',
              'CSA - AL',
              'Desportiva - ES',
              'Figueirense - SC',
              'Flamengo - RJ',
              'Fluminense - RJ',
              'Fortaleza - CE',
              'Goiás - GO',
              'Grêmio - RS',
              'Guarani - SP',
              'Inter de Limeira - SP',
              'Internacional - PA',
              'Ipatinga - MG',
              'Ituano - SP',
              'Ji-Paraná - RO',
              'Joinvile - SC',
              'Juventude - RS',
              'Juventus - SP',
              'Londrina - PR',
              'Marília - SP',
              'Mixto - MT',
              'Moto time - MA',
              'Nacional - AM',
              'Náutico - PE',
              'Olaria - RJ',
              'Operário - MS',
              'Palmas - TO',
              'Palmeiras - SP',
              'Paraná - PR',
              'Paulista - SP',
              'Paysandú - PA',
              'Ponte Preta - SP',
              'Portuguesa de Desportos - SP',
              'Remo - PA',
              'Rio Branco - AC',
              'Rio Branco - ES',
              'River - PI',
              'Roraima - RR',
              'Sampaio Corrêa - MA',
              'Santa Cruz - PE',
              'Santo André - SP',
              'Santos Futebol time - SP',
              'São Caetano - SP',
              'São Paulo Futebol Clube - SP',
              'São Raimundo - AM',
              'Sergipe - SE',
              'Sport Recife - PE',
              'Treze - PB',
              'Tuna Luso - PA',
              'Uberlândia - MG',
              'União Barbarense - SP',
              'União São João - SP',
              'Vasco da Gama - RJ',
              'Vila Nova - GO',
              'Villa Nova - MG',
              'Vitória - BA',
              'XV De Piracicaba - SP',
              'Ypiranga - AP']

    dezenas = 10
    print(f'\n\033[1;36m Você apostou na loteria: \033[0;0m{lot}')
    print(f'\033[1;36m Você está apostando com:\033[0;0m {dezenas} dezenas')
    print('\n\033[1;32m Time do Coração:\033[0;0m ' + equipe[random.randrange(len(equipe))])
    print(f'\n A aposta escolhida corresponde a: {jogos} jogo contendo {dezenas} ')
    print(' Total a pagar R$ ', locale.currency(total, grouping=True, symbol=None))

# Inicio nova aposta Timemania

    pergunta = str(input(' Deseja continuar apostando na loteria Dia de Sorte S/N? ')).upper()

    while pergunta not in ('S', 'N'):
        try:
            pergunta = str(input('\033[1;31m ERRO!\033[m Por favor, você precisa digitar S ou N! ')).upper()
        except ValueError:
            print('')
    while pergunta == 'S':
        timemania()
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
