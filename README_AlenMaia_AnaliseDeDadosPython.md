
# ProjetoAedSemana07
Repositório criado para o mini projeto - Análise Exploratória de Dados - SCTEC

---

# 📊 Projeto Análise Exploratória de Dados — SEMANA 07 | SCTEC

## 🎯 Objetivo

Realizar uma análise exploratória completa da Base Varejo, aplicando técnicas de limpeza de dados, transformação de tipos, tratamento de nulos com lógica condicional (if/else), e geração de estatísticas descritivas. O projeto contempla todas as Sprints de desenvolvimento, desde a importação até o versionamento no GitHub.

---

## 📁 Estrutura do Projeto

PROJETO - AED - SEMANA 07 V.FINAL/
├── ProjetoAedSemana07/                    # 📦 Repositório GitHub
│   ├── output/
│   │   └── df_limpo.csv                   # Dados processados
│   ├── .gitignore                         # Arquivos ignorados pelo Git
│   ├── Análise exploratória.ipynb         # Notebook Jupyter
│   ├── Análise exploratória.py            # Script Python
│   ├── Base Varejo.csv                    # Dados brutos
│   ├── Projeto III - Análise Exploratória de Dados...pdf
│   ├── README.md                          # Documentação do projeto
│   └── requirements.txt                   # Dependências Python
│
└── venv/                                  # 🐍 Ambiente virtual (não sincronizar)

<<<<<<< HEAD
```
=======
>>>>>>> a465b2128f013dce87d106be9ea7fa31977168a1

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Versão | Descrição |
|------------|--------|-----------|
| **Python** | 3.x | Linguagem principal |
| **pandas** | ≥1.3 | Manipulação de dados (leitura, limpeza, transformação) |
| **numpy** | ≥1.20 | Operações numéricas e estatísticas |
| **matplotlib** | ≥3.3 | Criação de gráficos e visualizações |
| **seaborn** | ≥0.11 | Gráficos estatísticos avançados |
| **jupyter** | ≥1.0 | Notebook para execução interativa |

---

## 🚀 Como Executar o Projeto

### ✅ Pré-requisitos

- Python 3.7+ instalado
- Git instalado
- Acesso ao terminal/PowerShell

### 📥 Passo 1: Clonar o Repositório

```bash
git clone https://github.com/alen221188/ProjetoAedSemana07.git
cd ProjetoAedSemana07
```

### 🐍 Passo 2: Criar e Ativar o Ambiente Virtual

**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```cmd
python -m venv venv
venv\Scripts\activate.bat
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 📦 Passo 3: Instalar as Dependências

```bash
pip install -r requirements.txt
```

### ▶️ Passo 4: Executar o Projeto

**Opção A — Jupyter Notebook (RECOMENDADO):**
```bash
jupyter notebook "Análise exploratória.ipynb"
```

---

## 🚀 Sprints de Desenvolvimento

### ✅ Sprint 1 — Importação dos Dados

- ✓ Leitura do arquivo CSV (830.000 registros)
- ✓ Exploração inicial com `head()`, `tail()`, `sample()`
- ✓ Verificação de dimensões e tipos de dados
- ✓ Análise de valores nulos por coluna

### ✅ Sprint 2 — Transformação de Tipos

- ✓ Remoção de colunas completamente nulas
- ✓ Conversão DATA (str → datetime) usando módulo datetime
- ✓ Mapeamento de Estado Civil (int → str legível)
- ✓ Extração de ANO, MÊS, DIA a partir da data

### ✅ Sprint 3 — Limpeza de Nulos e Duplicatas

- ✓ Implementação de `if/else` para tratamento de PR_CAT
  - Tratamento de `#N/D` (erro Excel)
  - Tratamento de `NaN` (valores nulos)
  - Tratamento de strings vazias
- ✓ Validação da regra de negócio do CO_ID (número da nota fiscal)
- ✓ Identificação e remoção de **96.553 duplicatas**
- ✓ Justificativa das escolhas de limpeza

### ✅ Sprint 4 — Estatística Descritiva

- ✓ Cálculo de 12 parâmetros estatísticos da coluna CL_FHL (Nº de Filhos)
  - Contagem, Média, Mediana, Moda
  - Desvio Padrão, Variância
  - Mínimo, Máximo, Amplitude
  - Quartis (Q1, Q2, Q3)
- ✓ Exploração de padrões de agrupamento:
  - Gênero × Categoria
  - Segmento × Categoria
  - Ano × Categoria

