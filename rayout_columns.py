import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')

st.write('インタラクティブなウィジェット')

img = Image.open('1_o.jpg')

img2 = Image.open('l_yx_dq_05.jpg')

#２カラムにする場合
col1, col2 = st.columns(2)
col1.image(img, caption='STREET FIGHTER 6')
col2.image(img2, caption='DRAGON QUEST 3')