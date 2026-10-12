
import streamlit as st, requests
st.set_page_config(page_title="مليار صلاة", page_icon="🕌")
U="https://abacus.jasoncameron.dev/hit/hamlamlyar-final-v2/0"
try:c=requests.get(U.replace('/hit/','/get/')).json()['value']
except:c=0
st.markdown(f"<h1 style='text-align:center'>{c:,}</h1>", unsafe_allow_html=True)
if st.button("صل على النبي ﷺ", use_container_width=True, type="primary"):
    c=requests.get(U).json()['value'];st.rerun()
