import pandas as pd
import openpyxl
import json
import csv


# Funçao que ler os dados
def carregar_dados(path_json,path_csv):
    dados_csv_v2 = pd.read_csv(path_csv, delimiter=',')
    dados_json_v2 = pd.read_json(path_json)
    
    return dados_json_v2,dados_csv_v2



path_json = '../data_raw/dados_empresaA.json'
path_csv = '../data_raw/dados_empresaB.csv'

dados_csv_v2, dados_json_v2 = carregar_dados(path_json, path_csv)


# Funçao modifica csv para conter os mesmo campos do json

def processar_dados_csv(dados_csv):
    
    dados_csv = dados_csv_v2.rename(columns={
    'Nome do Item':'Nome do Produto',
    'Classificação do Produto' :'Categoria do Produto' ,
    'Valor em Reais (R$)':'Preço do Produto (R$)',
    'Quantidade em Estoque':'Quantidade em Estoque',
    'Nome da Loja':'Filial'
    'Data da Venda':'Data da Venda'
    })
    

    return dados_csv



dados_csv_v2 = processar_dados_csv(dados_csv_v2)

print(dados_csv_v2)


#Funçao que unifica os 2 dfs:

def unifica_dados(dados_csv,dados_json):
    unificado = pd.concat([dados_csv,dados_json]).reset_index()
    
    return unificado

unificado = unifica_dados(dados_csv_v2,dados_json_v2)

print(unificado)


# Funçao para salvar o arquivo final

def salvar_arquivo(caminho,arquivo):
    caminho_completo = caminho + arquivo
    with pd.ExcelWriter(caminho_completo) as writer:
        unificado.to_excel(writer,index=False)
    
    return caminho_completo

caminho = '../data_processed/'
arquivo = 'dados_completo.xlsx'

caminho_completo = salvar_arquivo(caminho,arquivo)



    
