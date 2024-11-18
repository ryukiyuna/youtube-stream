import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Display Image')

img = Image.open('1_o.jpg')

st.image(img, caption='STREET FIGHTER 6')


img = Image.open('l_yx_dq_05.jpg')

st.image(img, caption='DRAGON QUEST 3')