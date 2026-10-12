
import streamlit as st
st.set_page_config(page_title="مليار صلاة", page_icon="🕌")
if "c" not in st.session_state:
    st.session_state.c = 0
st.markdown(f"<h1 style='text-align:center'>{st.session_state.c}</h1>", unsafe_allow_html=True)
if st.button("صل على النبي ﷺ", use_container_width=True, type="primary"):
    st.session_state.c += 1
    st.rerun()
