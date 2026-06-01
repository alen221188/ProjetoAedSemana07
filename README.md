# ProjetoAedSemana07
Repositório criado para o mini projeto - Análise Exploratória de Dados - SCTEC
# 📊 Projeto Análise Exploratória de Dados. SEMANA 07 | SCTEC 

## 🎯 Objetivo
Realizar uma análise exploratória completa da Base Varejo, aplicando técnicas de limpeza de dados, transformação de tipos, tratamento de nulos com lógica condicional (if/else), e geração de estatísticas descritivas. O projeto contempla todas as Sprints de desenvolvimento, desde a importação até o versionamento no GitHub.

---

## 📁 Estrutura do Projeto
ProjetoAedSemana07/
│
├── 📄 Análise exploratória.py ← Script Python puro
├── 📓 Análise exploratória.ipynb ← Notebook Jupyter (recomendado)
├── 📋 README.md ← Este arquivo
├── 📊 Base Varejo.csv ← Base de dados bruta (830k registros)
├── 📑 Projeto III - Analise...pdf ← Documento explicativo da base de dados
├── 📦 requirements.txt ← Dependências do projeto
│
├── venv/ ← Ambiente virtual Python
│ ├── etc/
│ ├── include/
│ ├── Lib/
│ ├── Scripts/
│ ├── share/
│ ├── .gitignore
│ └── pyvenv.cfg
│
└── .gitignore ← Configuração Git

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Versão | Descrição |
|-----------|--------|-----------|
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
git clone https://github.com/SEU_USUARIO/ProjetoAedSemana07.git
cd ProjetoAedSemana07

🐍 Passo 2: Criar e Ativar o Ambiente Virtual

Windows (PowerShell):
python -m venv venv
.\venv\Scripts\Activate.ps1

Windows (CMD):

bash
python -m venv venv  
venv\Scripts\activate.bat 

macOS/Linux:

bash
python3 -m venv venv  
source venv/bin/activate

📦 Passo 3: Instalar as Dependências
pip install -r requirements.txt

▶️ Passo 4: Executar o Projeto
Opção A — Jupyter Notebook (RECOMENDADO):
jupyter notebook "Análise exploratória.ipynb"

📊 Sprints de Desenvolvimento

✅ Sprint 1 — Importação dos Dados
✓ Leitura do arquivo CSV (830.000 registros)
✓ Exploração inicial com head(), tail(), sample()
✓ Verificação de dimensões e tipos de dados
✓ Análise de valores nulos por coluna

✅ Sprint 2 — Transformação de Tipos
✓ Remoção de colunas completamente nulas
✓ Conversão DATA (str → datetime) usando módulo datetime
✓ Mapeamento de Estado com dicionário Civil (int → str legível)
✓ Extração de ANO, MÊS, DIA a partir da data

✅ Sprint 3 — Limpeza de Nulos e Duplicatas
✓ Implementação de if/else para tratamento de PR_CAT
Tratamento de #N/D 
Tratamento de NaN 
Tratamento de strings vazias
✓ Validação da regra de negócio do CO_ID (número da nota fiscal)
✓ Identificação e remoção de duplicatas
✓ Justificativa das escolhas de limpeza

✅ Sprint 4 — Estatística Descritiva
✓ Cálculo de 12 parâmetros estatísticos da coluna CL_FHL (Nº de Filhos):
Contagem, Média, Mediana, Moda
Desvio Padrão, Variância
Mínimo, Máximo
Quartis (Q1, Q2, Q3)
Amplitude
Gênero × Categoria
Segmento × Categoria
Ano × Categoria

✅ Sprint 5 — Relatório e Documentação
✓ Geração de relatório final no terminal
✓ Exportação do df_limpo.csv
✓ Finalização do README.md com reflexão teórica

✅ Sprint 6 — Versionamento
✓ Commit com mensagem descritiva
✓ Push para o repositório GitHub
✓ Envio do link no AVA

📈 Resultados Principais
📊 Base de Dados:
   Total de registros                 :    733,447
   Total de colunas                   :         13
   Período dos dados                  : 04/01/2019 → 08/12/2022

 LIMPEZA REALIZADA:
   Colunas nulas removidas            :          4
   Duplicatas removidas               :          0
   Registros com Sem Categoria        :      3,228

 ESTATÍSTICAS — CL_FHL (Nº de Filhos):
   Média                              :       1.15
   Mediana                            :       0.00
   Desvio Padrão                      :       1.42

 CATEGORIAS DE PRODUTOS:
   Categorias únicas                  :          7

 PERFIL DOS CLIENTES:
   Clientes únicos                    :      1,000
   % Feminino                         :      52.1%
   % Masculino                        :      47.9%