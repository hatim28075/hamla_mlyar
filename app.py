
import streamlit as st

st.set_page_config(page_title="حملة المليار صلاة على النبي", page_icon="🕌", layout="centered")

if "c" not in st.session_state:
    st.session_state.c = 0

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Amiri:wght@700&display=swap');
h1,h2,p{font-family:'Amiri', serif; text-align:center}
.btn{width:100%; background:#0d5c36; color:white; padding:20px; border-radius:15px; font-size:26px; border:none}
.card{background:#f0fdf4; border:2px solid #0d5c36; border-radius:20px; padding:25px; text-align:center; margin:20px 0}
.num{font-size:80px; font-weight:bold; color:#0d5c36}
</style>
<h1>ﷺ حملة المليار صلاة على النبي ﷺ</h1>
<p>قال ﷺ: من صلى علي واحدة صلى الله عليه بها عشرا</p>
<div class='card'><div class='num'>{:,}</div><p>صلاة حتى الآن</p></div>
""".format(st.session_state.c), unsafe_allow_html=True)

if st.button("صل على النبي ﷺ", use_container_width=True, type="primary"):
    st.session_state.c += 1
    st.balloons()
    st.rerun()

st.markdown("<p>انسخ الرابط وانشره ولك أجر كل من صلى</p>", unsafe_allow_html=True)
st.code("https://hamlamlyar-hvbv2cv8hfpnapnxhusaqv.streamlit.app/")
