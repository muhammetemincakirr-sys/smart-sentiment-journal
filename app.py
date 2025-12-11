import streamlit as st
from textblob import TextBlob

# Sayfa Ayarları
st.set_page_config(page_title="Smart Sentiment Journal", page_icon="🧠")

# Başlık ve Açıklama
st.title("🧠 Smart Sentiment Journal")
st.write("Duygularınızı analiz eden yapay zeka günlüğü. İngilizce bir cümle yazın, analiz edelim!")

# Kullanıcıdan Veri Alma (Input)
user_input = st.text_area("Günlüğüne ne yazmak istersin?", height=150)

# Buton
if st.button("Analiz Et"):
    if user_input:
        # Analiz İşlemi
        blob = TextBlob(user_input)
        skor = blob.sentiment.polarity
        
        # Sonuçları Gösterme
        st.write("---")
        st.subheader("Analiz Raporu")
        
        if skor > 0.5:
            st.success(f"Duygu Durumu: Harika! (Skor: {skor:.2f}) 🤩")
        elif skor > 0:
            st.info(f"Duygu Durumu: Pozitif (Skor: {skor:.2f}) 🙂")
        elif skor == 0:
            st.warning(f"Duygu Durumu: Nötr (Skor: {skor:.2f}) 😐")
        else:
            st.error(f"Duygu Durumu: Negatif (Skor: {skor:.2f}) 😔")
            
    else:
        st.write("Lütfen önce bir metin girin.")
