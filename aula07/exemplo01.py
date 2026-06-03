import pandas as pd
import numpy as np

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

    
except Exception as e:
    print(f'Erro ao calcular as informações...')