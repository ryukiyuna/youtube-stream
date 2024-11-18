import streamlit as st
import numpy as np
import pandas as pd

st.title('Streamlit 超入門')

df = pd.DataFrame({
    '1列目':[1,2,3,4],
    '2列目':[10,20,30,40]
})

'''動的な表（ソートとかできる）----------------------------------------------------'''
st.write('DataFrame')
# st.write(df)
'''
表の表示
writeでも表示できるが、dataframeは、引数を付けることができる
'''
# st.dataframe(df, width=500, height=100)
st.dataframe(df.style.highlight_max(axis=0), width=500, height=300)

'''静的な表（ソートとかできない）-------------------------------------------------'''
st.write('table')

st.table(df.style.highlight_max(axis=0))

'''Json表示'''
st.json(
    {
        "party1": "1st party",
        "member": ["Hero", "Fighter", "Priest", "Witch"],

    }
)

"""
# 章
## 節
### 項

'''python
import streamlit as st
import numpy as np
import pandas as pd
'''
"""
