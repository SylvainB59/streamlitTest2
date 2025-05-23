import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title('Manipulation de données et création de graphiques')

# load names of seaborn dataset
# a github repo that allow the use of sns.load
dataset_name = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/dataset_names.txt')

# select box with dataset names
set = st.selectbox('Quel dataset veux-tu utiliser ?',dataset_name)

# st.write(set)
# df = sns.load_dataset(set, header=[0,3], index_col=[0,1])
# chargement du dataset selectionné
df = sns.load_dataset(set)

# affichage du dataset en dataframe streamlit
st.dataframe(df)

# récupération des colonnes
col = df.columns

# choix de la colonne X
X = st.selectbox('Choisissez la colonne X:', col)

# choix de la colonne Y en retirant la colonne X sélectionnée
Y = st.selectbox('Choisissez la colonne Y:', col.drop(X))

# liste des graph avec la fonction strealit en value graph
dict = {
    'scatter chart': st.scatter_chart,
    'line chart': st.line_chart,
    'bar char': st.bar_chart
}

# selection du graph
graph = st.selectbox('Quel graph veux-tu utiliser ?',dict)

# affichage du graph
dict[graph](data=df, x=X, y=Y)


# --------- checkbox correlation -----------
# copy de la df
df_corr = df.copy()
# boucle pour isoler les colonnes numérique
for i in col:
    if str(df[i].dtype) not in ('int64' , 'float64'):
        # st.write(i, df[i].dtype)
        df_corr.drop(i,axis=1, inplace=True)
# st.write(df_corr.shape[1])

# st.write(df_corr)
# st.write(df)
if st.checkbox('Afficher la matrice de corrélation ?'):
    # évite une erreur si la df ne contient pas de colonne numérique
    if 0 in df_corr.shape:
        st.write('/ ********************* \\')
        st.write('| - - -    Rien à afficher    - - - |')
        st.write('\\ ********************* /')
    else:
        df_corr.dropna(axis=0)
        corr = df_corr.corr()
        sns.heatmap(corr)
        st.pyplot(plt.gcf())