### ✅ Sprint 5 — Relatório e Documentação

- ✓ Geração de relatório final no terminal
- ✓ Exportação do `df_limpo.csv`
- ✓ Finalização do README.md com reflexão teórica

### ✅ Sprint 6 — Versionamento

- ✓ Commit com mensagem descritiva
- ✓ Push para o repositório GitHub
- ✓ Envio do link no AVA

---

## 📈 Resultados da Análise

### 1️⃣ Base de Dados — Volume e Período

| Métrica | Valor |
|---------|-------|
| Total de registros (pré-tratamento) | 830.000 |
| Total de registros (pós-tratamento) | 733.447 |
| Total de colunas (pré-tratamento) | 14 |
| Total de colunas (pós-tratamento) | 13 |
| Período de análise | 04/01/2019 → 08/12/2022 |
| Clientes únicos | 1.000 |
| Produtos únicos | 229 |
| Categorias únicas | 7 |

### 2️⃣ Limpeza Realizada — Impacto dos Tratamentos

| Processo | Quantidade | Percentual |
|----------|------------|------------|
| Colunas nulas removidas | 4 | — |
| Duplicatas removidas | 96.553 | 11,6% |
| Registros com "Sem Categoria" | 3.228 | 0,4% |
| Registros mantidos | 733.447 | 88,4% |

#### 💡 Insight Crítico

A remoção de **96.553 duplicatas** (11,6% do dataset) foi essencial. Esses registros duplicados poderiam:

- Enviesar análises de frequência
- Subestimar o número real de transações únicas
- Distorcer métricas de comportamento de clientes

### 3️⃣ Perfil dos Clientes

#### Distribuição por Gênero

| Gênero | Percentual | Quantidade |
|--------|------------|------------|
| 👩 Feminino | 52,1% | ~521 clientes |
| 👨 Masculino | 47,9% | ~479 clientes |

#### Estatísticas — Número de Filhos (CL_FHL)

| Parâmetro | Valor |
|-----------|-------|
| Média | 1,15 filhos |
| Mediana | 0,00 filhos |
| Desvio Padrão | 1,42 |
| Mínimo | 0 filhos |
| Máximo | 3+ filhos |

**📌 Interpretação:**

- População equilibrada entre gêneros (52% F / 48% M)
- Maioria dos clientes tem 0 filhos (mediana = 0)
- Alguns poucos têm muitos filhos (desvio padrão = 1,42)
- Essa variabilidade indica mercado diverso com diferentes perfis de família

### 4️⃣ Distribuição de Compras por Categoria

#### 🏆 Categoria Dominante: ALIMENTOS

| Aspecto | Detalhes |
|---------|----------|
| Compras | 384.197 |
| Percentual | 52,4% |
| Posição | 1ª categoria mais vendida |
| Impacto | Mais da metade de todas as compras |
| Conclusão | Alimentos é o **core business** da loja |

#### Top 5 Categorias

| Ranking | Categoria | Compras | % |
|---------|-----------|---------|---|
| 🥇 1º | ALIMENTOS | 384.197 | 52,4% |
| 🥈 2º | HIGIENE | 137.702 | 18,8% |
| 🥉 3º | LIMPEZA | 128.632 | 17,5% |
| 4º | BEBIDAS | 38.264 | 5,2% |
| 5º | PET | 28.553 | 3,9% |

**💡 Insight:**

- 88,7% do volume está em apenas **3 categorias**
- BEBIDAS (5,2%) e PET (3,9%) têm oportunidade de crescimento
- Essas categorias podem ser estratégicas para aumento de ticket médio

### 5️⃣ Distribuição de Compras por Segmento Econômico

#### 🏆 Segmento Mais Comprador: SEGMENTO B

| Aspecto | Detalhes |
|---------|----------|
| Posição | 1º segmento em volume |
| Compras | 468.505 |
| Percentual | 63,9% |
| Impacto | Quase 2/3 de todas as compras |
| Conclusão | Mercado-alvo primário definido |

#### Distribuição por Segmento

| Ranking | Segmento | Compras | % | Análise |
|---------|----------|---------|---|---------|
| 🥇 1º | Segmento B | 468.505 | 63,9% | Mercado principal |
| 🥈 2º | Segmento C | 205.265 | 28,0% | Mercado secundário |
| 🥉 3º | Segmento A | 59.677 | 8,1% | Baixa penetração |

**💡 Insight de Negócio:**

