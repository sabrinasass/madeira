import streamlit as st
import pandas as pd
from Massaki01 import *

MKD(Versao(), 'left', 18, 'blue')
   
MKD('⬜ Barra_Lateral_Texto', 'left', 48, 'darkblue')
   
Escrever('Esta função permite adicionar alguns elementos de texto com estilos específicos na Barra Lateral.', 'subcabecalho')
Escrever(' ')
Escrever('Observação: ', 'subcabecalho')
CONTAINER = Container(True)
with CONTAINER: 
        MKD('Biblioteca teste para facilitar o desenvolvimento de sites a qualquer pessa leiga na Programação.', "justified", 20, "black")
