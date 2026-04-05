import streamlit as st

st.set_page_config(page_title="Dahi Aras Hyper-Live", layout="wide")
st.title("🚀 Dahi Aras Ultra-Fast Live & Chatbot")

col1, col2 = st.columns([2, 1])

with col1:
    st.header("📹 Siber Yayın Ekranı")
    st.write("Hande Hoca Siber Takip Sistemi: AKTİF ✅")
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJndXIzZ3R3eXlyeXN6eHlyeXN6eHlyeXN6eHlyeXN6eCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7TKSjPqcKlxmP6Cy/giphy.gif")

with col2:
    st.header("🤖 Aras-Bot Chat")
    if "messages" not in st.session_state: st.session_state.messages = []
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]): st.markdown(msg["content"])
    if prompt := st.chat_input("Alparslan'a ne söyleyeyim kanka?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        response = f"Dahi Aras diyor ki: {prompt} - 10 Bin Lira masada kanka!"
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.rerun()
