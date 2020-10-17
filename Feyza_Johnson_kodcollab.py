import streamlit as st
import pandas as pd
import base64
from surprise import Reader, Dataset, KNNBaseline
from surprise.model_selection import cross_validate
from surprise.model_selection import train_test_split
"""
#  RECOMMENDED FOR YOU
"""
@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    body {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str

    st.markdown(page_bg_img, unsafe_allow_html=True)
    return
set_png_as_page_bg('backgroundty.JPG')

df=pd.read_csv('better_reco.csv')

is_check=st.checkbox('Display Data')
if is_check:
    st.write(df)
j=0
for i in df['ImageLink'].head(7):
    st.image(i, caption=('recommended for you'+' '+str(df['Unnamed: 0'][j])+' '), use_column_width=True)
    j=j+1
