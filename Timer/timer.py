import time

# Start the program
print('********** Seja bem-vindo ao temporizador do Artur! **********\n')

t = input('Digite o tempo (em segundos): ')

# Verify that a number has been entered correctly
if t.isdigit():
    t = int(t)
    print() # Skip a line in the terminal
else:
    print('\nEntrada inválida!')

# Run the timer
while t:
    minutes, seconds = divmod(t, 60)
    timer = '{:02d}:{:02d}'.format(minutes, seconds)
    print(timer, end='\r')
    time.sleep(1)
    t = t - 1

print()
print('\nO TEMPO ACABOU!')