import streamlit as st

def main():
    st.title("Transfert d'argent")
    st.subheader("Effectuez un transfert d'argent")

    # Transfer options
    st.write("### Choisissez le type de transfert")
    transfer_type = st.selectbox("Type de transfert:", ["Transfert vers un autre compte", "Transfert mobile", "International"])

    # Amount input
    st.write("### Montant du transfert:")
    transfer_amount = st.number_input("Montant:", min_value=0.0, format="%.2f")

    # Recipients
    st.write("### Destinataire:")
    recipient = st.text_input("Nom du destinataire")
    recipient_account = st.text_input("Numéro de compte ou numéro mobile")

    # Perform transfer button
    if st.button("Effectuer le transfert"):
        st.success(f"Transfert de {transfer_amount} XOF effectué avec succès à {recipient}.")

if __name__ == "__main__":
    main()
