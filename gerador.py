import os
import json

#tentando abrir o arquivo json

PATH = os.path.abspath(os.path.dirname(__file__))
nome_arquivo = 'dados_IQA_regiao_metrop.json'
caminho = os.path.join(PATH, nome_arquivo)


with open(caminho, 'r') as file:
        data = json.load(file)


# classificação do IQA
def classificar_IQA(iqa):
    if 0 <= iqa <= 50:
        return "Qualidade BOA"
    elif 51 <= iqa <= 100:
        return "Qualidade REGULAR"
    elif 101 <= iqa <= 199:
        return "Qualidade INADEQUADA"
    elif 200 <= iqa <= 299:
        return "Qualidade MÁ"
    elif iqa >= 300:
        return "Qualidade PÉSSIMA"
    else:
        return "Valor fora da escala"

#equação para o IQA
    
 def calcular_IQA(C, Cf, Ci, If, Ii):
    Ip = ((If - Ii) / (Cf - Ci)) * (C - Ci) + Ii
    return Ip

resultados = {}

#constantes e variáveis da equação
for nome, dados in data.items():
        media_valor = sum(dados) / len(dados)
        Cf, Ci, If, Ii = 300, 0, 500, 0

#resultado
Ip = calcular_IQA(media_valor, Cf, Ci, If, Ii)
resultados[nome] = Ip


poluente_dominante = max(resultados, key=resultados.get)

print(f"Poluente dominante: {poluente_dominante}, Valor IQA: {resultados[poluente_dominante]}")
for poluente, valor in resultados.items():
    print(f"{poluente}: {valor} ({classificar_IQA(valor)})")

# fazer um gráfico
