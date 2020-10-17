import streamlit as st
import pandas as pd
from spacy.lang.tr.stop_words import STOP_WORDS as tr_stop
from spacy.lang.en.stop_words import STOP_WORDS as en_stop
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import base64
"""
#  YOU MIGHT LIKE THESE TOO
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

df=pd.read_csv('reco_demo.csv')
final_stopwords_list = list(tr_stop) + list(en_stop)
tfidf = TfidfVectorizer(stop_words=final_stopwords_list)
tfidf_matrix = tfidf.fit_transform(df['detailed_description'])
count = CountVectorizer(stop_words=final_stopwords_list)
count_matrix = count.fit_transform(df['detailed_description'])
cosine_sim = cosine_similarity(count_matrix, count_matrix)
df = df.reset_index()
indices = pd.Series(df.index, index=df['category_name'])
def get_recommendations(category_name, cosine_sim=cosine_sim):
        # Get the index of the product that matches the category_name
        idx = indices[category_name]

        # Get the pairwsie similarity scores
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        sim_scores = sim_scores[1:11]

        product_indices = [i[0] for i in sim_scores]

        #  top 10 most similar products
        return (df['category_name'].iloc[product_indices], df['ImageLink'].iloc[product_indices])

option=st.radio(
          'You added this into your basket',
          ['Banyo Dolabı', 'Abiye Ayakkabı','Medikal Maske'])

if option == 'Banyo Dolabı':
    df_reco =get_recommendations('Banyo Dolabı', cosine_sim)

elif option=='Abiye Ayakkabı':
    df_reco=get_recommendations('Abiye Ayakkabı', cosine_sim)
else:
    df_reco=get_recommendations('Medikal Maske', cosine_sim)
names=(df_reco[0])
for i in df_reco[1]:
    st.image(i,use_column_width=True)


