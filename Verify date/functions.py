from datetime import datetime

def today():
    today = datetime.now()
    return today

def verify_date(date):
    try:
        date_format = datetime.strptime(date, '%d-%m-%Y')
        return date_format
    except:
        raise Exception('Entrada inválida! Formato sugerido: DD-MM-YYYY')

def verify_due(date_ref):
    due_date = verify_date(date=date_ref)

    if today() > due_date:
        return 'A data expirou!'
    else:
        return 'A data não expirou!'