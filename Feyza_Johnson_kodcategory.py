
import pandas as pd
import streamlit as st
import base64


st.title("THIS MONTH'S BIGGEST SELLERS")
st.markdown('YOU MIGHT LIKE THESE!')

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


df = pd.read_csv('reco_demo.csv')
is_check = st.checkbox("Display Data")
if is_check:
    st.write(df.head())
chart_df=pd.DataFrame(df.head(50), columns=('weight','category_name'))
option = st.sidebar.radio(
            'Choose the graph you want to see',
            ['Quit','Bar Chart','Line Chart'])
if option=='Quit':
    st.sidebar.write('Charts will be shown here')
elif option=='Bar Chart':
    st.bar_chart(df['business_unit'].head(50))
else:
    st.line_chart(df.value_counts())
class recofirst():

    j=0
    k=0
    for i in df['ImageLink'].head():

        st.image(i, caption=df['category_name'].iloc[:5][j]+' '+str(df['price'].iloc[:5][k])+'TL', use_column_width=True)
        j=j+1
        k=k+1


recofirst()

