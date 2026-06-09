# importação de funções
from menu import mostrar_menu
from conversoes import decimal_para_binario
from conversoes import binario_para_decimal
from conversoes import decimal_para_octal
from conversoes import octal_para_decimal
from conversoes import decimal_para_hexadecimal
from conversoes import hexadecimal_para_decimal
from conversoes import binario_para_octal
from conversoes import octal_para_binario
from conversoes import binario_para_hexadecimal
from conversoes import hexadecimal_para_binario
from conversoes import octal_para_hexadecimal
from conversoes import hexadecimal_para_octal


while True:
    mostrar_menu()

    # Bloco para tratativa de erro caso o usuario coloque letras
    try:
        opcao = int(input('|' ' Opção: ' ) )
    except ValueError:
        print('|' ' Opção Invalida\n| Digite apenas numeros, dentre as opções abaixo ')

        continue

    # Estrutura switch para o menu
    match opcao:

        case 1:
            decimal_para_binario()

        case 2:
            binario_para_decimal()

        case 3:
            decimal_para_octal()

        case 4:
            octal_para_decimal()

        case 5:
            decimal_para_hexadecimal()

        case 6:
            hexadecimal_para_decimal()

        case 7:
            binario_para_octal()

        case 8:
            octal_para_binario()

        case 9:
            binario_para_hexadecimal()

        case 10:
            hexadecimal_para_binario()

        case 11:
            octal_para_hexadecimal()

        case 12:
            hexadecimal_para_octal()

        # Caso o usuario escolha sair, encerra o programa
        case 0:
            print('Encerrado')
            break

        # Tratativa de erro, caso o usuario digite um valor que não esteja dentre as opçoes
        case _:
            print('|' ' Opção ' + str(opcao) + ' é invalida\n' + 'Escolha um valor entre 0 e 12 assim como mostra o Menu abaixo')

