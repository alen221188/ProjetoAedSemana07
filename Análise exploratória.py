# ============================================================
#        ANÁLISE EXPLORATÓRIA DE DADOS — VAREJO
#        Projeto — AED Semana 07
# ============================================================


# ============================================================
# SPRINT 1 — IMPORTAÇÃO DOS DADOS
# ============================================================

# --- Importando as Bibliotecas ---
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import os

print("Bibliotecas importadas com sucesso!")
print(f"   pandas:     {pd.__version__}")
print(f"   numpy:      {np.__version__}")
print(f"   matplotlib: {plt.matplotlib.__version__}")
print(f"   seaborn:    {sns.__version__}")
print("-" * 50)


# --- Leitura da Base de Dados ---
df = pd.read_csv('Base Varejo.csv', sep=";", encoding="UTF8")
print("DataFrame carregado, Leitura concluída:")
print(f"\nDimensões do DataFrame: {df.shape}")
print(f"\n{df.shape[0]} linhas | {df.shape[1]} colunas")
print('-' * 50)


# --- Exploração Inicial dos Dados ---
print("Iniciando a Exploração Inicial dos Dados")
print('-' * 50)

print("\n5 Primeiras linhas")
print(df.head())
print('-' * 50)

print("\n5 Últimas linhas")
print(df.tail())
print('-' * 50)

print("\n5 Linhas aleatórias")
print(df.sample(5))
print('-' * 50)


# --- Informações Gerais do DataFrame ---
print("\nInformações Gerais do DataFrame")
print('-' * 50)
df.info()
print('-' * 100)

print("\nEstatísticas Descritivas (colunas numéricas):")
print('-' * 50)
print(df.describe())

print("\nValores Nulos:")
print('-' * 50)
print(df.isnull().sum().to_frame(name="Nulos"))


# ============================================================
# SPRINT 2 — TRANSFORMAÇÃO DE STRINGS, INTEGER, FLOAT E DATETIME
# ============================================================

# --- Identificando Tipos de Dados ---
print("\nVerificando os tipos de dados")
print(df.dtypes.to_frame(name="Tipo de dados"))


# --- Remoção de Colunas Completamente Nulas ---
colunas_nulas = df.columns[df.isnull().all()].tolist()

print(f"\nColunas completamente nulas (serão removidas):")
print(f"   {colunas_nulas}")

df_limpo = df.dropna(axis=1, how='all')


# --- Conversão da Coluna DATA (str → datetime) ---
print("\nConversão da coluna DATA:")
print(f"   Tipo ANTES : {df['DATA'].dtype}")

df_limpo['DATA'] = pd.to_datetime(df['DATA'], dayfirst=True)
print(f"   Tipo DEPOIS: {df_limpo['DATA'].dtype}")

df_limpo['ANO'] = df_limpo['DATA'].dt.year
df_limpo['MES'] = df_limpo['DATA'].dt.month
df_limpo['DIA'] = df_limpo['DATA'].dt.day

print(f"\nPeríodo da base:")
print(f"      Data inicial : {df_limpo['DATA'].min().strftime('%d/%m/%Y')}")
print(f"      Data final   : {df_limpo['DATA'].max().strftime('%d/%m/%Y')}")
print("-" * 50)


# --- Mapeamento Estado Civil (int → str) ---
print("\nTransformação CL_EC (Estado Civil):")

dicionario_estado_civil = {
    1: "Casado ou União Estável",
    2: "Divorciado",
    3: "Separado",
    4: "Solteiro",
    5: "Viúvo"
}

df_limpo["CL_EC"] = df_limpo["CL_EC"].map(dicionario_estado_civil)

print("Estado civil mapeado!")
print(dicionario_estado_civil)

print("\nTipos DEPOIS da transformação:")
print(df_limpo.dtypes.to_frame(name="Tipo"))


# ============================================================
# SPRINT 3 — LIMPEZA DE NULOS E DUPLICATAS
# ============================================================

# --- Tratamento da Coluna PR_CAT ---
def tratar_categoria(valor):
    if pd.isna(valor):
        return "Sem Categoria"
    elif valor == "#N/D":
        return "Sem Categoria"
    elif valor.strip() == "":
        return "Sem Categoria"
    else:
        return valor

df_limpo["PR_CAT"]  = df_limpo["PR_CAT"].apply(tratar_categoria)
df_limpo["PR_NOME"] = df_limpo["PR_NOME"].apply(tratar_categoria)

print("Categorias após tratamento (PR_CAT):")
print(df_limpo["PR_CAT"].unique())
print("-" * 50)


