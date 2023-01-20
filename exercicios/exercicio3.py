import json

with open("exercicios/dados.json") as f:
    vetor = json.load(f)


def calc_media(vetor: list):
    soma = 0
    for valor in vetor:
        soma += valor['valor']
    return soma / len(vetor)


def calc_maior(vetor: list):
    maior = 0
    for valor in vetor:
        maior = valor['valor'] if valor['valor'] > maior else maior
    return maior


def calc_menor(vetor: list):
    menor = calc_maior(vetor)
    for valor in vetor:
        menor = valor['valor'] if valor['valor'] < menor else menor
    return menor


def calc_dias_media(vetor: list):
    media = calc_media(vetor)
    dias = 0
    for valor in vetor:
        if valor['valor'] > media:
            dias+= 1
    return dias

print(calc_maior(vetor))
print(calc_menor(vetor))
print(calc_dias_media(vetor))
