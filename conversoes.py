# Case 1
def decimal_para_binario():
    while True:
        entrada = input('|\n' + '| Informe um número decimal para ser convertido para binario: ')
        print('|' + '-' * 70 + '|')

        letras = False

        # Voltar para o menu inical
        if entrada.lower() == 'sair':
            return

        # Tratativa de erro, caso o usuario de entrada vazia
        if entrada == '':
            print('|' + ' Invalido.'.ljust(70) + '|' '\n| Digite um numero ou sair para voltar ao menu inicial.'.ljust(73) + '|')
            print('|' + '-' * 70 + '|')
            continue

        # tratativa de erro caso o usuario digite letras
        for letra in entrada:
            if letra.isalpha():
                letras = True
        if letras:
            print('| Invalido, não digite letras'.ljust(71) + '|\n| Digite apenas um numero inteiro ou sair para voltar ao menu inicial.'.ljust(73) + '|')
            print('|' + '-' * 70 + '|')
            continue

        # tratativa de erro, caso o usuario digite numero invalido
        try:
            num = int(entrada)
            break
        except ValueError:
            print('| Invalido.'.ljust(71) + '|\n| Digite apenas numeros inteiros ou sair para voltar ao menu inicial.'.ljust(73) + '|')
            print('|' + '-' * 70 + '|')
            continue

        break

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

    print('|' + '-' * 70 + '|')
    print('|' + ' Resultado: ' + resultado.ljust(58) + '|')
    print('|' + '-' * 70 + '|\n')

# Case 2
def binario_para_decimal():
    while True:
        binario = input('|\n' + '| Informe um numero binario para ser convertido para decimal: ')
        print('|' + '-' * 70 + '|')

        letra = False
        # Voltar para o menu inicial
        if binario.lower() == 'sair':
            return
        # Tratativa de erro, caso o usuario de entrada vazia
        if binario == '':
            print('| invalido!'.ljust(71) + '|' '\n| Digite apenas um numero binario ou sair para voltar ao menu inicial'.ljust(73) + '|')
            print('|' + '-' * 70 + '|')
            continue

        # tratativa de erro, caso o usuario digite letras
        for digito in binario:
            if digito.isalpha():
                letra = True
        if letra:
            print('| Invalido, não digite letras.'.ljust(71) + '|' '\n| Digite apenas um numero binario ou sair para voltar ao menu inicial.'.ljust(73) + '|')
            print('|' + '-' * 70 + '|')
            continue

        valido = True

        # Tratativa de erro, caso o usuario digite um valor sem ser um numero binario 0 ou 1
        for digito in binario:
            if digito != '0' and digito != '1':
                valido = False
        if not valido:
            print('| Invalido, numero digitado não é um numero binario.'.ljust(71) + '|' + '\n| Digite apenas um numero binario ou sair para voltar ao menu inicial.'.ljust(72) + '|')
            print('|' + '-' * 70 + '|')
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
        mensagem_passo = (' Passo %d: %d x 2**%d = %d'  % (passo_a_passo, digito, exponente, valor))
        print('|' + mensagem_passo.ljust(70) + '|' )
        resultado = resultado + valor
        exponente = exponente - 1

        valores.append(valor)
        passos.append(passo_a_passo)

        passo_a_passo += 1

    for passo in passos:
        conta_passos = conta_passos + str(passo) + ','

    for valor in valores:
        conta_valores = conta_valores + str(valor) + '+'


    mensagem_Ultpassos = (' Passo %d: Some os valores dos resultados dos passos %s' % (passo_a_passo, conta_passos))
    print('|' + mensagem_Ultpassos.ljust(70) + '|')
    mensagem_resultado = (' Resultado: %s = %d' % (conta_valores, resultado))
    print('|' + '-' * 70 + '|')
    print('|' + mensagem_resultado.ljust(70) + '|' )
    print('|' + '-' * 70 + '|\n')

