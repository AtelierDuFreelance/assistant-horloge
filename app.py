import streamlit as st
from datetime import datetime, timedelta

# Configuration de la page
st.set_page_config(page_title="Assistant Horloge", page_icon="🕐", layout="centered")

# Afficher l'heure actuelle
now = datetime.now()
st.title("🕐 Assistant Horloge")
st.write(f"Heure actuelle (heure système) : **{now.strftime('%H:%M:%S')}**")

# Deadline fictive
deadline = datetime.combine(now.date(), datetime.strptime("23:59:59", "%H:%M:%S").time())
remaining = (deadline - now).total_seconds()
total_day = 24 * 60 * 60
progress = 1 - (remaining / total_day)

# Afficher un livrable + barre de progression
st.subheader("📦 Livrable 1 : 'Assistant ADFL' – Livraison à minuit")
st.progress(progress)
st.write(f"Temps restant : **{int(remaining//3600)}h {int((remaining%3600)//60)}m {int(remaining%60)}s**")
