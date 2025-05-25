import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

data = pd.read_csv("Computos2006-Presidente.txt", sep="|")
print("Numero de entradas:", data.shape)
st.markdown("## Analisis de datos de las votaciones de 2006")
st.markdown("Primero cargamos los datos")
st.markdown(f"Número de entradas: {data.shape}")


idstate = {1: 'Aguascalientes', 2:'Baja California', 3: 'Baja California Sur', 4: 'Campeche',
 5: 'Coahuila', 6: 'Colima', 7: 'Chiapas', 8: 'Chihuahua', 9:'CDMX', 10: 'Durango',
 11: 'Guanajuato', 12: 'Guerrero', 13: 'Hidalgo', 14: 'Jalisco', 15: 'México',
 16: 'Michoacán', 17: 'Morelos', 18: 'Nayarit', 19: 'Nuevo León', 20: 'Oaxaca',
 21: 'Puebla', 22: 'Querétaro', 23: 'Quintana Roo', 24: 'San Luis Potosí',
 25: 'Sinaloa', 26: 'Sonora', 27: 'Tabasco', 28: 'Tamaulipas', 29: 'Tlaxcala',
 30: 'Veracruz', 31: 'Yucatán', 32: 'Zacatecas'} 

## Cambiar datos, ID_Estado a nombre del estado
data['ID_ESTADO'] = data['ID_ESTADO'].apply(lambda x: idstate[x]) 

data_10 = data.head(10)
st.table(data_10 ["ID_ESTADO"])

## Renombrar columna
data.rename(columns = {"ID_ESTADO" : "ESTADO"}, inplace=True) 

## Mostrar cuantos estados unicos hay
len(data['ESTADO'].unique())
st.markdown("## ¿Cuántos estados únicos hay?")
st.markdown(f"Hay {len(data['ESTADO'].unique())} estados únicos")
st.markdown("Con esto sabemos que hay votos en todos los estados") 

## Variables VotoExtranjero y VotoLocal
votoExtranjero = data[data["TIPO_CANDIDATURA"] == 6]
votoLocal = data[data["TIPO_CANDIDATURA"] == 1]
st.markdown("## Votos de candidatos al extranjero y locales")
st.markdown(f"Votos extranjeros: {votoExtranjero.shape[0]}")
st.markdown(f"Votos locales: {votoLocal.shape[0]}")

partidas = ["PAN", "PBT", "APM", "NA", "ASDC", "NO_VOTOS_VALIDOS", "NO_VOTOS_NULOS"]

suma_votos = votoLocal[partidas].sum() + votoExtranjero[partidas].sum()
suma_votos 
st.markdown("## Suma de votos")
st.markdown(f"Suma de votos: {suma_votos}")
st.table(suma_votos)

## Pocentajes de votos
porcentaje = (suma_votos / suma_votos.sum()) * 100
st.markdown("## Porcentajes de votos")
st.markdown(f"Porcentajes de votos: {porcentaje.round(2)}")
st.table(porcentaje.round(2))

## Gráfico de barras
porcentaje.plot(kind='bar', color='skyblue')
st.markdown("## Gráfico de barras de porcentajes de votos")
st.pyplot(plt)

st.markdown("## Gráfico de barras interactivo")
st.bar_chart(porcentaje)

data.isna().sum()
st.markdown("## Datos faltantes")
st.markdown(f"Datos faltantes: {data.isna().sum()}")
st.table(data.isna().sum())