# --- Validação da Regra de Negócio do CO_ID ---
print("\nValidação do CO_ID (Número da Nota Fiscal):")
total_registros = len(df_limpo)
co_id_unicos    = df_limpo["CO_ID"].nunique()
co_id_repetidos = total_registros - co_id_unicos

print(f"   Total de registros  : {total_registros:,}")
print(f"   CO_IDs únicos       : {co_id_unicos:,}")
print(f"   CO_IDs que repetem  : {co_id_repetidos:,}")
print("-" * 50)

produtos_por_compra = df_limpo.groupby("CO_ID").size()
print(f"\n    Regra de Negócio identificada:")
print(f"      Média de produtos por nota  : {produtos_por_compra.mean():.2f}")
print(f"      Máx. produtos em uma nota   : {produtos_por_compra.max()}")
print(f"      Mín. produtos em uma nota   : {produtos_por_compra.min()}")
print(f"\n   ATENÇÃO: CO_ID se repete pois uma nota fiscal")
print(f"      pode conter vários produtos — comportamento ESPERADO!")
print("-" * 50)


# --- Verificando Duplicatas ---
print("\nVerificação de Linhas Duplicadas:")
duplicatas = df_limpo.duplicated().sum()
print(f"   Total de linhas duplicadas: {duplicatas}")

if duplicatas > 0:
    df_limpo = df_limpo.drop_duplicates()
    print(f"{duplicatas} duplicatas removidas!")
else:
    print("Nenhuma duplicata encontrada!")
print("-" * 50)


# --- Análise de Produtos Sem Categoria ---
print("\nDistribuição por Categoria (após limpeza):")
print(df_limpo['PR_CAT'].value_counts().sort_values(ascending=True))


# ============================================================
# SPRINT 4 — ESTATÍSTICA DESCRITIVA (CL_FHL)
# ============================================================

print("=== ESTATÍSTICAS BÁSICAS — CL_FHL ===")
print("   CL_FHL = Número de Filhos do Cliente")
print("=" * 50)

filhos = df_limpo["CL_FHL"]

print(f"\nPARÂMETROS ESTATÍSTICOS:")
print(f"   {'Contagem':<20}: {filhos.count():>12,.0f}")
print(f"   {'Média':<20}: {filhos.mean():>12.2f}")
print(f"   {'Mediana':<20}: {filhos.median():>12.2f}")
print(f"   {'Moda':<20}: {filhos.mode()[0]:>12.0f}")
print(f"   {'Desvio Padrão':<20}: {filhos.std():>12.2f}")
print(f"   {'Variância':<20}: {filhos.var():>12.2f}")
print(f"   {'Mínimo':<20}: {filhos.min():>12.0f}")
print(f"   {'Máximo':<20}: {filhos.max():>12.0f}")
print(f"   {'Q1 (25%)':<20}: {filhos.quantile(0.25):>12.2f}")
print(f"   {'Q2 (50%)':<20}: {filhos.quantile(0.50):>12.2f}")
print(f"   {'Q3 (75%)':<20}: {filhos.quantile(0.75):>12.2f}")
print(f"   {'Amplitude':<20}: {filhos.max() - filhos.min():>12.0f}")
print("-" * 50)

print("\nResumo via describe():")
print(filhos.describe())


# --- Análise de Distribuição de Compras ---
print("\n" + "=" * 60)
print("ANÁLISE DE DISTRIBUIÇÃO DE COMPRAS")
print("=" * 60)

print("\nCategoria Mais Vendida:")
categoria_vendas          = df_limpo['PR_CAT'].value_counts()
categoria_dominante       = categoria_vendas.index[0]
vendas_categoria_dominante = categoria_vendas.iloc[0]

print(f"   Categoria: {categoria_dominante}")
print(f"   Quantidade de compras: {vendas_categoria_dominante:,}")
print(f"   Percentual: {(vendas_categoria_dominante/len(df_limpo))*100:.1f}%")
print("\n   Top 5 Categorias:")
for idx, (cat, qtd) in enumerate(categoria_vendas.head().items(), 1):
    pct = (qtd/len(df_limpo))*100
    print(f"      {idx}. {cat:<30} : {qtd:>10,} ({pct:>5.1f}%)")
print("-" * 60)

print("\nSegmentação com Maior Volume de Compras:")
segmento_vendas          = df_limpo['CL_SEG'].value_counts()
segmento_dominante       = segmento_vendas.index[0]
vendas_segmento_dominante = segmento_vendas.iloc[0]

print(f"   Segmentação: {segmento_dominante}")
print(f"   Quantidade de compras: {vendas_segmento_dominante:,}")
print(f"   Percentual: {(vendas_segmento_dominante/len(df_limpo))*100:.1f}%")
print("\n   Todos as Segmentação:")
for idx, (seg, qtd) in enumerate(segmento_vendas.items(), 1):
    pct = (qtd/len(df_limpo))*100
    print(f"      {idx}. Segmento {seg:<20} : {qtd:>10,} ({pct:>5.1f}%)")
