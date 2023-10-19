import streamlit as st

def main():
    st.title("Trouver votre jeu ou compétition E-Sport")

    # Posez les questions
    q1 = st.selectbox('Question 1:', ['Option 1', 'Option 2', 'Option 3'])
    q2 = st.selectbox('Question 2:', ['Option 1', 'Option 2', 'Option 3'])
    q3 = st.selectbox('Question 3:', ['Option 1', 'Option 2', 'Option 3'])
    q4 = st.selectbox('Question 4:', ['Option 1', 'Option 2', 'Option 3'])
    q5 = st.selectbox('Question 5:', ['Option 1', 'Option 2', 'Option 3'])

    # Bouton pour générer la suggestion
    if st.button('Suggérez-moi un jeu/compétition!'):
        # Ici, vous intégreriez avec GPT-3
        suggestion = get_gpt3_suggestion(q1, q2, q3, q4, q5)
        st.write(f"Vous devriez essayer: {suggestion}")

def get_gpt3_suggestion(q1, q2, q3, q4, q5):
    # Cette fonction fera l'intégration avec GPT-3
    # Pour l'instant, elle renvoie une suggestion fictive
    return "Jeu fictif"

if __name__ == "__main__":
    main()
