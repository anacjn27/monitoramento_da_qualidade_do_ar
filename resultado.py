import os
import json

# Tentando abrir o arquivo json
PATH = os.path.abspath(os.path.dirname(__file__))
nome_arquivo = 'dados_IQA_regiao_metrop.json'
caminho = os.path.join(PATH, nome_arquivo)

with open(caminho, 'r') as file:
    data = json.load(file)

# Classificação do IQA em forma de lista
classificacoes_iqa = [
    (0, 50, "Qualidade BOA"),
    (51, 100, "Qualidade REGULAR"),
    (101, 199, "Qualidade INADEQUADA"),
    (200, 299, "Qualidade MÁ"),
    (300, float('inf'), "Qualidade PÉSSIMA")
]

# Função de classificação usando a lista
def classificar_IQA(iqa):
    for faixa in classificacoes_iqa:
        if faixa[0] <= iqa <= faixa[1]:
            return faixa[2]
    return "Valor fora da escala"

# Função para calcular o IQA
def calcular_IQA(C, Cf, Ci, If, Ii):
    Ip = ((If - Ii) / (Cf - Ci)) * (C - Ci) + Ii
    return Ip

# Faixas de concentração dos poluentes
faixas_concentracao = {
    'SO2': [
        [0, 80], [81, 365], [366, 800], [801, 1600], [1600, 0]
    ],
    'CO': [
        [0, 4], [4.1, 9], [9.1, 15], [15.1, 30], [30, 0]
    ],
    'PM10': [
        [0, 50], [51, 150], [151, 250], [251, 420], [420, 0]
    ],
    'O3': [
        [0, 80], [81, 160], [161, 200], [201, 800], [800, 0]
    ],
    'NO2': [
        [0, 100], [101, 320], [321, 1130], [1131, 2260], [2260, 0]
    ],
}

# Valores IQA para cada faixa
valores_iqa = [(0, 50), (51, 100), (101, 200), (201, 300), (300, 0)]

# Dicionário para armazenar os resultados do IQA
resultados_ip = {}

#IQA para cada poluente
for nome, dados in data.items():
    media_valor = sum(dados) / len(dados)  # Calculando a média dos dados
     
     
    
    indice = 0
    for faixa in faixas_concentracao[nome]:
        if faixa[0] <= media_valor <= faixa[1]:
            

            calculo_ip = calcular_IQA(
                media_valor, 
                faixa[1], 
                faixa[0], 
                valores_iqa[indice][1], 
                valores_iqa[indice][0]
            )
            

            resultados_ip[nome] = calculo_ip
            break
        indice += 1

# Encontrar o poluente com o maior valor de IQA (Ip)
poluente_dominante = max(resultados_ip, key=resultados_ip.get)
iqa_dominante = resultados_ip[poluente_dominante]


print(f"Poluente com maior valor de IQA: {poluente_dominante}, Valor IQA = {iqa_dominante:.2f}")
