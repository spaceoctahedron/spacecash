import streamlit as st

def main():
    st.logo("assets/logo.png")
    st.title("Marchand")
    st.subheader("Accédez aux services marchands")

    # Available services
    st.write("### Services disponibles")
    st.write("1. Paiement de factures")
    st.write("2. Achat de produits")
    st.write("3. Recharge de carte prépayée")

    # Service selection
    service = st.selectbox("Sélectionnez un service:", ["Paiement de factures", "Achat de produits", "Recharge de carte prépayée"])

    # Amount input for services
    st.write("### Montant:")
    amount = st.number_input("Montant:", min_value=0.0, format="%.2f")

    # Perform payment or purchase
    if st.button("Effectuer l'achat ou le paiement"):
        st.success(f"{service} de {amount} XOF effectué avec succès.")

if __name__ == "__main__":
    main()
