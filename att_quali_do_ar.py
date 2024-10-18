import numpy as np 
import matplotlib.pyplot as plt  # Correção aqui

SO2 = float(input('nível de SO2: '))
NO2 = float(input('nível de NO2: '))
O3 = float(input('nível de O3: '))
CO2 = float(input('nível de CO2: '))
CH4 = float(input('nível de CH4: '))

parametros_do_ar = [("NO2", NO2),
                    ("SO2", SO2),
                    ("O3", O3),
                    ("CO2", CO2),
                    ("CH4", CH4)]
                 
def qualidade_do_ar(parametros):
    for nome, valor in parametros:
        if valor >= 0 and valor <= 19:
            print(f'níveis de {nome} com qualidade excelente {valor}')
        elif valor <= 49:
            print(f'níveis de {nome} com qualidade razoável {valor}')
        elif valor <= 99:
            print(f'níveis de {nome} com qualidade ruim {valor}')
        elif valor <= 149:
            print(f'níveis de {nome} com qualidade insalubre {valor}')
        elif valor <= 249:
            print(f'níveis de {nome} com qualidade muito insalubre {valor}')
        elif valor >= 250:
            print(f'níveis de {nome} com qualidade perigosa {valor}')

qualidade_do_ar(parametros_do_ar)

def qualidade_média_do_ar():
    média = np.mean([valor for _, valor in parametros_do_ar])

    if média >= 0 and média <= 19:
        return 'excelente'
    elif média <= 49:
        return 'razoável'
    elif média <= 99:
        return 'ruim'
    elif média <= 149:
        return 'insalubre'
    elif média <= 249:
        return 'muito insalubre'
    elif média >= 250:
        return 'perigoso'

resultado = qualidade_média_do_ar()
print(f'A média dos níveis de poluição do ar é: {resultado}')

# Dados para o gráfico
nomes = [nome for nome, _ in parametros_do_ar]
valores = [valor for _, valor in parametros_do_ar]

# Plotar gráfico de barras
plt.bar(nomes, valores)

# Rótulos e título
plt.xlabel('Substâncias')
plt.ylabel('Níveis de Poluição')
plt.title('Níveis de Poluição do Ar')

# Mostrar gráfico
plt.show()
