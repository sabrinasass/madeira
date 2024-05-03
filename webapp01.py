import streamlit as st
import pandas as pd
from Massaki01 import *

MKD(Versao(), 'left', 18, 'blue')
   
MKD('⬜ Massaki01 - Biblioteca teste', 'left', 48, 'darkblue')
   
Escrever('Biblioteca teste para facilitar o desenvolvimento de sites a qualquer pessoa leiga na Programação.', 'subcabecalho')
Escrever(' ')
Escrever('Observação: Em desenvolvimento!', 'subcabecalho')
CONTAINER = Container(True)
with CONTAINER: 
        MKD('Biblioteca teste para facilitar o desenvolvimento de sites a qualquer pessa leiga na Programação.', "justified", 20, "black")
