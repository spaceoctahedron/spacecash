import streamlit as st

def main():
    st.logo("assets/logo.png")
    st.title("Remboursement")
    st.subheader("Suivi de vos demandes de remboursement")

    # Refund status
    st.write("### Remboursements en cours")
    st.write("1. Remboursement de frais de transfert bancaire: En attente de validation.")
    st.write("2. Remboursement d'une erreur de facturation: Complété - 20 000,00 XOF.")

    # Refund request history
    st.write("### Historique des remboursements")
    st.write("1. Erreur de facturation - 10 janvier 2025 - Remboursé: 100 000,00 XOF.")

if __name__ == "__main__":
    main()
