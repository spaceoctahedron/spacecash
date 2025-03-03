import streamlit as st
import yfinance as yf
from datetime import datetime
from PIL import Image

# Function to format balance with space as thousands separator and comma as decimal
def format_balance(balance):
    return "{:,.2f}".format(balance).replace(",", " ").replace(".", ",")

# Hide the account balance initially
def toggle_balance():
    if 'show_balance' not in st.session_state:
        st.session_state.show_balance = False

    if st.button("Afficher le solde"):
        st.session_state.show_balance = not st.session_state.show_balance
    
    formatted_balance = format_balance(11_820_000)  # Example balance

    if st.session_state.show_balance:
        return f"Votre solde : <span style='color: #52bcff;'>{formatted_balance} XOF</span>"
    else:
        return "Votre solde :<span style='color: #52bcff;'> **** **** **** **** ****</span>"

# Function to display card images as a slider
def display_card_slider():
    debit_card_image = Image.open("assets/card_debit.png")
    credit_card_image = Image.open("assets/card_credit.png")

    card_options = ["Carte Débit", "Carte Crédit"]
    selected_card = st.radio("Choisissez une carte à afficher:", card_options)

    if selected_card == "Carte Débit":
        st.image(debit_card_image, caption="Carte Débit", use_container_width=True)
    elif selected_card == "Carte Crédit":
        st.image(credit_card_image, caption="Carte Crédit", use_container_width=True)

# Main function to render the page
def main():
    st.set_page_config(page_title="Space Cash", page_icon="📱", layout="wide")
    st.logo("assets/logo.png")
    
    current_datetime = datetime.now().strftime("%d %B %Y %H:%M")
    
    # Page title and introduction
    
    st.image("assets/stars.gif", use_container_width=True)
    st.markdown('<h1 style="color: #8b76e9;">SPACE CASH</h1>', unsafe_allow_html=True)
    st.write("### Bienvenue !")
    st.write(f"Dernière connexion: {current_datetime}")
    st.write("***")

    # Toggle for hiding/unhiding account balance
    st.write("### Votre solde de compte:")
    balance = toggle_balance()
    st.markdown(balance, unsafe_allow_html=True)
    st.write("***")

    # Display debit and credit card images with a radio button slider
    st.write("### Vos cartes bancaires:")
    display_card_slider()

    st.write("***")

    # Display investment opportunities
    st.write("### Restez informé des marchés boursiers mondiaux")

    logo_urls = {
        "AAPL": "https://companieslogo.com/img/orig/AAPL-bf1a4314.png?t=1720244490&download=true",
        "NVDA": "https://companieslogo.com/img/orig/NVDA-220e1e03.png?t=1722952498&download=truex",
        "MSFT": "https://companieslogo.com/img/orig/MSFT-a203b22d.png?t=1722952497&download=true",
        "AMZN": "https://companieslogo.com/img/orig/AMZN-e9f942e4.png?t=1722944001&download=true",
        
        "GOOG": "https://companieslogo.com/img/orig/GOOG-0ed88f7c.png?t=1722952493&download=true",
        "2222.SR": "https://companieslogo.com/img/orig/2222.SR-99009d53.png?t=1720244490&download=true",
        "META": "https://companieslogo.com/img/orig/META-4767da84.png?t=1720244492&download=true",
        "BRK-B": "https://companieslogo.com/img/orig/BRK-B-25f11589.png?t=1722006061&download=true",
        "TSM": "https://companieslogo.com/img/orig/TSM-f70117e2.png?t=1722952500&download=true",
    }

    tickers = ["AAPL", "NVDA", "MSFT", "AMZN", "GOOG", "2222.SR", "META", "BRK-B", "TSM"]
    selected_ticker = st.selectbox("Sélectionnez un symbole boursier", tickers)

    company = yf.Ticker(selected_ticker)

    data = yf.download(selected_ticker, period='8d')
    data.index = data.index.date
    data.drop('Volume', axis=1, inplace=True)

    data = data.applymap(lambda x: round(x) if isinstance(x, (int, float)) else x)

    historical_data = company.history(period="24mo")

    logo_url = logo_urls.get(selected_ticker, None)
    st.markdown("""
        <style>
            .circle-logo {
                width: 80px; 
                height: 80px;
                border-radius: 50%;
                background-color: #D3D3D3;  /* Light gray background */
                display: flex;
                justify-content: center;
                align-items: center;
                overflow: hidden;
            }
            .circle-logo img {
                width: auto;
                height: 50%;
                object-fit: contain;
            }
        </style>
    """, unsafe_allow_html=True)

    if logo_url:
        st.markdown(f'<div class="circle-logo"><img src="{logo_url}" alt="Logo"></div>', unsafe_allow_html=True)

    st.write(f"#### {company.info.get('shortName', selected_ticker)}")
    st.write("Les données ci-dessus montrent les prix des actions en dollars pour les derniers jours. Les valeurs maximales sont mises en surbrillance.")
    st.write(" ")
    st.dataframe(data.style.highlight_max(color='#8b76e9', axis=0))
    st.write("Le graphique suivant montre l'évolution des prix des actions en dollars sur les deux dernières années")
    st.line_chart(historical_data['Close'], color="#ea2071")

if __name__ == "__main__":
    main()
