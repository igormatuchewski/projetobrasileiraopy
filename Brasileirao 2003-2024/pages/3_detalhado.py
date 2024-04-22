import pandas as pd
import streamlit as st

st.set_page_config(
    page_title='Visão Geral',
    page_icon='https://cdn-icons-png.flaticon.com/512/53/53283.png',
    layout='wide'
)

# Diminuindo o tamanho do padding do streamlit
st.markdown("""
        <style>
               .block-container {
                    padding-top: 1.5rem;
                    padding-bottom: 0rem;
                    padding-left: 3rem;
                    padding-right: 3rem;
                }
        </style>
        """, unsafe_allow_html=True)

df = st.session_state['data']

# Reordenando as colunas

df_reord = df[['temporada', 'time', 'partidas_disputadas', 'aproveitamento(%)', 'pontos_possiveis', 'pontos', 'vitorias', 'empates', 'derrotas', 'gols_marcados', 'gols_sofridos', 'saldo_gols']].sort_values(by='aproveitamento(%)', ascending = False)

## Criando filtro de time
time = sorted(df_reord['time'].unique()) # Convertendo a coluna 'time' em uma lista
time.insert(0, "Todos")  # Adicionando "Todos" como a primeira opção na lista
times_selecionados = st.sidebar.multiselect('Selecione o(s) time(s)', time, default=['Todos'])

## Criando filtro de temporada
temporadas = sorted(df_reord['temporada'].unique())
temporadas.insert(0, "Todas")  
temporada = st.sidebar.multiselect('Selecione uma temporada', temporadas, default='Todas')

# Aplicando os filtros
df_filtrado = df_reord.copy()
# Filtrando por time
if 'Todos' not in times_selecionados:
    df_filtrado = df_filtrado[df_filtrado['time'].isin(times_selecionados)]
# Filtrando por temporada
if 'Todas' not in temporada:
    df_filtrado = df_filtrado[df_filtrado['temporada'].isin(temporada)]


## Criando variaveis
# Média de partidas disputadas
qtd_participacoes = len(df_filtrado)
# Pontos possíveis
pts_poss = df_filtrado['pontos_possiveis'].sum()
# Pontos conquistados
pts_cnq = df_filtrado['pontos'].sum()
# Aproveitamento
aprv = (((df_filtrado['aproveitamento(%)'].sum()) / pts_poss) * 100).round(2)
# Total de gols marcados
gols_anotados = df_filtrado['gols_marcados'].sum()
# Total de gols sofridos
gols_tomados = df_filtrado['gols_sofridos'].sum()
# Saldo de gols
saldo_de_gols = gols_anotados - gols_tomados


# Exibindo titulo
st.markdown('## Valores Detalhados por time (2003-2023)')

# Adicionando valores
col1, col2 = st.columns(2)
col1.write(f'* Quantidade de Participações na Serie A: {qtd_participacoes}')
col2.write(f'* Quantidade de Gols Marcados: {gols_anotados}')

col3, col4 = st.columns(2)
col3.write(f'* Pontos possíveis: {pts_poss}')
col4.write(f'* Quantidade de Gols Sofridos: {gols_tomados}')

col5, col6 = st.columns(2)
col5.write(f'* Pontos possíveis: {pts_cnq}')
col6.write(f'* Saldo de Gols: {saldo_de_gols}')

col7, col8, col9 = st.columns(3)
col8.write(f'* <b> Aproveitamento:</b> {aprv}%', unsafe_allow_html=True)


# Exibindo a tabela
st.dataframe(df_filtrado)

st.sidebar.markdown('Feito por [Igor Matuchewski](https://www.linkedin.com/in/igor-matuchewski)')