- Classe média é absolutamente dominante (63,9%)
- Classe alta tem penetração muito baixa (8,1%)
- **Oportunidade:** Expandir produtos premium para Segmento A
- **Risco:** Dependência excessiva do Segmento B

### 6️⃣ Produto Mais Vendido

#### 🏆 Top 1 — Produto Líder: PRESUNTO COZIDO

| Aspecto | Detalhes |
|---------|----------|
| Compras | 12.719 |
| Percentual | 1,7% |
| Categoria | ALIMENTOS |
| Posição | 1º produto mais vendido |
| Market Share | 1,7% do total |

#### Top 10 Produtos Mais Vendidos

| Ranking | Produto | Compras | % |
|---------|---------|---------|---|
| 1 | PRESUNTO COZIDO | 12.719 | 1,7% |
| 2 | SARDINHA | 6.610 | 0,9% |
| 3 | BANANA | 6.518 | 0,9% |
| 4 | ESCOVA DE DENTE | 6.518 | 0,9% |
| 5 | GEL | 6.517 | 0,9% |
| 6 | PAPINHA INFANTIL | 6.515 | 0,9% |
| 7 | MODELADOR | 6.505 | 0,9% |
| 8 | CERA | 6.502 | 0,9% |
| 9 | LIMPADOR PERFUMADO | 6.501 | 0,9% |
| 10 | CEBOLA | 6.501 | 0,9% |

**📌 Interpretação:**

- Mercado **altamente fragmentado** e diversificado
- Presunto Cozido lidera com apenas 1,7% — **nenhum "super-produto"**
- Produtos 2-10 têm participação similar (0,9% cada)
- **Indicativo:** Necessário mix diversificado para atrair clientes
- **Conclusão:** Nenhum produto é crítico ao negócio — não há dependência extrema

### 7️⃣ Resumo Executivo — Números-Chave

```
📊 VOLUME TOTAL DE TRANSAÇÕES
   Pré-tratamento:   830.000
   Pós-tratamento:   733.447
   ↓ Redução: 96.553 registros (11,6%)

🏬 BASE DE CLIENTES
   Total: 1.000 clientes únicos
   Distribuição: 52,1% F / 47,9% M

📦 PORTFÓLIO
   Produtos: 229 únicos
   Categorias: 7 principais
   Maior: ALIMENTOS (52,4%)

💰 MERCADO
   Segmento primário: B (63,9%)
   Segmento secundário: C (28,0%)
   Segmento oportunidade: A (8,1%)

🛍️ PRODUTO LÍDER
   PRESUNTO COZIDO: 12.719 vendas (1,7%)
```

---

## 💡 Reflexão Teórica

### 1. Importância da Limpeza de Dados — Impacto Real

Na prática, aproximadamente **11,6% do dataset** (96.553 registros) era duplicado. Este projeto demonstrou que:

- Dados brutos sempre contêm inconsistências (`#N/D`, valores nulos, duplicatas, tipos incorretos)
- A limpeza inadequada compromete dramaticamente as análises posteriores
- Se não tivéssemos removido as duplicatas:
  - Teríamos subestimado o número real de transações únicas
  - Superestimaríamos o volume de vendas por cliente
  - Métricas de comportamento ficariam distorcidas
- **Documentar por que removemos dados é tão importante quanto remover**

### 2. if/else vs. replace() — Quando e Por quê?

Durante o desenvolvimento, testamos ambas abordagens e descobrimos que:

- `if/else` com `apply()` permite verificar **múltiplas condições simultaneamente**
- Oferece **maior controle lógico e flexibilidade**
- Facilita **documentação e manutenção** do código
- É essencial para casos complexos (nulos, strings vazias, valores especiais)

**Exemplo prático:**

```python
# ❌ Insuficiente — não trata todos os casos
df['PR_CAT'].replace('#N/D', 'Sem Categoria')

# ✅ Completo — trata múltiplas condições
def tratar_categoria(valor):
    if pd.isna(valor) or valor == "#N/D" or valor == "":
        return "Sem Categoria"
    return valor

df['PR_CAT'] = df['PR_CAT'].apply(tratar_categoria)
```

### 3. Datetime — Mais que uma simples string

Converter DATA de string para datetime foi crucial pois:

- Permite **cálculos entre datas** (duração, intervalos)
- Facilita **filtragens por período específico** (04/01/2019 a 08/12/2022 = ~3 anos)
- Habilita **análises de série temporal**
- Reduz **uso de memória** (datetime é mais eficiente que string)

