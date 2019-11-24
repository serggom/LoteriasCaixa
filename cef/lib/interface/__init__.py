from cef.dsrt import diasorte
from cef.dsen import duplasena
from cef.fed import federal
from cef.lofa import lotofacil
from cef.lotogol import lotogol
from cef.ltmania import lotomania
from cef.megas import megasena
from cef.cinco import quina
from cef.time import timemania

from cef.saida import sair


def menu():
    print('''
      1 - Dia de Sorte
      2 - Dupla Sena
      3 - Loteria Federal
      4 - Lotofácil 
      5 - Lotogol   
      6 - Lotomania
      7 - Mega-Sena
      8 - Quina
      9 - Timemania
      0 - Sair''')

    while True:
        try:
            option = int(input('\n Opção:\> '))
            if option == 1:
                diasorte()
                break
            elif option == 2:
                duplasena()
                break
            elif option == 3:
                federal()
                break
            elif option == 4:
                lotofacil()
                break
            elif option == 5:
                lotogol()
                break
            elif option == 6:
                lotomania()
                break
            elif option == 7:
                megasena()
                break
            elif option == 8:
                quina()
                break
            elif option == 9:
                timemania()
                break
            elif option == 0:
                sair()
                break
            else:
                print('\n\033[1;31m Atenção!\033[0;0m A opção escolhida não consta no menu. Por favor, '
                      'tente novamente!\033[0;0m')
                menu()
                break
        except ValueError:
            print('\033[1;31m Erro!\033[0;0m Por favor, você precisa escolher uma opção válida!')
        except KeyboardInterrupt:
            print(' Interrompido pelo usuário... Retornando ao menu principal! ')

            menu()
