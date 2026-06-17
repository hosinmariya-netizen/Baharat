import streamlit as st
import pandas as pd

# استبدل هذا الرابط برابط الـ CSV الذي ستستخرجه من "نشر للويب"
csv_url = "ضع_رابط_الـ_CSV_هنا"

@st.cache_data
def load_data():
    return pd.read_csv(csv_url)

df = load_data()

st.title("متجر حوامل البهارات")

# اختيار المنتج
selected_model = st.selectbox("اختر الموديل:", df['الموديل'])
product = df[df['الموديل'] == selected_model].iloc[0]

# عرض البيانات
st.image(product['رابط_الصورة'])
st.write(f"السعر: {product['السعر']} دج")
