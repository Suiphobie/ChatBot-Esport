import streamlit as st

def main():
    st.title("Trouver votre jeu ou compétition E-Sport basé sur vos préférences sportives")

    # Posez les questions sur les sports traditionnels
    q1 = st.selectbox('Quel type de sport préférez-vous regarder ?', 
                      ['Individuel (e.g., tennis, athlétisme)', 
                       'Collectif (e.g., football, basketball)', 
                       'Sports mécaniques (e.g., Formule 1, MotoGP)', 
                       'Sports de combat (e.g., boxe, MMA)', 
                       'Autres'])

    q2 = st.selectbox('Quelle intensité de jeu préférez-vous ?', 
                      ['Action rapide et continue (e.g., basketball, hockey)', 
                       'Moments stratégiques et pauses (e.g., football américain, cricket)', 
                       'Endurance et longue durée (e.g., marathon, cyclisme)'])

    q3 = st.selectbox('Que préférez-vous dans un sport ?', 
                      ['Stratégie et tactique (e.g., échecs, snooker)', 
                       'Performance physique et athlétisme (e.g., 100 mètres sprint, natation)'])

    q4 = st.selectbox('Dans quel environnement aimez-vous voir un sport se dérouler ?', 
                      ['Intérieur (e.g., basketball, volley-ball)', 
                       'Extérieur (e.g., football, rugby)', 
                       'Virtuel (e.g., jeux vidéo, simulations)'])

    q5 = st.selectbox('Comment préférez-vous vous engager avec le sport que vous regardez ?', 
                      ['Je préfère juste regarder', 
                       'Je discute avec des amis ou en ligne', 
                       'J\'assiste à des événements en personne', 
                       'Je pratique moi-même le sport'])

    # Bouton pour générer la suggestion
    if st.button('Suggérez-moi un jeu/compétition E-Sport!'):
        # Ici, vous intégreriez avec GPT-3
        suggestion = get_gpt3_suggestion(q1, q2, q3, q4, q5)
        st.write(f"Vous devriez essayer: {suggestion}")

def get_gpt3_suggestion(q1, q2, q3, q4, q5):
    # Cette fonction fera l'intégration avec GPT-3
    # Pour l'instant, elle renvoie une suggestion fictive
    return "Jeu fictif"

if __name__ == "__main__":
    main()
