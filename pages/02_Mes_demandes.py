import streamlit as st

def main():
    st.title("Mes Demandes")
    st.subheader("Suivez vos demandes en cours")

    # Request status
    st.write("### Demandes en cours:")
    st.write("1. Demande de crédit immobilier: En attente de traitement.")
    st.write("2. Demande de carte bancaire: Approuvée, en attente de livraison.")
    st.write("3. Demande de remboursement: En cours d'examen.")

    # Request history
    st.write("### Historique des demandes:")
    st.write("1. Remboursement d'une transaction erronée - 10 février 2025 - Terminé.")
    st.write("2. Demande d'augmentation de limite de carte - 5 janvier 2025 - Approuvée.")

if __name__ == "__main__":
    main()
