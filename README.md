# ⚡ ONS Energy Generation Analyzer — Análise Horária de Geração (Fevereiro/2026)

Este projeto consiste em uma ferramenta interativa em Python para leitura, agregação e visualização da **geração horária de energia elétrica no Brasil**, utilizando os dados abertos oficiais do **ONS (Operador Nacional do Sistema Elétrico)** referentes a fevereiro de 2026.

A aplicação permite consultar qualquer dia do mês disponível na base e gera instantaneamente um gráfico de barras detalhado com os megawatts (MW) gerados a cada hora (00h às 23h).

---

## 📌 Destaques do Projeto

- **Otimização de Desempenho**: Carregamento e tratamento inicial da base de dados (`.xlsx`) realizados uma única vez na inicialização, permitindo consultas instantâneas no loop de navegação.
- **Interface Interativa CLI**: Navegação via terminal com validação de entradas, tratamento de erros e suporte a maiúsculas/minúsculas.
- **Visualização de Dados**: Gráficos claros com `matplotlib`, contendo rótulos de dados (*data labels*), grid auxiliar e formatação dinâmica de títulos.
- **Tratamento de Exceções**: Proteção contra arquivos ausentes (`FileNotFoundError`) e entradas inválidas do usuário.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Pandas**: Manipulação de dados, agrupamentos (`groupby`) e tratamento temporal (`to_datetime`).
- **Matplotlib**: Renderização do painel gráfico interativo.
- **OpenPyXL**: Engine de leitura de arquivos `.xlsx`.

---

## 📂 Estrutura do Repositório

```text
├── dados/
│   └── GERACAO_USINA-2_2026_02.xlsx   # Base de dados oficial do ONS
├── analise_geracao_ons.py             # Script Python interativo principal
└── README.md                           # Documentação do repositório

##  Estrutura da Base de Dados
A base do ONS contém as seguintes informações chave analisadas pelo script:
din_instante: Data e hora da medição.

nom_subsistema: Região do subsistema elétrico (Norte, Nordeste, Sudeste/Centro-Oeste, Sul).

nom_usina: Nome da usina geradora.

nom_tipousina: Fonte de energia (Hidrelétrica, Termelétrica, Eólica, Fotovoltaica).

val_geracao: Quantidade de energia gerada em Megawatts (MW).
