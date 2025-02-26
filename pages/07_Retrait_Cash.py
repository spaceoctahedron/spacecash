import streamlit as st

def main():
    st.logo("assets/logo.png")
    st.title("Retrait Cash")
    st.subheader("Effectuer un retrait d'argent")

    # Withdrawal amount input
    st.write("### Montant du retrait:")
    withdrawal_amount = st.number_input("Montant à retirer:", min_value=0.0, format="%.2f")

    # Withdrawal options
    st.write("### Choisissez un mode de retrait:")
    withdrawal_mode = st.selectbox("Mode de retrait:", ["Retrait au guichet", "Retrait à un distributeur automatique"])

    # Perform withdrawal
    if st.button("Effectuer le retrait"):
        st.success(f"Retrait de {withdrawal_amount} XOF effectué avec succès par {withdrawal_mode}.")

if __name__ == "__main__":
    main()
