while True:
    operação = input('Escolha a operação (+, /, * ou -): ')
    if operação not in ('+', '/', 'x', '*', '-'):
        print('Operação inválida. Tente novamente.')
        continue

    number1 = input('Digite o primeiro número: ')
    number2 = input('Digite o segundo número: ' + number1 + ' ' + operação + ' ')

    try:
        number1 = float(number1)
        number2 = float(number2)
    except ValueError:
        print("Por favor, digite números válidos.")
        continue

    resposta_soma = float(number1) + float(number2)
    resposta_div = float(number1) / float(number2)
    resposta_mult = float(number1) * float(number2)
    resposta_sub = float(number1) - float(number2)

    if operação == ("+"):
        print (resposta_soma)
    elif operação == ("/"):
        print (resposta_div)
    elif operação == ("*") or str('x'):
        print (resposta_mult)
    elif operação == ("-"):
        print (resposta_sub)
    else:
        print ("Operação inválida.")