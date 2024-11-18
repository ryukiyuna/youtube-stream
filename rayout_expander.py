import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')

st.write('インタラクティブなウィジェット')

#エキスパンダー・・・降りたたみ表示
expander = st.expander('レジュメ')
expander.write('part1')
expander.write('part2')
expander.write('part3')
expander.write('part4')
expander.write('part5')