# Case 3
def decimal_para_octal():
    while True:
        entrada = input('|\n' + '| Informe um numero decimal para ser convertido para octal: ')
        print('|' + '-' * 70 + '|')

        letras = False

        # tratativa de erro, caso o usuario de entrada vazia
        if entrada == '':
            print('| Invalido!'.ljust(71) + '|\n| Digite um numero inteiro ou sair para voltar ao menu inicial'.ljust(73) + '|')
            print('|' + '-' * 70 + '|')
            continue

        # tratativa de erro caso o usuario digite letras
        for letra in entrada:
            if letra.isalpha():
                letras = True
        if letras:
            print('| Invalido! não digite letras'.ljust(71) + '|\n| Digite apenas um numero inteiro ou sair para voltar ao menu inicial '.ljust(73) + '|')
            print('|' + '-' * 70 + '|')
            continue


        try:
            num = int(entrada)
            break
        except ValueError:
            print('| Invalido!'.ljust(71) + '|\n| Digite apenas numeros inteiros ou sair para voltar ao menu inicial'.ljust(73) + '|')
            print('|' + '-' * 70 + '|')
            continue

        break

    # declaração das variaveis
    resto = []
    passos = []
    passo_a_passo = 1
    conta_passos = ''
    resultado = ''

    # logica da conversão, na base 8
    while num > 0:

        resto_atual = num % 8
        quociente = num // 8

        mensagem_passo = ' Passo %d: %d / 8 -> Quociente: %d, Resto: %d' % (passo_a_passo, num, quociente, resto_atual)
        print('|' + mensagem_passo.ljust(70) + '|')

        resto.append(num % 8)
        passos.append(passo_a_passo)

        num = quociente

        passo_a_passo += 1

    resto.reverse()
    passos.reverse()

    for passo in passos:
        conta_passos = conta_passos + str(passo) + ','

    mensagem_Ultpasso = ' Passo %d: Junte os valores dos restos dos passos %s' % (passo_a_passo, conta_passos)
    print('|' + mensagem_Ultpasso.ljust(70) + '|')

    for digito in resto:
        resultado = resultado + str(digito)

    print('|' + '-' * 70 + '|')
    print('| Resultado: ' + resultado.ljust(58) + '|')
    print('|' + '-' * 70 + '|\n')

# case 4
def octal_para_decimal():
    while True:
        octal = input('|\n| Informe um numero Octal para ser convertido para decimal: ')
        print('|' + '-' * 70 + '|')

        letras = False

        if octal.lower() == 'sair':
            return

        if octal == '':
            print('| Invalido!'.ljust(71) + '|\n| Digite apenas um numero octal ou sair para voltar ao menu inical'.ljust(73) + '|')
            print('|' + '-' * 70 + '|')
            continue

        for digito in octal:
            if digito.isalpha():
                letras = True

        if letras:
            print('| invalido! não digite letras'.ljust(71) + '|\n| Digite apenas um numero octal ou sair para voltar ao menu inical'.ljust(73) + '|')
            print('|' + '-' * 70 + '|')
            continue

        try:
            num = int(octal)
            break
        except ValueError:
            print('| Invalido!'.ljust(71) + '|\n| Digite apenas numeros octal ou sair para voltar ao menu inicial'.ljust(73) + '|')
            print('|' + '-' * 70 + '|')
            continue

        break

    # declaração das variaveis
    exponente = len(octal) - 1
    resultado = 0
    passo_a_passo = 1
    valores = []
    passos = []
    conta_passos = ''
    conta_valores = ''

    # logica da conversão, na base 8
    for digito in octal:
        digito = int(digito)
        valor = digito * 8**exponente
        mensagem_passo = (' Passo %d: %d x 2**%d = %d'  % (passo_a_passo, digito, exponente, valor))
        print('|' + mensagem_passo.ljust(70) + '|')
        resultado = resultado + valor
        exponente = exponente - 1

        valores.append(valor)
        passos.append(passo_a_passo)

        passo_a_passo += 1

    for passo in passos:
        conta_passos = conta_passos + str(passo) + ','

    for valor in valores:
        conta_valores = conta_valores + str(valor) + '+'

    mensagem_Ultpasso = (' Passo %d: Some os valores dos resultados dos passos %s' % (passo_a_passo, conta_passos))
    print('|' + mensagem_Ultpasso.ljust(70) + '|')
    mensagem_Resultado = (' Resultado: %s = %d' % (conta_valores, resultado))
    print('|' + mensagem_Resultado.ljust(70) + '|')
    print('|' + '-' * 70 + '|')

