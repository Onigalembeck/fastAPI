import random 

def geraraleatorio(n):
    return random.randint(10**n, 9*10**n)

def gera_boleto():
    return f"0019{geraraleatorio(5)}5{geraraleatorio(10)}9{geraraleatorio(10)}43{geraraleatorio(4)}{geraraleatorio(10)}"
