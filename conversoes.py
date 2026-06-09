def decimal_para_binario():
    num = int(input('|\n' + '| Informe um número decimal para ser convertido para binario: '))
    print('|' + '-' * 70 + '|')


    # Declaração de Variaveis
    resto = []
    passos = []
    passo_a_passo = 1
    conta_passos = ''
    resultado = ''

    # Logica da conversão
    while num > 0:

        resto_atual = num % 2
        quociente = num // 2

        mensagem_passo = ' Passo %d: %d / 2 -> Quociente: %d, Resto: %d' % (passo_a_passo, num, quociente, resto_atual)
        print('|' + mensagem_passo.ljust(70) + '|')

        resto.append(num % 2)
        passos.append(passo_a_passo)

        num = quociente

        passo_a_passo += 1

    resto.reverse()
    passos.reverse()

    for passo in passos:
        conta_passos = conta_passos + str(passo) + ','

    mensagem_Ultipasso = ' Passo %d: Junte os valores dos restos dos passos %s' % (passo_a_passo, conta_passos)
    print('|' + mensagem_Ultipasso.ljust(70) + '|' )

    for digito in resto:
        resultado = resultado + str(digito)

    print('|' + ' Resultado: ' + resultado.ljust(58) + '|')
    print('|' + '-' * 70 + '|\n')

def binario_para_decimal():
    while True:
        binario = input('|\n' + '| Informe um numero binario para ser convertido para decimal: ')
        print('|' + '-' * 70 + '|')

        letra = False
        # Voltar para o menu inicial
        if binario.lower() == 'sair':
            return
        # tratativa de erro, caso o usuario apenas de enter
        if binario == '':
            print('Entrada invalida! digite apenas um numero binario ou sair para voltar ao menu inicial')
            continue

        # tratativa de erro, caso o usuario digite letras
        for digito in binario:
            if digito.isalpha():
                letra = True
        if letra:
            print('Invalido, não digite letras. \nDigite apenas um numero binario ou sair para voltar ao menu inicial.')
            continue

        valido = True

        # Tratativa de erro, caso o usuario digite um valor sem ser um numero binario 0 ou 1
        for digito in binario:
            if digito != '0' and digito != '1':
                valido = False
        if not valido:
            print('Invalido, numero digitado não é um numero binario \nDigite apenas um numero binario ou sair para voltar ao menu inicial.')
            continue

        break

    # declaração de variavel
    exponente = len(binario) -1
    resultado = 0
    passo_a_passo = 1
    valores = []
    passos = []
    conta_valores = ''
    conta_passos = ''

    # Logica da conversão
    for digito in binario:
        digito = int(digito)
        valor = digito * 2**exponente
        print(' Passo %d: %d x 2**%d = %d'  % (passo_a_passo, digito, exponente, valor))
        resultado = resultado + valor
        exponente = exponente - 1

        valores.append(valor)
        passos.append(passo_a_passo)

        passo_a_passo += 1

    for passo in passos:
        conta_passos = conta_passos + str(passo) + ','

    for valor in valores:
        conta_valores = conta_valores + str(valor) + '+'


    print(' Passo %d: Some os valores dos resultados dos passos %s' % (passo_a_passo, conta_passos))
    print('|' + ' Resultado: %s = %d' % (conta_valores, resultado) + '|' )
    print('|' + '-' * 70 + '|\n')