# case 5
def decimal_para_hexadecimal():
    while True:
        decimal = input('|\n' + '| Informe um numero decimal para ser convertido para hexadecimal: ')
        print('|' + '-' * 70 + '|')

        letras = False

        # tratativa de erro, caso o usuario de entrada vazia
        if decimal == '':
            print('| Invalido!'.ljust(71) + '|\n| Digite um numero inteiro ou sair para voltar ao menu inicial'.ljust(
                73) + '|')
            print('|' + '-' * 70 + '|')
            continue

        # tratativa de erro caso o usuario digite letras
        for letra in decimal:
            if letra.isalpha():
                letras = True
        if letras:
            print('| Invalido! não digite letras'.ljust(
                71) + '|\n| Digite apenas um numero inteiro ou sair para voltar ao menu inicial '.ljust(73) + '|')
            print('|' + '-' * 70 + '|')
            continue

        try:
            num = int(decimal)
            break
        except ValueError:
            print('| Invalido!'.ljust(
                71) + '|\n| Digite apenas numeros inteiros ou sair para voltar ao menu inicial'.ljust(73) + '|')
            print('|' + '-' * 70 + '|')
            continue

        break

    # Declaração de Variaveis
    resto = []
    passos = []
    passo_a_passo = 1
    conta_passos = ''
    resultado = ''

    # Logica da conversão
    while num > 0:

        resto_atual = num % 16
        quociente = num // 16

        mensagem_passo = ' Passo %d: %d / 16 -> Quociente: %d, Resto: %d' % (passo_a_passo, num, quociente, resto_atual)
        print('|' + mensagem_passo.ljust(70) + '|')

        if resto_atual == 10:
            resto.append('A')
        elif resto_atual == 11:
            resto.append('B')
        elif resto_atual == 12:
            resto.append('C')
        elif resto_atual == 13:
            resto.append('D')
        elif resto_atual == 14:
            resto.append('E')
        elif resto_atual == 15:
            resto.append('F')
        else:
            resto.append(resto_atual)

        passos.append(passo_a_passo)

        num = quociente

        passo_a_passo += 1

    resto.reverse()
    passos.reverse()

    for passo in passos:
        conta_passos = conta_passos + str(passo) + ','

    if len(passos) > 1:
        mensagem_Ultipasso = ' Passo %d: Junte os valores dos restos dos passos %s' % (passo_a_passo, conta_passos)
        print('|' + mensagem_Ultipasso.ljust(70) + '|' )

    for digito in resto:
        resultado = resultado + str(digito)

    print('|' + '-' * 70 + '|')
    print('|' + ' Resultado: ' + resultado.ljust(58) + '|')
    print('|' + '-' * 70 + '|\n')

# case 6
def hexadecimal_para_decimal():
    while True:
        hexadecimal = input('|\n' + '| Informe um numero hexadecimal para ser convertido para decimal: ')
        print('|' + '-' * 70 + '|')

        letra = False
        # Voltar para o menu inicial
        if hexadecimal.lower() == 'sair':
            return
        # Tratativa de erro, caso o usuario de entrada vazia
        if hexadecimal == '':
            print('| invalido!'.ljust(71) + '|' '\n| Digite apenas um numero hexadecimal ou sair para voltar ao menu inicial'.ljust(73) + '|')
            print('|' + '-' * 70 + '|')
            continue

        hexadecimal = hexadecimal.upper()

        valido = True

        for digito in hexadecimal:
            if digito not in '0123456789ABCDEF':
                valido = False

        if not valido:
            print('| invalido!'.ljust(71) + '|\n| Digite apenas valores hexadecimais: 0-9 e A-F.'.ljust(73) + '|\n| ou digite sair para voltar ao menu inicial'.ljust(73) + '|')
            print('|' + '-' * 70 + '|')
            continue

        break

    # declaração das variaveis
    exponente = len(hexadecimal) - 1
    resultado = 0
    passo_a_passo = 1
    valores = []
    passos = []
    conta_passos = ''
    conta_valores = ''

    # logica da conversão, na base 16
    for digito in hexadecimal:

        if digito == 'A':
            digito_convertido =10
        elif digito == 'B':
            digito_convertido =11
        elif digito == 'C':
            digito_convertido =12
        elif digito == 'D':
            digito_convertido =13
        elif digito == 'E':
            digito_convertido =14
        elif digito == 'F':
            digito_convertido =15
        else:
            digito_convertido =int(digito)

        valor = digito_convertido * 16**exponente

        if len(hexadecimal) == 1:
            mensagem_passo = ' Passo %d: %s corresponde ao valor decimal %d' % (passo_a_passo, digito, valor)
        else:
            mensagem_passo = ' Passo %d: %s x 16**%d = %d' % (passo_a_passo, digito, exponente, valor)

        print('|' + mensagem_passo.ljust(70) + '|')

        resultado = resultado + valor
        exponente = exponente - 1

        valores.append(valor)
        passos.append(passo_a_passo)

        passo_a_passo += 1

    for passo in passos:
        conta_passos = conta_passos + str(passo) + ','

    for valor in valores:
        conta_valores = conta_valores + str(valor) + '+'

    if len(passos) > 1:
        mensagem_Ultpasso = (' Passo %d: Some os valores dos resultados dos passos %s' % (passo_a_passo, conta_passos))
        print('|' + mensagem_Ultpasso.ljust(70) + '|')

    if len(passos) > 1:
        print('|' + '-' * 70 + '|')
        mensagem_Resultado = (' Resultado: %s = %d' % (conta_valores, resultado))
        print('|' + mensagem_Resultado.ljust(70) + '|')
    else:
        print('|' + '-' * 70 + '|')
        mensagem_Resultado = (' Resultado: %d' % (resultado))
        print('|' + mensagem_Resultado.ljust(70) + '|')

    print('|' + '-' * 70 + '|')

