import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time #プログレスバーに必要

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')

'Start!'
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.01)

'Done!'