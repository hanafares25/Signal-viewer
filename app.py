import streamlit as st
from PIL import Image 

st.set_page_config(page_title= "DSP", page_icon=":ghost:", layout="wide")



    st.title("Digital Signal Processing")
    st.write("Signal viewer Task 1")
    st.write("[Task 1 >](https://github.com/hanafares25/Signal-viewer.git)")



#--- more data ------
with st.container():
    st.write("---")
    left_column, right_column= st.columns(2)
    with left_column:
        
