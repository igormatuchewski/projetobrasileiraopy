import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(
    page_title='Geral',
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

## Criando um novo dataframe com todos os valores somados:
df_b = df.groupby('time')[['partidas_disputadas', 'pontos_possiveis', 'pontos', 'vitorias', 'empates', 'derrotas', 'gols_marcados', 'gols_sofridos', 'saldo_gols']].sum().reset_index().sort_values(by='pontos', ascending = False)

# Criando colunas Media de Gols Marcados, Media de Gols Sofridos e aproveitamento
df_b['med_gols_marcados'] = (df_b['gols_marcados'] / df_b['partidas_disputadas']).round(2)
df_b['med_gols_sofridos'] = (df_b['gols_sofridos'] / df_b['partidas_disputadas']).round(2)
df_b['aproveitamento(%)'] = ((df_b['pontos'] / df_b['pontos_possiveis']) * 100).round(2)

# Criando o dataframe geral com as colunas reordenadas
df_geral = df_b.groupby('time')[['partidas_disputadas', 'aproveitamento(%)', 'pontos_possiveis', 'pontos', 'vitorias', 'empates', 'derrotas', 'gols_marcados', 'gols_sofridos', 'saldo_gols', 'med_gols_marcados', 'med_gols_sofridos']].sum().reset_index().sort_values(by='pontos', ascending = False)

### Criando filtros
## Criando filtro de time
times = sorted(df_geral['time'].unique()) # Convertendo a coluna 'time' em uma lista
times.insert(0, "Todos")  # Adicionando "Todos" como a primeira opção na lista
times_selecionados = st.sidebar.multiselect('Selecione o(s) time(s)', times, default=['Todos'])

## Criando filtro de Qtd de Partidas Disputadas
# Definindo o valor minimo e maximo de partidas
min_partidas = int(df_geral['partidas_disputadas'].min())
max_partidas = int(df_geral['partidas_disputadas'].max())
qtd_partidas = st.sidebar.slider('Quantidade de Partidas', min_partidas, max_partidas, (min_partidas, max_partidas))

## Criando filtro de Aproveitamento
# Definindo o valor minimo e maximo de partidas
min_aproveitamento = float(df_geral['aproveitamento(%)'].min())
max_aproveitamento = float(df_geral['aproveitamento(%)'].max())
aproveitamento = st.sidebar.slider('Aproveitamento(%)', min_aproveitamento, max_aproveitamento, (min_aproveitamento, max_aproveitamento))

# Aplicando os filtros
df_filtrado = df_geral.copy()
# Filtrando por time
if 'Todos' not in times_selecionados:
    df_filtrado = df_filtrado[df_filtrado['time'].isin(times_selecionados)]
# Filtrando por quantidade de partidas
df_filtrado = df_filtrado[(df_filtrado['partidas_disputadas'] >= qtd_partidas[0]) & (df_filtrado['partidas_disputadas'] <= qtd_partidas[1])]
# Filtrando por aproveitamento
df_filtrado = df_filtrado[(df_filtrado['aproveitamento(%)'] >= aproveitamento[0]) & (df_filtrado['aproveitamento(%)'] <= aproveitamento[1])]


## Criando variáveis e Gráficos caso o valor do filtro não esteja vazio
if not df_filtrado.empty:
    # Nome do time e Maior Média de Gols
    maior_media = df_filtrado['med_gols_marcados'].max()
    time_maior_media = df_filtrado.loc[df_filtrado['med_gols_marcados'].idxmax(), 'time']
    # Nome do time e Maior Média de Gols
    menor_media = df_filtrado['med_gols_sofridos'].min()
    time_menor_media = df_filtrado.loc[df_filtrado['med_gols_sofridos'].idxmin(), 'time']
    # Quantidade de Times
    qtd_times = df_filtrado['time'].value_counts().count()
    # Gráfico de Aproveitamento por Time
    df_filtr_aprov_ord = df_filtrado.sort_values(by='aproveitamento(%)', ascending=False)
    apr_time = px.bar(df_filtr_aprov_ord, x='time', y='aproveitamento(%)', color_discrete_sequence=['#2093db'], labels={'time' : 'Time', 'aproveitamento(%)' : 'Aproveitamento(%)'}, title='Aproveitamento x Time')
    apr_time.update_layout(xaxis_tickangle=-45, bargap=0.3)
    # Gráficos de Partidas Disputadas
    df_filtr_part_ord = df_filtrado.sort_values(by='partidas_disputadas', ascending=False)
    part_time = px.bar(df_filtr_part_ord, x='time', y='partidas_disputadas', color_discrete_sequence=['#31eadb'], labels={'time' : 'Time', 'partidas_disputadas' : 'Partidas Disputadas'}, title='Partidas Disputadas x Time')
    part_time.update_layout(xaxis_tickangle=-45, bargap=0.3)

    # Gráfico de Gols Marcados e Sofridos x Time
    df_filtr_saldo_ord = df_filtrado.sort_values(by='saldo_gols', ascending=True)
    saldo_gols = px.bar(df_filtr_saldo_ord, x='saldo_gols', y='time', orientation='h', color=df_filtr_saldo_ord['saldo_gols'] < 0, color_discrete_map={False: '#2093db', True: '#ff3838'},
                        labels={'saldo_gols' : 'Saldo de Gols', 'time' : 'Time'}, title='Saldo de Gols x Time')
    saldo_gols.update_layout(showlegend=False, bargap=0.3)

    # Exibindo a tabela
    st.markdown('## Valores Gerais por Time (2003-2023)')
    st.dataframe(df_filtrado)

    # Gráficos
    st.markdown('## Gráficos')
    col1, col2 = st.columns(2)
    col1.plotly_chart(apr_time, use_container_width=True)
    col2.plotly_chart(part_time, use_container_width=True)


    st.plotly_chart(saldo_gols, use_container_width=True)
else:
    # Mensagem caso o filtro esteja vazio
    st.markdown('Por favor, selecione um ou mais times no filtro ou "Todos".')

st.sidebar.markdown('Feito por [Igor Matuchewski](https://www.linkedin.com/in/igor-matuchewski)')
