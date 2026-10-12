
import streamlit as st
st.title("ﷺ حملة المليار صلاة")
if "c" not in st.session_state:
    st.session_state.c = 0
st.header(st.session_state.c)
if st.button("صل على النبي ﷺ"):
    st.session_state.c += 1
    st.rerun()
