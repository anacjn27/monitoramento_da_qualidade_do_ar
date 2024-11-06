def calcular_IQA(C, Cf, Ci, If, Ii):
    Ip = ((If - Ii) / (Cf - Ci)) * (C - Ci) + Ii
    return Ip

# função para calcular o indice de qualidade do ar
# Ip = indice para o poluente
# If = valor do IQA máximo da faixa onde o poluente se encontra
# Ii = valor do IQA mínimo da faixa onde o poluente se encontra
# Cf = valor máximo da faixa de concentração onde o poluente se encontra
# Ci = valor mínimo da faixa de concentração onde o poluente se encontra
# C = concentração média do poluente

def calcular_IQA_para_poluentes(poluentes):
    resultados = {}
    for nome, dados in poluentes.items():
        C = dados['C']
        Cf = dados['Cf']
        Ci = dados['Ci']
        If = dados['If']
        Ii = dados['Ii']
        
        Ip = calcular_IQA(C, Cf, Ci, If, Ii)
        resultados[nome] = 
