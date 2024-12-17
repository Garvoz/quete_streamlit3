import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu


# Nos données utilisateurs doivent respecter ce format


lesDonneesDesComptes = {'usernames': {'utilisateur': {'name': 'utilisateur',

    'password': 'utilisateurMDP',

    'email': 'utilisateur@gmail.com',

    'failed_login_attemps': 0, # Sera géré automatiquement

    'logged_in': False, # Sera géré automatiquement

    'role': 'utilisateur'},

    'root': {'name': 'root',

    'password': 'rootMDP',

    'email': 'admin@gmail.com',

    'failed_login_attemps': 0, # Sera géré automatiquement

    'logged_in': False, # Sera géré automatiquement

    'role': 'administrateur'}}}


authenticator = Authenticate(

    lesDonneesDesComptes, # Les données des comptes

    "cookie name", # Le nom du cookie, un str quelconque

    "cookie key", # La clé du cookie, un str quelconque

    30, # Le nombre de jours avant que le cookie expire 

)


authenticator.login()

def accueil():

    with st.sidebar:

        authenticator.logout("Déconnexion")

        st.write(f"Bienvenue *root*")

        selection = option_menu( menu_title= 'Menu : ', options = [ "🤩 Accueil", "😺 Les photos de mon chat"] )   

        

    if selection == "🤩 Accueil":
        st.markdown("<h1 style='text-align: center;'>Bienvenu sur ma page</h1>", unsafe_allow_html=True)
        st.markdown("<div style='text-align: center;'><img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRhl6uQ4mc5cA-m-m2M0oJPXboqxOhYFpbGpg&s' width='300'></div>", unsafe_allow_html=True)
   
    elif selection == "😺 Les photos de mon chat":
        st.markdown("<h1 style='text-align: center;'>Bienvenue dans l'album photo de mon chat 😺</h1>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)

        with col1:
            st.image("data:image/jpeg;base64,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")


        with col2:
            st.image("https://t4.ftcdn.net/jpg/07/14/01/67/360_F_714016720_bvIgAZqr86I74NxvMJQoW9jlsC6yCxTa.jpg")


        with col3:
            st.image("https://img.freepik.com/photos-premium/chat-tabby-surpris-yeux-larges-fond-rose-parfait-pour-contenu-humoristique_1294860-22296.jpg?semt=ais_hybrid")


if st.session_state["authentication_status"]:

  accueil()

elif st.session_state["authentication_status"] is False:

    st.error("L'username ou le password est/sont incorrect")

elif st.session_state["authentication_status"] is None:

    st.warning('Les champs username et mot de passe doivent être remplie')