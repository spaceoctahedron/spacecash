import streamlit as st

def main():
    st.title("Mobile Money")
    st.subheader("Gérez votre argent mobile")

    # Mobile money balance
    st.write("### Solde mobile money:")
    st.write("Votre solde actuel: 500 000,00 XOF")

    # Mobile money operations
    st.write("### Opérations récentes")
    st.write("1. Transfert reçu: 100 000,00 XOF - 15 janvier 2025")
    st.write("2. Recharge de téléphone: -20 000,00 XOF - 14 janvier 2025")
    st.write("3. Paiement de facture: -50 000,00 XOF - 13 janvier 2025")

    # Transfer options
    st.write("### Effectuer une opération")
    st.selectbox("Choisissez l'opération:", ["Envoyer de l'argent", "Recharger votre solde", "Payer des factures"])
    st.text_input("Montant:")

if __name__ == "__main__":
    main()
