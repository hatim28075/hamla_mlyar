
import streamlit as st, requests

st.set_page_config(page_title="حملة المليار صلاة", page_icon="🕌")

@st.cache_data(ttl=2)
def get_global():
    try:
        r = requests.get("https://abacus.jasoncameron.dev/get/hamla-global-final", timeout=3).json()
        return r.get('value', 0)
    except:
        return 0

def hit_global():
    try:
        r = requests.get("https://abacus.jasoncameron.dev/hit/hamla-global-final", timeout=3).json()
        return r.get('value', 0)
    except:
        return None

count = get_global()
st.markdown(f"<h1 style='text-align:center'>{count:,}</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center'>صلاة حول العالم</p>", unsafe_allow_html=True)

if st.button("صل على النبي ﷺ", use_container_width=True, type="primary"):
    new = hit_global()
    if new is not None:
        st.cache_data.clear()
        st.rerun()
    else:
        st.error("النت ضعيف، حاول تاني")
