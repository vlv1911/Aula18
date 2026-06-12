# python - venv venv
# souce ./venv/source/activate
# pip install pandas numpy
# pip install matplotlib

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# obtendo dados:

try:
    print('Obtendo os dados...')

    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

    # iso-8859-1 | utf-8 | latin1 | cp1252
    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')

    # delimitando as variáveis:

    df_roubo_veiculo = df_ocorrencias[['munic', 'roubo_veiculo']]

    # agrupando e quantificando as variáveis quantitativas
    df_roubo_veiculo = df_roubo_veiculo.groupby('munic', as_index=False)['roubo_veiculo'].sum()

    # ordena em decrescente
    df_roubo_veiculo = df_roubo_veiculo.sort_values(by='roubo_veiculo', ascending=False)

    # print(df_roubo_veiculo)
                                
except Exception as e:
    print(f'Erro ao obter os dados: {e}')
    exit()

# Obtendo informações:

try:
    print('Obtendo informações a cerca dos roubos de veículos...')
    array_roubo_veiculo = np.array(df_roubo_veiculo['roubo_veiculo'])

    media_roubo_veiculo = np.mean(array_roubo_veiculo)
    mediana_roubo_veiculo = np.median(array_roubo_veiculo)
    distancia = abs((media_roubo_veiculo - mediana_roubo_veiculo) / mediana_roubo_veiculo * 100)

    print('\nMedidas de tendência central:')
    print(29*'=')
    print(f'Média: {media_roubo_veiculo:.2f}')
    print(f'Mediana: {mediana_roubo_veiculo:.2f}')
    print(f'Distância entre média e mediana: {distancia:.2f}%')

    # obtendo os quartis

    q1 = np.quantile(array_roubo_veiculo, 0.25)
    q2 = np.quantile(array_roubo_veiculo, 0.50)
    q3 = np.quantile(array_roubo_veiculo, 0.75)

    print('\nMedidas Posição:')
    print(16*'=')
    print(f'Q1: {q1:.2f}')
    print(f'Q2: {q2:.2f}')
    print(f'Q3: {q3:.2f}')

    # menores

    df_roubo_veiculo_menores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] < q1]

    # maiores

    df_roubo_veiculo_maiores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] > q3]

    print('\nMunicipios com mais roubos')
    print(40 * '=')
    print(df_roubo_veiculo_maiores)

    print('\nMunicipios com mais roubos')
    print(40 * '=')
    # ordem decrescente
    print(df_roubo_veiculo_menores.sort_values(by='roubo_veiculo', ascending=True))

except Exception as e:
    print(f'Erro ao calcular as informações...')

# Verificando Medidas de dispersão - Amplitude total:

try:
    # Amplitude Total = meu maior_valor - menor_valor
    # Quanto mais próximo de zero, maior a homogeneidade dos dados
    # Se for igual a 0 (zero), todos os dados são iguais
    # Quanto mais próximo do maior valor, maior a dispersão
    maximo = np.max(array_roubo_veiculo)
    minimo = np.min(array_roubo_veiculo)
    amplitude = maximo - minimo

    print('\nMedidas de dispersão: ')
    print(25 * '=')
    print(f'Máximo: {maximo}')
    print(f'Mínimo: {minimo}')
    print(f'Amplitude total: {amplitude}')
    
except Exception as e:
    print(f'Erro ao calcular Medidas de dispersão... {e}')


# Outliers:
    
try:
    # IQR (Intervalo Interquartil)
    # É a amplitude dos 50% dos dados mais centrais
    # IQR = Q3 - Q1
    # Ele ignora os valores mais extremos, max e min estão fora
    # Não sofre influência dos extremos
    # Quanto mais próximo de zero, maior a homogeneidade dos dados
    # Se for igual a 0 (zero), todos os dados são iguais
    # Quanto mais próximo do Q3, maior a dispersão
    iqr = q3 - q1

    # print(f'\nIQR: {iqr}')

    # Limite superior:
    limite_superior = q3 + (1.5 * iqr)
      
    # Limite inferior:
    limite_inferior = q1 - (1.5 * iqr)

    # Outliers:
    df_roubo_veiculo_outliers_superiores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] > limite_superior]

    df_roubo_veiculo_outliers_inferiores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] < limite_inferior]

    print('\nMedidas: ')
    print(25 * '=')
    print(f'Mínimo: {minimo}')
    print(f'Limite inferior: {limite_inferior}')
    print(f'Q1: {q1}')
    print(f'Q2: {q2}')
    print(f'Q3: {q3}')
    print(f'IQR: {iqr}')
    print(f'Limite superior: {limite_superior}')
    print(f'Máximo: {maximo}')
    
    # Printando os Outliers:
    print('\nOutliers superiores: ')
    print(50 * '=')
    if len(df_roubo_veiculo_outliers_superiores) == 0:
        print('Não existem Outliers superiores')
    else:
        print(f'\n{df_roubo_veiculo_outliers_superiores}')

    print('\nOutliers inferiores: ')
    print(50 * '=')
    if len(df_roubo_veiculo_outliers_inferiores) == 0:
        print('Não existem Outliers inferiores')
    else:
        print(f'\n{df_roubo_veiculo_outliers_inferiores}')
    
except Exception as e:
    print(f'Erro ao calcular Outliers {e}')


# Visualizando os dados:
try:
    # mostrando cidades com maiores números de roubos
    plt.figure(figsize=(16, 8))
    df_roubo_veiculo_outliers_superiores = df_roubo_veiculo_outliers_superiores.sort_values(by='roubo_veiculo', ascending=True) 
    plt.barh(df_roubo_veiculo_outliers_superiores['munic'], df_roubo_veiculo_outliers_superiores['roubo_veiculo'])
    plt.title('Cidades com os maiores casos de roubos de veículos:')
    plt.show()


except Exception as e:
    print(f'Erro ao plotar o gráfico: {e}')