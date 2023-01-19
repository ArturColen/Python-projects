from functions import *

due_date = input('Qual a data de vencimento (formato: DD-MM-YYYY)? ')

# Verify user input
if len(due_date) == 10:
    print(verify_due(due_date))
else:
    print('Entrada inválida!')