import random
import string

# Create a random password from a defined length
def password_generator(len_pass = 8):
    ascii_options = string.ascii_letters
    number_options = string.digits
    punt_options = string.punctuation
    options = ascii_options + number_options + punt_options

    password_user = ''

    for i in range(0, len_pass):
        digit = random.choice(options)
        password_user = password_user + digit

    return password_user

# Start the program
print('********** Seja bem-vindo ao password generator! **********\n')
choice_user = input('Quantos digitos sua senha deve ter? ')

# Verify that the password length entered by the user is valid
if choice_user.isdigit():
    choice_user = int(choice_user)
else:
    print('\nEntrada inválida!')
    quit()

# Show the created password
response = password_generator(len_pass = choice_user)
print(f'\nA senha gerada é: {response}')