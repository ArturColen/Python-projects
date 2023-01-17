import random

# Start the game
print('**********Seja bem-vindo ao Guess Number!**********\n')
choice_number = input('Digite o número teto do desafio: ')

# Check if the entered value is numeric and generate the random number
if choice_number.isdigit():
    choice_number = int(choice_number)
else:
    print('\nErro: o valor informado não é numérico! Favor executar novamente e informar um número.')
    quit()

random_number = random.randint(0, choice_number)

number_choices = 0

# Enter a number and check if you got it right or not
while True:
    answer_user = input('\nAdivinhe o número: ')

    if answer_user.isdigit():
        answer_user = int(answer_user)
    else:
        print('\nErro: o valor informado não é numérico! Favor informar um número.')
        continue

    number_choices = number_choices + 1

    if answer_user == random_number:
        print('\nAcertou!')
        break
    elif answer_user > random_number:
        print('\nChutou alto! O número aleatório é menor que isso...')
    else:
        print('\nChutou baixo! O número aleatório é maior que isso...')

# Show the number of attempts
print('\nNúmero de tentativas: ' + str(number_choices))