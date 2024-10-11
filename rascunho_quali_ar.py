SO2 = float(input('nível de SO2'))
NO2 = float(input('nivel de NO2'))
O3 = float(input('nível de O3'))
CO2 = float(input('nível de CO2'))
CH4 = float(input('nível de CH4'))

parametros_do_ar = [NO2,SO2,O3, CO2, CH4]

def qualidade_do_ar (SO2, NO2, O3, CO2, CH4):
   
   for valor in parametros_do_ar:
   
    if valor >= 0 and valor <= 19:
        print('qualidade excelente')
    elif valor <=49:
        print('qualidade razoavel')
    elif valor <= 99:
         print('qualidade ruim')
    elif valor <= 149:
        print('qualidade insalubre')
    elif valor <= 249:
            print('qualidade muito isalubre')
    elif valor >= 250:
        print('qualidade perigosa')

qualidade_do_ar(SO2, NO2, O3, CO2, CH4)