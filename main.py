# importação de funções
from menu import mostrar_menu
from conversoes import decimal_para_binario
from conversoes import binario_para_decimal


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
            print('Conversão de Decimal para Octal')

        case 4:
            print('Conversão de Octal para Decimal')

        case 5:
            print('Conversão de Decimal para hexadecimal')

        case 6:
            print('Conversão de Hexadecimal para Decimal')

        case 7:
            print('Conversão de Binario para Octal')

        case 8:
            print('Conversão de Octal para Binario ')

        case 9:
            print('Conversão de Binario para Hexadecimal')

        case 10:
            print('Conversão de Hexadecimal para Binario')

        case 11:
            print('Conversão de Octal para Hexadecimal')

        case 12:
            print('Conversão Hexadecimal para Octal')

        # Caso o usuario escolha sair, encerra o programa
        case 0:
            print('Encerrado')
            break

        # Tratativa de erro, caso o usuario digite um valor que não esteja dentre as opçoes
        case _:
            print('|' ' Opção ' + str(opcao) + ' é invalida\n' + 'Escolha um valor entre 0 e 12 assim como mostra o Menu abaixo')
