import streamlit as st
from datetime import datetime, timedelta
import requests

# 🔄 Rafraîchissement automatique via JavaScript (toutes les 30 secondes)
st.markdown("""
    <script>
    function refreshPage() {
        window.location.reload();
    }
    setTimeout(refreshPage, 30000); // 30 000 ms = 30 secondes
    </script>
""", unsafe_allow_html=True)

# Configuration de la page
st.set_page_config(page_title="Assistant Horloge", page_icon="🕐", layout="centered")

# 📡 Récupérer l'heure exacte depuis l'API worldtimeapi
try:
    response = requests.get("http://worldtimeapi.org/api/timezone/Europe/Paris")
    data = response.json()
    now = datetime.fromisoformat(data["datetime"].split(".")[0])
except Exception as e:
    st.error("❌ Erreur de synchronisation avec l'heure externe. Heure locale utilisée.")
    now = datetime.now()

# 🕐 Afficher l'heure actuelle
st.title("🕐 Assistant Horloge")
st.write(f"Heure exacte synchronisée (Paris) : **{now.strftime('%H:%M:%S')}**")

# 📦 Liste des livrables avec leurs deadlines
livrables = [
    {"nom": "Assistant Horloge", "deadline": datetime.combine(now.date(), datetime.strptime("23:59", "%H:%M").time())},
    {"nom": "Assistant CRM", "deadline": now + timedelta(hours=12)},
    {"nom": "Création Société", "deadline": now + timedelta(hours=18)},
]

# 🔁 Afficher chaque livrable
for livrable in livrables:
    deadline = livrable["deadline"]
    total_seconds = (deadline - now).total_seconds()
    total_jour = (deadline - datetime.combine(now.date(), datetime.min.time())).total_seconds()
    progress = max(0.0, min(1.0, 1 - total_seconds / total_jour))

    st.subheader(f"📦 {livrable['nom']} — deadline : {deadline.strftime('%d/%m %H:%M')}")
    st.progress(progress)
    if total_seconds > 0:
        h = int(total_seconds // 3600)
        m = int((total_seconds % 3600) // 60)
        s = int(total_seconds % 60)
        st.write(f"⏳ Temps restant : **{h}h {m}m {s}s**")
    else:
        st.write("✅ Livrable terminé ou en retard.")
