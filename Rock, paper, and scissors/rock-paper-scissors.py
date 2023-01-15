import random

# Start the game
print('**********Seja bem-vindo ao Pedra, Papel e Tesoura!**********\n')
username = input('Digite seu nome: ').upper()

# Initial data
user_points = 0
computer_points = 0
options = ['r', 'p', 't']

while True:
    # Verify the choice entered by the user
    user_choice = input(f'\n{username}, escolha R(Pedra), P(Papel), T(Tesoura) ou S para sair: ').lower()

    if user_choice == 's':
        break

    if user_choice not in options:
        print('\nOpção inválida!')
        continue

    # Random computer choice
    computer_choice = random.randint(0, 2) # 0: R, 1: P, 2: T
    computer_option = options[computer_choice]

    print('\nO computador escolheu: ' + computer_option.upper())

    # Check and display the round result
    if user_choice == computer_option:
        print('\nEmpate!')
    elif user_choice == 'r' and computer_option == 't':
        print('\nVocê ganhou!')
        user_points = user_points + 1
    elif user_choice == 'p' and computer_option == 'r':
        print('\nVocê ganhou!')
        user_points = user_points + 1
    elif user_choice == 't' and computer_option == 'p':
        print('\nVocê ganhou!')
        user_points = user_points + 1
    else:
        print('\nVocê perdeu!')
        computer_points = computer_points + 1

# Show the game result
print(f'\n{username} {user_points} X {computer_points} COMPUTADOR')

if user_points > computer_points:
    print('\nParabéns! Você ganhou.')
elif user_points < computer_points:
    print('\nTá ruin, ein? Você perdeu.')
else:
    print('\nEmpate!')