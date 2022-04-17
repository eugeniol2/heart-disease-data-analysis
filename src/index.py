from numpy import sort
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

from app.dataExploration.data_exploration import data_exploration
# from app.preProcessing.pre_processing import pre_processing

ds = pd.read_csv('data/personal-key-indicators-of-heart-disease-dataset.csv')

optionsDict = {
  'Analise exploratória': 'exploratoryAnalysis',
  'Pré-processamento': 'preProcessing'
}

st.set_page_config(layout="wide")
with st.sidebar:
  selected = option_menu(
    menu_title='Menu Principal',
    options=['Pré-processamento', 'Analise exploratória'],
    icons=['gear-fill', 'bar-chart-fill'],
    menu_icon='cast',
    default_index=0,
  )

options = optionsDict[selected]
if options == 'preProcessing':
  # pre_processing()
  print('s')
if options == 'exploratoryAnalysis':
  data_exploration()
