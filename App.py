import streamlit as st

st.title("مرحباً بك في متجر حاملات البهارات")
st.write("هنا ستظهر موديلاتنا الرائعة قريباً.")

# اختيار بسيط للتجربة
choice = st.selectbox("اختر الموديل:", ["موديل 1", "موديل 2"])
st.write(f"لقد اخترت: {choice}")