# case 7
def binario_para_octal():
    while True:
        binario = input('|\n' + '| Informe um numero binario para ser convertido para octal: ')
        print('|' + '-' * 70 + '|')

        letra = False
        # Voltar para o menu inicial
        if binario.lower() == 'sair':
            return
        # Tratativa de erro, caso o usuario de entrada vazia
        if binario == '':
            print('| invalido!'.ljust(71) + '|' '\n| Digite apenas um numero binario ou sair para voltar ao menu inicial'.ljust(73) + '|')
            print('|' + '-' * 70 + '|')
            continue

        # tratativa de erro, caso o usuario digite letras
        for digito in binario:
            if digito.isalpha():
                letra = True
        if letra:
            print('| Invalido, não digite letras.'.ljust(71) + '|' '\n| Digite apenas um numero binario ou sair para voltar ao menu inicial.'.ljust(73) + '|')
            print('|' + '-' * 70 + '|')
            continue

        valido = True

        # Tratativa de erro, caso o usuario digite um valor sem ser um numero binario 0 ou 1
        for digito in binario:
            if digito != '0' and digito != '1':
                valido = False
        if not valido:
            print('| Invalido, numero digitado não é um numero binario.'.ljust(71) + '|' + '\n| Digite apenas um numero binario ou sair para voltar ao menu inicial.'.ljust(72) + '|')
            print('|' + '-' * 70 + '|')
            continue

        break

    # aqui adiciona zeros a esquerda, caso digite um tamanho q não seja multiplo de 3
    while len(binario) % 3 != 0:
        binario = '0' + binario

    grupos = []

    # aqui separa em grupos de 3
    for i in range (0, len(binario), 3):
        grupos.append(binario[i:i+3])

    resultado = ''
    passo_a_passo = 1


    # para cada grupo, vai calcular o valor decimal daquele grupo de 3 bits
    for grupo in grupos:
        valor = 0
        exponente = 2
        conta = ''

        for digito in grupo:
            calculo = int(digito)* 2**exponente
            valor = valor + calculo

            conta = conta + '%s x 2**%d + ' % (digito, exponente)

            exponente = exponente - 1

        mensagem_passo = (' Passo %d: %s = %d, que é igual a %d' % (passo_a_passo, conta, valor, valor))
        print('|' + mensagem_passo.ljust(70) + '|')

        resultado = resultado + str(valor)
        passo_a_passo += 1

    conta_passos = ''

    for passo in range(1, passo_a_passo):
        conta_passos = conta_passos + str(passo) + ','

    if passo_a_passo > 2:
        mensagem_Ultpasso = (' Passo %d: Junte os valores octais nos passos %s' % (passo_a_passo, conta_passos))
        print('|' + mensagem_Ultpasso.ljust(70) + '|')

    print('|' + '-' * 70 + '|')
    mensagem_Resultado = (' Resultado: %s ' % (resultado))
    print('|' + mensagem_Resultado.ljust(70) + '|')
    print('|' + '-' * 70 + '|')

# case 8
def octal_para_binario():
    while True:
        octal = input('|\n| Informe um numero Octal para ser convertido para binario: ')
        print('|' + '-' * 70 + '|')

        letras = False

        if octal.lower() == 'sair':
            return

        # tratativa, caso o usario, informe vazio
        if octal == '':
            print('| Invalido!'.ljust(71) + '|\n| Digite apenas um numero octal ou sair para voltar ao menu inicial'.ljust(73) + '|')
            print('|' + '-' * 70 + '|')
            continue

        # tratativa de erro, caso o usuario digite letras
        for digito in octal:
            if digito.isalpha():
                letras = True

        if letras:
            print('| Invalido! Não digite letras.'.ljust(71) + '|\n| Digite apenas um numero octal ou sair para voltar ao menu inicial'.ljust(73) + '|')
            print('|' + '-' * 70 + '|')
            continue

        # tratativa para caracteres especiais
        try:
            int(octal)
        except ValueError:
            print('| Invalido!'.ljust(71) + '|\n| Digite apenas numeros octais ou sair para voltar ao menu inicial'.ljust(73) + '|')
            print('|' + '-' * 70 + '|')
            continue

        # tratativa para numeros fora da base octal
        valido = True

        for digito in octal:
            if digito not in '01234567':
                valido = False

        if not valido:
            print('| Invalido! Numero digitado não é octal.'.ljust(71) + '|\n| Digite apenas numeros de 0 a 7 ou sair para voltar ao menu.'.ljust(73) + '|')
            print('|' + '-' * 70 + '|')
            continue

        break

    # declaração das variáveis
    resultado = ''
    passo_a_passo = 1

    # para cada dígito octal
    for digito in octal:
        if digito == '0':
            binario = '000'
            conta = '0x2**2 + 0x2**1 + 0x2**0'
        elif digito == '1':
            binario = '001'
            conta = '0x2**2 + 0x2**1 + 1x2**0'
        elif digito == '2':
            binario = '010'
            conta = '0x2**2 + 1x2**1 + 0x2**0'
        elif digito == '3':
            binario = '011'
            conta = '0x2**2 + 1x2**1 + 1x2**0'
        elif digito == '4':
            binario = '100'
            conta = '1x2**2 + 0x2**1 + 0x2**0'
        elif digito == '5':
            binario = '101'
            conta = '1x2**2 + 0x2**1 + 1x2**0'
        elif digito == '6':
            binario = '110'
            conta = '1x2**2 + 1x2**1 + 0x2**0'
        elif digito == '7':
            binario = '111'
            conta = '1x2**2 + 1x2**1 + 1x2**0'

        mensagem_passo = (' Passo %d: %s = %s = %s' % (passo_a_passo, digito, conta, binario))
        print('|' + mensagem_passo.ljust(70) + '|')

        resultado = resultado + binario
        passo_a_passo += 1

    # monta a lista de passos
    conta_passos = ''

    for passo in range(1, passo_a_passo):
        conta_passos = conta_passos + str(passo) + ','

    # mostra o último passo apenas se houver mais de um dígito
    if passo_a_passo > 2:
        mensagem_Ultpasso = (' Passo %d: Junte os grupos binarios encontrados nos passos %s' % (passo_a_passo, conta_passos))
        print('|' + mensagem_Ultpasso.ljust(70) + '|')

    print('|' + '-' * 70 + '|')
    mensagem_Resultado = ' Resultado: %s' % resultado
    print('|' + mensagem_Resultado.ljust(70) + '|')
    print('|' + '-' * 70 + '|')

