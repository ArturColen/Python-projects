# Start the quiz
print('********** Seja bem-vindo ao quiz de Python! **********\n')
answer_user = input('Deseja começar o quiz? (S/N) ').lower()

if answer_user != 's':
    quit()

score = 0

print('\nComeçando...\n')

# Display the questions and check that the answers are correct
print('1 - Qual é a sintaxe correta para gerar "Hello World" em Python?\n(A) p("Hello World")\n(B) echo("Hello World")\n(C) print("Hello World")\n')
answer_1 = input('Resposta: ').lower()

if answer_1 == 'c':
    print('Correto!\n')
    score = score + 1
else:
    print('Incorreto!\n')

print('2 - Como você insere comentários no código Python?\n(A) # Isso é um comentário\n(B) /* Isso é um comentário */\n(C) // Isso é um comentário\n')
answer_2 = input('Resposta: ').lower()

if answer_2 == 'a':
    print('Correto!\n')
    score = score + 1
else:
    print('Incorreto!\n')

print('3 - Qual NÃO é um nome de variável legal?\n(A) minha_variavel\n(B) minha-variavel\n(C) MinhaVariavel\n')
answer_3 = input('Resposta: ').lower()

if answer_3 == 'b':
    print('Correto!\n')
    score = score + 1
else:
    print('Incorreto!\n')

print('4 - Como você cria uma variável com o valor numérico 5?\n(A) x = int(5)\n(B) x = 5\n(C) Ambas alternativas estão corretas\n')
answer_4 = input('Resposta: ').lower()

if answer_4 == 'c':
    print('Correto!\n')
    score = score + 1
else:
    print('Incorreto!\n')

print('5 - Qual é a extensão de arquivo correta para arquivos Python?\n(A) .pt\n(B) .pyt\n(C) .py\n')
answer_5 = input('Resposta: ').lower()

if answer_5 == 'c':
    print('Correto!\n')
    score = score + 1
else:
    print('Incorreto!\n')

print('6 - Como você cria uma variável com o número flutuante 2.8?\n(A) y = 2.8\n(B) y = 2,8\n(C) y = float(2,8)\n')
answer_6 = input('Resposta: ').lower()

if answer_6 == 'a':
    print('Correto!\n')
    score = score + 1
else:
    print('Incorreto!\n')

print('7 - Qual é a maneira correta de criar uma função em Python?\n(A) def minhaFuncao()\n(B) create minhaFuncao()\n(C) function minhaFuncao()\n')
answer_7 = input('Resposta: ').lower()

if answer_7 == 'a':
    print('Correto!\n')
    score = score + 1
else:
    print('Incorreto!\n')

print('8 - Qual é a sintaxe correta para retornar o primeiro caractere em uma string?\n(A) x = "Hello".sub(0, 1)\n(B) x = "Hello"[0]\n(C) x = sub("Hello", 0, 1)\n')
answer_8 = input('Resposta: ').lower()

if answer_8 == 'b':
    print('Correto!\n')
    score = score + 1
else:
    print('Incorreto!\n')

print('9 - Qual método pode ser usado para retornar uma string em letras maiúsculas?\n(A) uppercase()\n(B) toUpperCase()\n(C) upper()\n')
answer_9 = input('Resposta: ').lower()

if answer_9 == 'c':
    print('Correto!\n')
    score = score + 1
else:
    print('Incorreto!\n')

print('10 - Qual método pode ser usado para substituir partes de uma string?\n(A) replace()\n(B) repl()\n(C) replaceString()\n')
answer_10 = input('Resposta: ').lower()

if answer_10 == 'a':
    print('Correto!\n')
    score = score + 1
else:
    print('Incorreto!\n')

print('11 - Qual operador é usado para multiplicar números?\n(A) %\n(B) *\n(C) x\n')
answer_11 = input('Resposta: ').lower()

if answer_11 == 'b':
    print('Correto!\n')
    score = score + 1
else:
    print('Incorreto!\n')    

print('12 - Qual dessas coleções define uma lista?\n(A) ("maçã", "banana", "cereja")\n(B) ["maçã", "banana", "cereja"]\n(C) {"maçã", "banana", "cereja"}\n')
answer_12 = input('Resposta: ').lower()

if answer_12 == 'b':
    print('Correto!\n')
    score = score + 1
else:
    print('Incorreto!\n')

print('13 - Qual dessas coleções define um dicionário?\n(A) {"nome": "maçã", "cor": "verde"}\n(B) ["maçã", "banana", "cereja"]\n(C) ("maçã", "banana", "cereja")\n')
answer_13 = input('Resposta: ').lower()

if answer_13 == 'a':
    print('Correto!\n')
    score = score + 1
else:
    print('Incorreto!\n')

print('14 - Como você começa a escrever uma instrução if em Python?\n(A) if (x > y)\n(B) if x > y then:\n(C) if x > y:\n')
answer_14 = input('Resposta: ').lower()

if answer_14 == 'c':
    print('Correto!\n')
    score = score + 1
else:
    print('Incorreto!\n')

print('15 - Como você começa a escrever um loop for em Python?\n(A) for x in y:\n(B) for each x in y:\n(C) for x > y:\n')
answer_15 = input('Resposta: ').lower()

if answer_15 == 'a':
    print('Correto!\n')
    score = score + 1
else:
    print('Incorreto!\n')

# Display the quiz result
print(f'O quiz acabou... Pontuação: {score}/15')