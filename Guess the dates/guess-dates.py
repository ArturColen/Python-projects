import json
import random

# Access data from the JSON file
file = open('Guess the dates\dates.json', encoding='utf8')

dates = json.load(file)
choice_computer = random.choice(list(dates.keys()))

# Start the game
print('********** Seja bem-vindo ao Guess the date! **********\n')
answer_user = input('Deseja começar o quiz? (S/N) ').lower()

if answer_user != 's':
    quit()

number_choices = 5
win = False

# View the tip and check the user's response
while number_choices > 0 and win is not True:
    print('\nDica ' + dates[choice_computer])
    answer_user = input('\nData (DDMMAAAA): ')

    if len(answer_user) != 8:
        print('\nErro: a resposta deve conter 8 digitos!')
        continue

    if answer_user.isdigit():
        check = []
        score = 0

        for i in range(8):
            if answer_user[i] == choice_computer[i]:
                check.append('✅')
                score = score + 1
            else:
                check.append('❌')

        print('\nResposta: ')
        print('|'.join(check))
        print(' |'.join(answer_user))

        if score == 8:
            win = True
    else:
        print('\nErro: a resposta deve ser uma data!')
        continue

    number_choices = number_choices - 1

# Check the game result
if win == True:
    print('\nParabéns! Você ganhou!')
else:
    print('\nVocê perdeu! :(')
    print('A resposta era: ' + choice_computer)