# case 9
def binario_para_hexadecimal():
    while True:
        binario = input('|\n' + '| Informe um numero binario para ser convertido para hexadecimal: ')
        print('|' + '-' * 70 + '|')

        letra = False

        # voltar para o menu inicial
        if binario.lower() == 'sair':
            return

        # tratativa de erro, caso o usuario deixe vazio
        if binario == '':
            print('| Invalido!'.ljust(71) + '|\n| Digite apenas um numero binario ou sair para voltar ao menu inicial'.ljust(73) + '|')
            print('|' + '-' * 70 + '|')
            continue

        # tratativa de erro, caso o usuario digite letras
        for digito in binario:
            if digito.isalpha():
                letra = True

        if letra:
            print('| Invalido! Não digite letras.'.ljust(71) + '|\n| Digite apenas um numero binario ou sair para voltar ao menu inicial.'.ljust(73) + '|')
            print('|' + '-' * 70 + '|')
            continue

        valido = True

        # tratativa de erro, caso o usuario digite algo diferente de 0 ou 1
        for digito in binario:
            if digito != '0' and digito != '1':
                valido = False

        if not valido:
            print('| Invalido! Numero digitado não é um numero binario.'.ljust(71) + '|\n| Digite apenas um numero binario ou sair para voltar ao menu inicial.'.ljust(73) + '|')
            print('|' + '-' * 70 + '|')
            continue

        break

    # aqui adiciona zeros a esquerda, caso o usuario digite um tamanho q não seja multiplo de 4
    while len(binario) % 4 != 0:
        binario = '0' + binario

    grupos = []

    # aqui separa em grupos de 4
    for i in range(0, len(binario), 4):
        grupos.append(binario[i:i + 4])

    resultado = ''
    passo_a_passo = 1

    # para cada grupo, vai calcular o valor decimal daquele grupo de 4 bits
    for grupo in grupos:
        valor = 0
        exponente = 3
        conta = ''

        for digito in grupo:
            calculo = int(digito) * 2 ** exponente
            valor = valor + calculo

            conta = conta + '%s x 2**%d + ' % (digito, exponente)

            exponente = exponente - 1

        if valor == 10:
            hexadecimal = 'A'
        elif valor == 11:
            hexadecimal = 'B'
        elif valor == 12:
            hexadecimal = 'C'
        elif valor == 13:
            hexadecimal = 'D'
        elif valor == 14:
            hexadecimal = 'E'
        elif valor == 15:
            hexadecimal = 'F'
        else:
            hexadecimal = str(valor)

        mensagem_passo = (' Passo %d: %s = %d, que é igual a %s' % (passo_a_passo, conta, valor, hexadecimal))
        print('|' + mensagem_passo.ljust(70) + '|')

        resultado = resultado + hexadecimal
        passo_a_passo += 1

    # monta a lista de passos
    conta_passos = ''

    for passo in range(1, passo_a_passo):
        conta_passos = conta_passos + str(passo) + ','

    # mostra o último passo apenas se houver mais de um grupo
    if passo_a_passo > 2:
        mensagem_Ultpasso = (' Passo %d: Junte os valores hexadecimais encontrados nos passos %s' % (passo_a_passo, conta_passos))
        print('|' + mensagem_Ultpasso.ljust(70) + '|')

    print('|' + '-' * 70 + '|')
    mensagem_Resultado = (' Resultado: %s' % resultado)
    print('|' + mensagem_Resultado.ljust(70) + '|')
    print('|' + '-' * 70 + '|')

