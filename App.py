import streamlit as st
import pandas as pd

# ضع رابط CSV الخاص بجدولك هنا بعد نشره للويب
sheet_url = "رابط_الـ_CSV_الذي_حصلت_عليه_من_Publish_to_web"

@st.cache_data
def load_data():
    return pd.read_csv(sheet_url)

df = load_data()

st.title("حوامل البهارات الخشبية")

# اختيار المنتج
selected_model = st.selectbox("اختر الموديل:", df['الموديل'])
product = df[df['الموديل'] == selected_model].iloc[0]

# عرض البيانات
st.image(product['رابط_الصورة'], caption=selected_model)
st.subheader(f"السعر: {product['السعر']} دج")

if st.button("طلب المنتج"):
    st.write("تم الطلب بنجاح!")
    
