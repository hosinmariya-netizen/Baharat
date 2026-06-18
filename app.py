import streamlit as st
import pandas as pd

# البيانات مباشرة في الكود - بدون Google Sheets
data = {
    'الموديل': ['موديل 1', 'موديل 2', 'موديل 3'],
    'السعر': ['500 دج', '750 دج', '1000 دج'],
    'رابط_الصورة': [
        'https://رابط_صورة_1.jpg',
        'https://رابط_صورة_2.jpg',
        'https://رابط_صورة_3.jpg'
    ]
}

df = pd.DataFrame(data)

st.title("متجر حوامل البهارات")

selected_model = st.selectbox("اختر الموديل:", df['الموديل'])
product = df[df['الموديل'] == selected_model].iloc[0]

st.image(product['رابط_الصورة'])
st.subheader(f"السعر: {product['السعر']}")

if st.button("طلب المنتج"):
    st.success("تم تأكيد اختيارك!")