# case 10
def hexadecimal_para_binario():
    while True:
        hexadecimal = input('|\n' + '| Informe um numero hexadecimal para ser convertido para binario: ')
        print('|' + '-' * 70 + '|')

        letra = False
        # Voltar para o menu inicial
        if hexadecimal.lower() == 'sair':
            return
        # Tratativa de erro, caso o usuario de entrada vazia
        if hexadecimal == '':
            print('| invalido!'.ljust(71) + '|' '\n| Digite apenas um numero hexadecimal ou sair para voltar ao menu inicial'.ljust(73) + '|')
            print('|' + '-' * 70 + '|')
            continue

        hexadecimal = hexadecimal.upper()

        valido = True

        for digito in hexadecimal:
            if digito not in '0123456789ABCDEF':
                valido = False

        if not valido:
            print('| invalido!'.ljust(71) + '|\n| Digite apenas valores hexadecimais: 0-9 e A-F.'.ljust(73) + '|\n| ou digite sair para voltar ao menu inicial'.ljust(73) + '|')
            print('|' + '-' * 70 + '|')
            continue

        break

    # declaração das variáveis
    resultado = ''
    passo_a_passo = 1

    # para cada dígito hexadecimal
    for digito in hexadecimal:
        if digito == '0':
            binario = '0000'
            conta = '0x2**3 + 0x2**2 + 0x2**1 + 0x2**0'
        elif digito == '1':
            binario = '0001'
            conta = '0x2**3 + 0x2**2 + 0x2**1 + 1x2**0'
        elif digito == '2':
            binario = '0010'
            conta = '0x2**3 + 0x2**2 + 1x2**1 + 0x2**0'
        elif digito == '3':
            binario = '0011'
            conta = '0x2**3 + 0x2**2 + 1x2**1 + 1x2**0'
        elif digito == '4':
            binario = '0100'
            conta = '0x2**3 + 1x2**2 + 0x2**1 + 0x2**0'
        elif digito == '5':
            binario = '0101'
            conta = '0x2**3 + 1x2**2 + 0x2**1 + 1x2**0'
        elif digito == '6':
            binario = '0110'
            conta = '0x2**3 + 1x2**2 + 1x2**1 + 0x2**0'
        elif digito == '7':
            binario = '0111'
            conta = '0x2**3 + 1x2**2 + 1x2**1 + 1x2**0'
        elif digito == '8':
            binario = '1000'
            conta = '1x2**3 + 0x2**2 + 0x2**1 + 0x2**0'
        elif digito == '9':
            binario = '1001'
            conta = '1x2**3 + 0x2**2 + 0x2**1 + 1x2**0'
        elif digito == 'A':
            binario = '1010'
            conta = '1x2**3 + 0x2**2 + 1x2**1 + 0x2**0'
        elif digito == 'B':
            binario = '1011'
            conta = '1x2**3 + 0x2**2 + 1x2**1 + 1x2**0'
        elif digito == 'C':
            binario = '1100'
            conta = '1x2**3 + 1x2**2 + 0x2**1 + 0x2**0'
        elif digito == 'D':
            binario = '1101'
            conta = '1x2**3 + 1x2**2 + 0x2**1 + 1x2**0'
        elif digito == 'E':
            binario = '1110'
            conta = '1x2**3 + 1x2**2 + 1x2**1 + 0x2**0'
        elif digito == 'F':
            binario = '1111'
            conta = '1x2**3 + 1x2**2 + 1x2**1 + 1x2**0'

        mensagem_passo = (' Passo %d: %s = %s = %s' % (passo_a_passo, digito, conta, binario))
        print('|' + mensagem_passo.ljust(70) + '|')

        resultado = resultado + binario
        passo_a_passo += 1

    # monta a lista de passos
    conta_passos = ''

    for passo in range(1, passo_a_passo):
        conta_passos = conta_passos + str(passo) + ','

    # mostra o último passo apenas se houver mais de um dígito
    if passo_a_passo > 2:
        mensagem_Ultpasso = (' Passo %d: Junte os grupos binarios encontrados nos passos %s' % (passo_a_passo, conta_passos))
        print('|' + mensagem_Ultpasso.ljust(70) + '|')
    print('|' + '-' * 70 + '|')

    mensagem_Resultado = (' Resultado: %s' % resultado)
    print('|' + mensagem_Resultado.ljust(70) + '|')
    print('|' + '-' * 70 + '|')

