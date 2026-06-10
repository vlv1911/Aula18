import pandas as pd
import numpy as np

try:

    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

    df_registros = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')

    df_casos_estelionato = df_registros[['mes_ano', 'estelionato']]

    df_casos_estelionato = df_casos_estelionato.groupby('mes_ano', as_index=False)['estelionato'].sum()

except Exception as e:
    print(f'Erro ao obter os dados: {e}')
    exit()

try:
    print('Recebendo dados sobre números de casos de estelionato...')
    array_casos_estelionato = np.array(df_casos_estelionato['estelionato'])

    media_casos_estelionato = np.mean(array_casos_estelionato)
    mediana_casos_estelionato = np.median(array_casos_estelionato)
    total_casos_estelionato = np.sum(array_casos_estelionato)

    print('\nTendencias...')                                                        
    print(30*'-')
    print(f'Média de casos: {media_casos_estelionato:.2f}')
    print(f'Mediana de casos: {mediana_casos_estelionato:.2f}')
    print(f'Total de casos: {total_casos_estelionato}')

    q1 = np.quantile(array_casos_estelionato, 0.25)
    q2 = np.quantile(array_casos_estelionato, 0.50)
    q3 = np.quantile(array_casos_estelionato, 0.75)

    print('\nMedições: ')
    print(30*'-')
    print(f'Q1: {q1}')
    print(f'Q2: {q2}')
    print(f'Q3: {q3}')

    df_casos_estelionato_menores = df_casos_estelionato[df_casos_estelionato['estelionato'] < q1]

    df_casos_estelionato_maiores = df_casos_estelionato[df_casos_estelionato['estelionato'] > q3]

    print('\nMenores casos de estelionato:')
    print(30*'-')
    print(df_casos_estelionato_menores.head(10).sort_values(by='estelionato', ascending=True))

    print('\nMaiores casos de estelionato:')
    print(30*'-')
    print(df_casos_estelionato_maiores.head(10).sort_values(by='estelionato', ascending=False))

except Exception as e:
    print(f'Erro ao calcular as informações...')

