from datetime import datetime

LISTA_CARTAO= {
    "01":"Cartão1",
    "03":"Cartão2",
    "09":"Cartão3"
}

def check_bandeira_cartao(numero_cartao):
    first_digits = numero_cartao[0:2]
    for number in LISTA_CARTAO:
        if first_digits == number:
            return LISTA_CARTAO[number]
    return "NAO VALIDO"

def check_validade_cartao(data):
 data_de_validade=datetime.strptime(data, "%m/%y")
 valido=datetime.strptime("04/22", "%m/%y" )
 if data_de_validade >= valido:
    return "dentro da validade"
 else:
    return "fora da validade"