dicionario = {'SP': 67836.43, "RJ": 36678.66, "MG": 29229.88, "ES": 27165.48, "Outros": 19849.53}
dicionario2 = {'teste': 5, 'teste2': 5}

def calc_percentual(dicionario: dict):
    list = dicionario.keys()
    soma = 0
    for item in list:
        soma += dicionario[item]
    total = soma

    todos_percentuais = []
    for item in list:
        percentual  = 100 * dicionario[item] / total 
        todos_percentuais.append(f'{item} - {"%.2f" % percentual}%')

    return todos_percentuais

     

print(calc_percentual(dicionario))