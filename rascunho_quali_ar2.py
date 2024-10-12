import numpy as np

SO2 = float(input('Insira nível de SO2: '))
NO2 = float(input('Insira nivel de NO2: '))
O3 = float(input('Insira nível de O3: '))
CO2 = float(input('Insira nível de CO2: '))
CH4 = float(input('Insira nível de CH4: '))

parametros_do_ar = [NO2,SO2,O3, CO2, CH4]

def qualidade_do_ar ():
   
   for valor in parametros_do_ar:
   
    if valor >= 0 and valor <= 19:
        print('Nível está excelente')
    elif valor <=49:
        print('Nível está razoavel')
    elif valor <= 99:
         print('Nível está ótimo')
    elif valor <= 149:
        print('Nível está insalubre')
    elif valor <= 249:
            print('Nível está muito isalubre')
    elif valor >= 250:
        print('Nível está perigoso')

resultado = qualidade_do_ar()

print(resultado)

def qualidade_média_do_ar ():
    
    média = np.mean(parametros_do_ar)
    if média >= 0 and média <= 19:
                return 'excelente'
    elif média <=49:
                return 'razoável'
    elif média <= 99:
                return 'ótimo'
    elif média <= 149:
                return 'insalubre'
    elif média <= 249:
                return 'muito insalubre'
    elif média >= 250:
                return 'perigoso'

resultado2 = qualidade_média_do_ar()
print(f'A média dos níveis de poluição do ar é: {resultado2}')
