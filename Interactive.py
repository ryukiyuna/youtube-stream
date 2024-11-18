import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')

st.write('インタラクティブなウィジェット')

#チェックボックス・・・チェック有り=true, チェック無し=false
if st.checkbox('Show Image'):
    img = Image.open('l_yx_dq_05.jpg')
    st.image(img, caption='DRAGON QUEST 3')

#セレクトボックス・・・C#のコンボボックス、ドロップダウンリスト
option = st.selectbox(
    'あなたが好きな数字を教えてください',
    list(range(1, 11))
)
'あなたの好きな数字：', option

#テキスト入力
text = st.text_input('あなたの趣味を教えてください。')
'あなたの趣味：', text

#スライダー
condition =  st.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション：', condition