import streamlit as st
import numpy as np
import pandas as pd

st.title('Streamlit 超入門 ～チャート～')

df = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)

'''折れ線グラフ'''
st.line_chart(df)

'''エリアチャート'''
st.area_chart(df)

'''バーチャート'''
st.bar_chart(df)