# case 11
def octal_para_hexadecimal():
    while True:
        octal = input('|\n| Informe um numero Octal para ser convertido para hexadecimal: ')
        print('|' + '-' * 70 + '|')

        letras = False

        if octal.lower() == 'sair':
            return

        if octal == '':
            print('| Invalido!'.ljust(71) + '|\n| Digite apenas um numero octal ou sair para voltar ao menu inical'.ljust(73) + '|')
            print('|' + '-' * 70 + '|')
            continue

        for digito in octal:
            if digito.isalpha():
                letras = True

        if letras:
            print('| invalido! não digite letras'.ljust(71) + '|\n| Digite apenas um numero octal ou sair para voltar ao menu inical'.ljust(73) + '|')
            print('|' + '-' * 70 + '|')
            continue

        try:
            num = int(octal)
            break
        except ValueError:
            print('| Invalido!'.ljust(71) + '|\n| Digite apenas numeros octal ou sair para voltar ao menu inicial'.ljust(73) + '|')
            print('|' + '-' * 70 + '|')
            continue

        break

    # declaração das variáveis
    binario_completo = ''
    resultado = ''
    passo_a_passo = 1

    # converte cada digito octal para binario
    for digito in octal:

        if digito == '0':
            binario = '000'
            conta = '0x2**2 + 0x2**1 + 0x2**0'
        elif digito == '1':
            binario = '001'
            conta = '0x2**2 + 0x2**1 + 1x2**0'
        elif digito == '2':
            binario = '010'
            conta = '0x2**2 + 1x2**1 + 0x2**0'
        elif digito == '3':
            binario = '011'
            conta = '0x2**2 + 1x2**1 + 1x2**0'
        elif digito == '4':
            binario = '100'
            conta = '1x2**2 + 0x2**1 + 0x2**0'
        elif digito == '5':
            binario = '101'
            conta = '1x2**2 + 0x2**1 + 1x2**0'
        elif digito == '6':
            binario = '110'
            conta = '1x2**2 + 1x2**1 + 0x2**0'
        elif digito == '7':
            binario = '111'
            conta = '1x2**2 + 1x2**1 + 1x2**0'

        mensagem_passo = (' Passo %d: %s = %s = %s' % (passo_a_passo, digito, conta, binario))
        print('|' + mensagem_passo.ljust(70) + '|')

        binario_completo = binario_completo + binario
        passo_a_passo += 1

    # adiciona zeros a esquerda para formar grupos de 4
    while len(binario_completo) % 4 != 0:
        binario_completo = '0' + binario_completo

    grupos = []

    # separa em grupos de 4 bits
    for i in range(0, len(binario_completo), 4):
        grupos.append(binario_completo[i:i + 4])

    # converte cada grupo de 4 bits para hexadecimal
    for grupo in grupos:

        valor = 0
        exponente = 3
        conta = ''

        for digito in grupo:
            calculo = int(digito) * 2 ** exponente
            valor = valor + calculo

            conta = conta + '%s x 2**%d + ' % (digito, exponente)

            exponente = exponente - 1

        if valor == 10:
            hexadecimal = 'A'
        elif valor == 11:
            hexadecimal = 'B'
        elif valor == 12:
            hexadecimal = 'C'
        elif valor == 13:
            hexadecimal = 'D'
        elif valor == 14:
            hexadecimal = 'E'
        elif valor == 15:
            hexadecimal = 'F'
        else:
            hexadecimal = str(valor)

        mensagem_passo = (' Passo %d: %s = %d, que é igual a %s' % (passo_a_passo, conta, valor, hexadecimal))
        print('|' + mensagem_passo.ljust(70) + '|')

        resultado = resultado + hexadecimal
        passo_a_passo += 1

    conta_passos = ''

    for passo in range(1, passo_a_passo):
        conta_passos = conta_passos + str(passo) + ','

    if passo_a_passo > 2:
        mensagem_Ultpasso = (' Passo %d: Junte os valores hexadecimais encontrados nos passos %s' % (passo_a_passo,conta_passos))
        print('|' + mensagem_Ultpasso.ljust(70) + '|')

    print('|' + '-' * 70 + '|')
    mensagem_Resultado = (' Resultado: %s' % resultado)
    print('|' + mensagem_Resultado.ljust(70) + '|')
    print('|' + '-' * 70 + '|')

