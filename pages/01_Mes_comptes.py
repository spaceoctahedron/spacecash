import streamlit as st

def main():
    st.logo("assets/logo.png")
    st.title("Mes Comptes")
    st.subheader("Bienvenue sur votre espace comptes")

    # Account balance
    st.write("### Solde actuel de votre compte:")
    st.write("Votre solde: 11 820 000,00 XOF")  # Example balance

    # Account types
    st.write("### Types de comptes")
    st.write("1. Compte courant: Disponible pour les transactions quotidiennes.")
    st.write("2. Compte épargne: Pour économiser et générer des intérêts.")
    st.write("3. Compte professionnel: Compte dédié aux entreprises.")

    # Recent transactions (placeholder)
    st.write("### Transactions récentes")
    st.write("1. Dépôt: +2 000 000,00 XOF - 15 janvier 2025")
    st.write("2. Retrait: -500 000,00 XOF - 16 janvier 2025")
    st.write("3. Paiement: -1 000 000,00 XOF - 17 janvier 2025")

if __name__ == "__main__":
    main()
