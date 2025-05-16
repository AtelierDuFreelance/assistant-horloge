import streamlit as st
from datetime import datetime, timedelta
import pytz
import time

# Configuration de la page
st.set_page_config(page_title="Assistant Horloge", page_icon="🕐", layout="centered")

# Rafraîchir automatiquement toutes les 30 secondes
st.markdown(
    """
    <meta http-equiv="refresh" content="30">
    """,
    unsafe_allow_html=True
)

# Fuseau horaire Paris
paris = pytz.timezone('Europe/Paris')
now = datetime.now(paris)

# Afficher l'heure actuelle
st.title("🕐 Assistant Horloge")
st.write(f"Heure actuelle (Paris) : **{now.strftime('%H:%M:%S')}**")

# Deadline fictive à minuit heure de Paris
deadline = paris.localize(datetime.combine(now.date(), datetime.strptime("23:59:59", "%H:%M:%S").time()))
remaining = (deadline - now).total_seconds()
total_day = 24 * 60 * 60
progress = 1 - (remaining / total_day)

# Affichage d'un livrable + progression
st.subheader("📦 Livrable 1 : 'Assistant ADFL' – Livraison à minuit")
st.progress(progress)
st.write(f"⏳ Temps restant : **{int(remaining//3600)}h {int((remaining%3600)//60)}m {int(remaining%60)}s**")

# Lien pour t'adresser à moi
st.markdown("---")
st.markdown("💬 **Besoin de moi ?** [Clique ici pour me parler via ChatGPT](https://chat.openai.com/chat)")