# case 12
def hexadecimal_para_octal():
    while True:
        hexadecimal = input('|\n' + '| Informe um numero hexadecimal para ser convertido para octal: ')
        print('|' + '-' * 70 + '|')

        # voltar para o menu inicial
        if hexadecimal.lower() == 'sair':
            return

        # tratativa de erro, caso o usuario deixe vazio
        if hexadecimal == '':
            print('| invalido!'.ljust(71) + '|\n| Digite apenas um numero hexadecimal ou sair para voltar ao menu inicial'.ljust(73) + '|')
            print('|' + '-' * 70 + '|')
            continue

        hexadecimal = hexadecimal.upper()

        valido = True

        for digito in hexadecimal:
            if digito not in '0123456789ABCDEF':
                valido = False

        if not valido:
            print('| invalido!'.ljust(71) + '|\n| Digite apenas valores hexadecimais: 0-9 e A-F.'.ljust(73) + '|\n| Ou digite sair para voltar ao menu inicial.'.ljust(73) + '|')
            print('|' + '-' * 70 + '|')
            continue

        break

    # declaração das variáveis
    binario_completo = ''
    resultado = ''
    passo_a_passo = 1

    # converte cada digito hexadecimal para binario
    for digito in hexadecimal:

        if digito == '0':
            binario = '0000'
            conta = '0x2**3 + 0x2**2 + 0x2**1 + 0x2**0'
        elif digito == '1':
            binario = '0001'
            conta = '0x2**3 + 0x2**2 + 0x2**1 + 1x2**0'
        elif digito == '2':
            binario = '0010'
            conta = '0x2**3 + 0x2**2 + 1x2**1 + 0x2**0'
        elif digito == '3':
            binario = '0011'
            conta = '0x2**3 + 0x2**2 + 1x2**1 + 1x2**0'
        elif digito == '4':
            binario = '0100'
            conta = '0x2**3 + 1x2**2 + 0x2**1 + 0x2**0'
        elif digito == '5':
            binario = '0101'
            conta = '0x2**3 + 1x2**2 + 0x2**1 + 1x2**0'
        elif digito == '6':
            binario = '0110'
            conta = '0x2**3 + 1x2**2 + 1x2**1 + 0x2**0'
        elif digito == '7':
            binario = '0111'
            conta = '0x2**3 + 1x2**2 + 1x2**1 + 1x2**0'
        elif digito == '8':
            binario = '1000'
            conta = '1x2**3 + 0x2**2 + 0x2**1 + 0x2**0'
        elif digito == '9':
            binario = '1001'
            conta = '1x2**3 + 0x2**2 + 0x2**1 + 1x2**0'
        elif digito == 'A':
            binario = '1010'
            conta = '1x2**3 + 0x2**2 + 1x2**1 + 0x2**0'
        elif digito == 'B':
            binario = '1011'
            conta = '1x2**3 + 0x2**2 + 1x2**1 + 1x2**0'
        elif digito == 'C':
            binario = '1100'
            conta = '1x2**3 + 1x2**2 + 0x2**1 + 0x2**0'
        elif digito == 'D':
            binario = '1101'
            conta = '1x2**3 + 1x2**2 + 0x2**1 + 1x2**0'
        elif digito == 'E':
            binario = '1110'
            conta = '1x2**3 + 1x2**2 + 1x2**1 + 0x2**0'
        elif digito == 'F':
            binario = '1111'
            conta = '1x2**3 + 1x2**2 + 1x2**1 + 1x2**0'

        mensagem_passo = (' Passo %d: %s = %s = %s' % (passo_a_passo, digito, conta, binario))
        print('|' + mensagem_passo.ljust(70) + '|')

        binario_completo = binario_completo + binario
        passo_a_passo += 1

    # adiciona zeros a esquerda para formar grupos de 3
    while len(binario_completo) % 3 != 0:
        binario_completo = '0' + binario_completo

    grupos = []

    # separa em grupos de 3 bits
    for i in range(0, len(binario_completo), 3):
        grupos.append(binario_completo[i:i + 3])

    # converte cada grupo de 3 bits para octal
    for grupo in grupos:
        valor = 0
        exponente = 2
        conta = ''

        for digito in grupo:
            calculo = int(digito) * 2 ** exponente
            valor = valor + calculo

            conta = conta + '%s x 2**%d + ' % (digito, exponente)

            exponente = exponente - 1

        mensagem_passo = (' Passo %d: %s = %d, que é igual a %d' % (passo_a_passo, conta, valor, valor))
        print('|' + mensagem_passo.ljust(70) + '|')

        resultado = resultado + str(valor)
        passo_a_passo += 1

    conta_passos = ''

    for passo in range(1, passo_a_passo):
        conta_passos = conta_passos + str(passo) + ','

    if passo_a_passo > 2:
        mensagem_Ultpasso = (' Passo %d: Junte os valores octais encontrados nos passos %s' % (passo_a_passo, conta_passos))
        print('|' + mensagem_Ultpasso.ljust(70) + '|')

    print('|' + '-' * 70 + '|')
    mensagem_Resultado = (' Resultado: %s' % resultado)
    print('|' + mensagem_Resultado.ljust(70) + '|')
    print('|' + '-' * 70 + '|')



