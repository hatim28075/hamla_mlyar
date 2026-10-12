import streamlit as st
st.set_page_config(page_title="حملة المليار صلاة", page_icon="ﷺ", layout="centered")
st.markdown("""
<style>
.main-title { text-align: center; font-size: 42px; color: #0d5d2e; font-weight: bold; }
.counter-box { background: linear-gradient(135deg, #0d5d2e, #1a9c4e); color: white; padding: 30px; border-radius: 20px; text-align: center; margin: 20px 0; }
.counter-number { font-size: 60px; font-weight: bold; }
.hadith { background: #fff; border-right: 5px solid #0d5d2e; padding: 15px; border-radius: 10px; text-align: right; margin:15px 0; }
</style>
""", unsafe_allow_html=True)
if 'count' not in st.session_state:
    st.session_state.count = 782354120
st.markdown('<div class="main-title">ﷺ حملة المليار صلاة على النبي ﷺ</div>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center;">من صلى علي واحدة صلى الله عليه عشرا</p>', unsafe_allow_html=True)
st.markdown(f'<div class="counter-box"><div>العدد الحالي</div><div class="counter-number">{st.session_state.count:,}</div><div>صلاة على النبي ﷺ</div></div>', unsafe_allow_html=True)
if st.button("ﷺ صل على النبي ﷺ", use_container_width=True):
    st.session_state.count += 1
    st.balloons()
    st.success("تم تسجيل صلاتك!")
st.markdown('<div class="hadith"><b>فضل الصلاة:</b><br>- سبب في شفاعة النبي ﷺ<br>- سبب لمغفرة الذنوب<br>- أولى الناس بالنبي يوم القيامة أكثرهم صلاة عليه</div>', unsafe_allow_html=True)
