import streamlit as st
from controller.controller import ControladorSupermercado

def main(caminho): 
    controlador = ControladorSupermercado(caminho)
    controlador.modelo.criar_coluna_mes()
    
    mes_radio = st.sidebar.radio("Selecione o mês (Radio)", controlador.modelo.df["Mes"].unique())
    
    mes_selectbox = st.sidebar.selectbox("Selecione o mês (Selectbox)", controlador.modelo.df["Mes"].unique())
    
    mes_multiselect = st.sidebar.multiselect("Selecione o mês (Multiselect)", controlador.modelo.df["Mes"].unique(), default=controlador.modelo.df["Mes"].unique()[0])
    
    meses = controlador.modelo.df["Mes"].unique()
    mes_slider = st.sidebar.slider("Selecione o mês (Slider)", 0, len(meses)-1, 0)
    mes_selecionado_slider = meses[mes_slider]
    
    # Apresentar resultados dos widgets
    st.write("### Resultados da seleção")
    st.write(f"Mês selecionado no Radio: {mes_radio}")
    st.write(f"Mês selecionado no Selectbox: {mes_selectbox}")
    st.write(f"Mês selecionado no Multiselect: {mes_multiselect}")
    st.write(f"Mês selecionado no Slider: {mes_selecionado_slider}")
    
    # Executar controlador com um dos meses selecionados (você pode escolher qual usar)
    controlador.executar(mes_radio)  # ou mes_selectbox, mes_multiselect[0], mes_selecionado_slider

if __name__ == "__main__":
    st.set_page_config(page_title="Exemplo Final", page_icon="😊", layout="wide")
    main("./assets/supermarket_sales.csv")