print("-" * 60)

print("\nProduto Mais Vendido:")
produto_vendas          = df_limpo['PR_NOME'].value_counts()
produto_dominante       = produto_vendas.index[0]
vendas_produto_dominante = produto_vendas.iloc[0]

print(f"   Produto: {produto_dominante}")
print(f"   Quantidade de compras: {vendas_produto_dominante:,}")
print(f"   Percentual: {(vendas_produto_dominante/len(df_limpo))*100:.1f}%")
print("\n   Top 10 Produtos Mais Vendidos:")
for idx, (prod, qtd) in enumerate(produto_vendas.head(10).items(), 1):
    pct = (qtd/len(df_limpo))*100
    print(f"      {idx:2d}. {prod:<40} : {qtd:>10,} ({pct:>5.1f}%)")
print("-" * 60)


# --- Agrupamentos ---
print("\n=== PADRÕES DE AGRUPAMENTO ===")

print("\nAgrupamento 1: Gênero x Categoria")
grupo1 = (df_limpo.groupby(["CL_GENERO", "PR_CAT"])["CO_ID"]
          .count().reset_index(name="QTD")
          .sort_values("QTD", ascending=False))
print(grupo1.head(10))

print("\nAgrupamento 2: Segmentação x Categoria")
grupo2 = (df_limpo.groupby(["CL_SEG", "PR_CAT"])["CO_ID"]
          .count().reset_index(name="QTD")
          .sort_values("QTD", ascending=False))
print(grupo2.head(10))

print("\nAgrupamento 3: Ano x Categoria")
grupo3 = (df_limpo.groupby(["ANO", "PR_CAT"])["CO_ID"]
          .count().reset_index(name="QTD")
          .sort_values(["ANO", "QTD"], ascending=[True, False]))
print(grupo3.head(10))


# ============================================================
# SPRINT 5 — RELATÓRIO FINAL E EXPORTAÇÃO
# ============================================================

print("\n" + "=" * 60)
print("            RELATÓRIO FINAL DO PROJETO")
print("           Análise Exploratória de Dados — Varejo")
print("=" * 60)

print(f"\n BASE DE DADOS:")
print(f"   {'Total de registros pré tratamento':<35}: {len(df):>10,}")
print(f"   {'Total de registros pós tratamento':<35}: {len(df_limpo):>10,}")
print(f"   {'Total de colunas pré tratamento':<35}: {df.shape[1]:>10}")
print(f"   {'Total de colunas pós tratamento':<35}: {df_limpo.shape[1]:>10}")
print(f"   {'Período dos dados':<35}: {df_limpo['DATA'].min().strftime('%d/%m/%Y')} → {df_limpo['DATA'].max().strftime('%d/%m/%Y')}")

print(f"\n LIMPEZA REALIZADA:")
print(f"   {'Colunas nulas removidas':<35}: {len(colunas_nulas):>10}")
print(f"   {'Duplicatas removidas':<35}: {duplicatas:>10}")
print(f"   {'Registros com Sem Categoria':<35}: {(df_limpo['PR_CAT'] == 'Sem Categoria').sum():>10,}")

print(f"\n ESTATÍSTICAS — CL_FHL (Nº de Filhos):")
print(f"   {'Média':<35}: {df_limpo['CL_FHL'].mean():>10.2f}")
print(f"   {'Mediana':<35}: {df_limpo['CL_FHL'].median():>10.2f}")
print(f"   {'Desvio Padrão':<35}: {df_limpo['CL_FHL'].std():>10.2f}")

print(f"\n CATEGORIAS DE PRODUTOS:")
print(f"   {'Categorias únicas':<35}: {df_limpo['PR_CAT'].nunique():>10}")

print(f"\n PERFIL DOS CLIENTES:")
print(f"   {'Clientes únicos':<35}: {df_limpo['CL_ID'].nunique():>10,}")
print(f"   {'% Feminino':<35}: {(df_limpo['CL_GENERO'] == 'F').mean()*100:>9.1f}%")
print(f"   {'% Masculino':<35}: {(df_limpo['CL_GENERO'] == 'M').mean()*100:>9.1f}%")

print("\n" + "=" * 60)
print("  Análise concluída com sucesso!")
print("=" * 60)


# --- Exportando o DataFrame Limpo ---
os.makedirs('output', exist_ok=True)
df_limpo.to_csv('output/df_limpo.csv', index=False, encoding='UTF-8')
print("\ndf_limpo.csv exportado para a pasta output/")
