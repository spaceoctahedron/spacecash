import streamlit as st
from datetime import datetime
from PIL import Image

# Function to format balance with space as thousands separator and comma as decimal
def format_balance(balance):
    # Format the balance with spaces as thousands separators and commas as decimals
    return "{:,.2f}".format(balance).replace(",", " ").replace(".", ",")

# Hide the account balance initially
def toggle_balance():
    if 'show_balance' not in st.session_state:
        st.session_state.show_balance = False

    if st.button("Afficher le solde"):
        st.session_state.show_balance = not st.session_state.show_balance
    
    # Formatted balance using manual space formatting
    formatted_balance = format_balance(11_820_000)  # Example balance

    if st.session_state.show_balance:
        return f"Votre solde: {formatted_balance} XOF"
    else:
        return "Votre solde: **** **** **** **** ****"  # Hidden balance

# Function to display card images as a slider
def display_card_slider():
    # Upload or add the image paths for your debit and credit cards
    # For this example, I will assume the images are in the 'assets' folder and have rounded corners.

    # You should replace 'debit_card.jpg' and 'credit_card.jpg' with the actual image filenames
    debit_card_image = Image.open("assets/card_debit.png")
    credit_card_image = Image.open("assets/card_credit.png")

    # Create a slider to switch between the cards
    card_options = ["Carte Débit", "Carte Crédit"]
    selected_card = st.radio("Choisissez une carte à afficher:", card_options)

    if selected_card == "Carte Débit":
        st.image(debit_card_image, caption="Carte Débit", use_container_width=True)
    elif selected_card == "Carte Crédit":
        st.image(credit_card_image, caption="Carte Crédit", use_container_width=True)

# Main function to render the page
def main():
    # Set page configuration
    st.set_page_config(page_title="Space Cash", page_icon="📱", layout="wide")

    # Get the current datetime and format it
    current_datetime = datetime.now().strftime("%d %B %Y %H:%M")

    # Page title and introduction
    st.title("Bienvenue dans l'application Space Cash")
    st.subheader(f"Dernière connexion: {current_datetime}")
    st.write("***")

    # Toggle for hiding/unhiding account balance
    st.write("### Votre solde de compte:")
    balance = toggle_balance()
    st.write(balance)
    st.write("***")

    # Display debit and credit card images with a radio button slider
    st.write("### Vos cartes bancaires:")
    display_card_slider()

# Run the app
if __name__ == "__main__":
    main()