### 4. Padrões de Agrupamento Revelam Comportamentos

Os agrupamentos por Gênero × Categoria, Segmento × Categoria e Ano × Categoria mostraram que:

- Diferentes segmentos têm **preferências distintas**
  - Segmento B domina em ALIMENTOS
  - Segmento A prefere categorias premium
- Gênero **influencia nas escolhas de produtos**
  - Mulheres: maior volume em HIGIENE
  - Homens: maior volume em BEBIDAS e PET
- **Padrões mudaram ao longo dos anos** (2019-2022)
  - Crescimento de produtos PET
  - Aumento de HIGIENE (pós-pandemia)
- **Dados limpos revelam padrões; dados sujos ocultam realidades**

### 5. Estatística Descritiva ≠ Análise Inferencial

Neste projeto, focamos em **estatística descritiva** (descrever os dados que temos), não em **inferência** (extrapolar para populações).

| Conceito | Aplicação | Insight |
|----------|-----------|---------|
| Média vs. Mediana | Filhos: Média=1,15 / Mediana=0 | Maioria tem 0 filhos, poucos têm muitos |
| Desvio Padrão | 1,42 filhos | Alta variabilidade — mercado diverso |
| Quartis | Dividem dados em 4 partes | Úteis para boxplots e outliers |

---

## 🛠️ Desafios Enfrentados e Soluções

| Desafio | Solução Implementada | Resultado |
|---------|----------------------|-----------|
| 96.553 duplicatas | `.drop_duplicates()` após análise | 11,6% de redução validada |
| Nulos em PR_CAT | `if/else` com lógica condicional | Tratamento robusto de 3.228 registros |
| Tipos mistos (str/int/float) | `astype()`, `map()`, `pd.to_datetime()` | Conversão 100% bem-sucedida |
| DATA como string | `pd.to_datetime(dayfirst=True)` | Suporte a formato brasileiro DD/MM/YYYY |
| 830k registros = lentidão | Operações vetorizadas (Pandas) | Processamento eficiente, sem loops |
| Padrões ocultos em brutos | `groupby()` e `pivot_table()` | Revelação de insights estratégicos |
| Valores especiais (#N/D) | Mapeamento customizado | Categorização consistente |

---

## 📚 Conceitos de Data Science Aplicados

- **EDA (Exploratory Data Analysis):** Entender dados antes de análises
- **Data Cleaning:** Preparar dados para análise (remoção de duplicatas, tratamento de nulos)
- **Feature Engineering:** Criação de novas colunas (ANO, MÊS, DIA a partir de DATA)
- **Descriptive Statistics:** Resumir características (média, mediana, desvio padrão)
- **Groupby Operations:** Agregar dados por múltiplas dimensões

---

## 🎯 Aprendizados sobre o Negócio

### 📊 Mercado Concentrado

- Segmento B é dominante (63,9%)
- Classe A tem penetração baixa (8,1%)
- **Oportunidade:** Desenvolver linha premium para Segmento A

### 🛒 Alimentos é Core Business

- 52,4% das vendas
- Categoria estratégica
- **Recomendação:** Manter abastecimento prioritário

### 📦 Mercado Diversificado

- Presunto Cozido (1º) = 1,7% do total
- Top 10 produtos = ~9,7% do total
- **Conclusão:** Necessário mix diversificado, sem dependência extrema

### 🚀 Potenciais de Crescimento

- **BEBIDAS** (5,2%) — abaixo de categorias adjacentes
- **PET** (3,9%) — categoria emergente
- **Segmento A** (8,1%) — mercado não explorado

---

## ✨ Conclusão

Este projeto, apesar de quase me deixar louco, pois fiquei um dia inteiro lutando contra o VSCODE e GITHUB, exemplifica um **pipeline completo de análise de dados**: desde a importação bruta, passando pela limpeza e transformação, até a geração de insights estratégicos. A remoção sistemática de inconsistências (11,6% do dataset) e a análise descritiva revelaram que:

1. **Não existe análise de dados sem consumo excessivo de cafeína**
2. **Fazer análise de dados enquanto assiste o jogo do Brasil pode distrair o analista, não recomendo**
3. **O negócio depende da Classe Média** (63,9% do volume)
4. **Alimentos é fundamental** (52,4% das vendas)
5. **Há oportunidades em segmentos premium e categorias emergentes** (PET, Bebidas)
6. **A base de clientes é diversificada** (1.000 clientes, 229 produtos)
