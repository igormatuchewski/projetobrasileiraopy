import pandas as pd
import streamlit as st
import plotly.express as px

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


## Criando variáveis e gráficos caso o valor do filtro nao esteja vazio
if not df_filtrado.empty:
    # Gols marcados por ano
    gols_marcados_anos = df_filtrado.groupby('temporada')['gols_marcados'].sum()
    gols_marcados = df_filtrado['gols_marcados'].sum()
    med_gols_marcados_anos = gols_marcados_anos.mean().round(2)
    graf_gols_marcados = px.line(df_filtrado, x=gols_marcados_anos.index, y=gols_marcados_anos.values, title=f'Gols Marcados por Ano - Total: {gols_marcados}',
                                 labels={'x' : 'Temporada', 'y' : 'Qtd Gols Marcados'}, color_discrete_sequence=['#31eadb'])
    graf_gols_marcados.add_hline(y=med_gols_marcados_anos, line_dash='dash', line_color='yellow', annotation_text=f'Média: {med_gols_marcados_anos}/ano')
    # Gols sofridos por ano
    gols_sofridos_anos = df_filtrado.groupby('temporada')['gols_sofridos'].sum()
    gols_sofridos = df_filtrado['gols_sofridos'].sum()
    med_gols_sofridos_anos = gols_sofridos_anos.mean().round(2)
    graf_gols_sofridos = px.line(df_filtrado, x=gols_sofridos_anos.index, y=gols_sofridos_anos.values, title=f'Gols sofridos por Ano - Total: {gols_sofridos}',
                                 labels={'x' : 'Temporada', 'y' : 'Qtd Gols Sofridos'}, color_discrete_sequence=['#ff3838'])
    graf_gols_sofridos.add_hline(y=med_gols_sofridos_anos, line_dash='dash', line_color='yellow', annotation_text=f'Média: {med_gols_sofridos_anos}/ano')
    # Saldo de Gols por ano
    saldo_gols_anos = df_filtrado.groupby('temporada')['saldo_gols'].sum()
    saldo_gols = df_filtrado['saldo_gols'].sum()
    graf_saldo_anos = px.line(df_filtrado, x=saldo_gols_anos.index, y=saldo_gols_anos.values, title=f'Saldo de Gols por Ano',
                              labels={'x' : 'Temporada', 'y' : 'Saldo Gols'}, color_discrete_sequence=['#31eadb'])

    # Exibindo o titulo
    st.markdown('## Histórico de Gols por ano | Geral e por Time')

    # Exibindo os Gráficos
    col1, col2 = st.columns(2)
    col1.plotly_chart(graf_gols_marcados, use_container_width=True)
    col2.plotly_chart(graf_gols_sofridos, use_container_width=True)
    st.plotly_chart(graf_saldo_anos, use_container_width=True)

else:
    # Mensagem caso o filtro esteja vazio
    st.markdown('Por favor, selecione um ou mais times no filtro ou "Todos".')

st.sidebar.markdown('Feito por [Igor Matuchewski](https://www.linkedin.com/in/igor-matuchewski)')
