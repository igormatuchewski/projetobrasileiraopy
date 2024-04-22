# Importando as bibliotecas

import pandas as pd
import streamlit as st
import webbrowser as wb

# Configurando opções da página

st.set_page_config(
    page_title='Home',
    page_icon='https://cdn-icons-png.flaticon.com/512/53/53283.png',
    layout='wide'
)

# Diminuindo o tamanho do padding do streamlit
st.markdown("""
        <style>
               .block-container {
                    padding-top: 2rem;
                    padding-bottom: 0rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
        </style>
        """, unsafe_allow_html=True)

# Carregando os dados

# Verifica se 'data' não está na session_state ou se não é um DataFrame
if 'data' not in st.session_state or not isinstance(st.session_state['data'], pd.DataFrame):
    # Carrega o DataFrame a partir do arquivo CSV
    df = pd.read_csv('dataset/brasileirao.csv')
    # Armazena o DataFrame na session_state para uso posterior
    st.session_state['data'] = df
else:
    # Se 'data' já está na session_state e é um DataFrame válido, apenas o recupera
    df = st.session_state['data']

## Realizando alguns tratamentos e configurações para bases: 

# Renomeando colunas
df.rename(columns={
    'season' : 'temporada',
    'place' : 'colocacao',
    'acronym' : 'sigla',
    'team' : 'time',
    'points' : 'pontos',
    'played' : 'partidas_disputadas',
    'won' : 'vitorias',
    'draw' : 'empates',
    'loss' : 'derrotas',
    'goals_for' : 'gols_marcados',
    'goals_against' : 'gols_sofridos',
    'goals_diff' : 'saldo_gols'
}, inplace=True)

# Alterando tipo de dados de uma coluna
df['temporada'] = df['temporada'].astype('str')
df['temporada'].dtype

# Criando novas colunas
df['pontos_possiveis'] = df['partidas_disputadas'] * 3
df['aproveitamento(%)'] = ((df['pontos'] / df['pontos_possiveis']) * 100).round(2)
df['med_gols_marcados'] = (df['gols_marcados'] / df['partidas_disputadas']).round(2)
df['med_gols_sofridos'] = (df['gols_sofridos'] / df['partidas_disputadas']).round(2)

## Criando a tela:

st.title('Dados do Campeonato Brasileiro - 2003 ~ 2023')
st.sidebar.markdown('Feito por [Igor Matuchewski](https://www.linkedin.com/in/igor-matuchewski)')

btn = st.button('Clique aqui para acessar o Dataset!')
if btn:
    wb.open_new_tab('https://www.kaggle.com/datasets/lucasyukioimafuko/brasileirao-serie-a-2006-2022')

# st.markdown('Olá a todos, esse foi meu primeiro projeto criando dashboards com Python e suas bibliotecas Streamlit e Plotly Express, utilizei ainda o Pandas para realizar alguns tratamentos e manipulações. É incrível ver a capacidade e versatilidade do Python para desenvolver páginas interativas e com interface de usuário amigável, utilizando o Streamlit para adicionar filtros, gráficos e tabelas dinâmicos.')
# st.markdown('O Python oferece muita flexibilidade e controle, no entanto ferramentas como o PowerBI ainda são mais fáceis de aprender e tem uma curva de aprendizado extremamente mais rápida, especialmente para quem não é familiarizado com programação. No entanto, a combinação do Python com bibliotecas como Pandas, Streamlit e Plotly Express tornam o processo de desenvolvimento muito tranquilo e eficaz e fiquei satisfeito com o resultado obtido.')

st.markdown('Esse foi o meu primeiro projeto de Análise de Dados desenvolvido 100% via Python. Utilizei a biblioteca Pandas para realizar todos os tratamentos de dados necessários, assim como criação de novas colunas e manipulação de outros dataframes. Apliquei também o Streamlit, biblioteca extremamente poderosa para desenvolvimento de dashboards com a possibilidade de criar diversas páginas, filtros e milhares de outras funcionalidades. A outra biblioteca utilizada foi o Pyploy Express para gerar gráficos interativos e também conectá-los com os filtros, tornando a dashboard dinâmica.')
st.markdown('Considero o resultado obtido muito satisfatório, visto que foi o meu primeiro projeto que desenvolvi utilizando o Streamlit e o Pyplot Express, já havia utilizado o Pandas e o Matplotlib para realizar Análises Exploratórias. Apesar de ser fácil a compreensão e muito simples o desenvolvimento (comparado à outras linguagens de programação) considero o PowerBI ainda muito mais intuitivo e fácil de utilizar. É claro que conforme a utilização a velocidade de desenvolvimento também aumenta.')
st.markdown('Embora atualmente (março/2024) eu ainda considero que minha capacidade de desenvolvimento de dashboards via PowerBI seja mais rápida e completa, há de se destacar pontos relevantes em que o Python se destaca quando comparamos ao PowerBI:')
st.write('* Velocidade de leitura e processamento dos dados: quando trabalhamos com muitos dados conectados ao PowerBI e ainda mais, quando são tratados via Power Query, o carregamento e a visualização fica extremamente lenta, levando alguns segundos para carregar e, dependendo do tamanho do arquivo, até minutos;')
st.write('* Limitação de linhas: o PowerBI possui uma limitação de 1.048.576 linhas *(fonte: https://support.microsoft.com/pt-br/office/power-query-especifica%C3%A7%C3%B5es-e-limites-no-excel-5fb2807c-1b16-4257-aa5b-6793f051a9f4)* o que pode ser algo muito negativo dependendo do negócio que estamos trabalhando, algo que não existe no Python;')
st.write('* Liberdade de personalização: aqui nesse projeto fiz a utlilzação do Streamlit, nessa bilioteca em específico a customização não é o foco, se tornando menos customizável do que o PowerBI, no entanto, existe uma biblioteca chamada "dash" que é mais capaz nesse quesito e pode superar o PowerBI.')

st.markdown(' ')