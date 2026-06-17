import streamlit as st
import pandas as pd

# رابط ملف Google Sheets (تأكد من جعله عاماً للنشر للويب)
sheet_url = "ضع_رابط_ملف_CSV_الخاص_بجدولك_هنا"

@st.cache_data
def load_data():
    return pd.read_csv(sheet_url)

df = load_data()

st.title("معرض حوامل البهارات الخشبية")

# اختيار الموديل من القائمة
selected_model = st.selectbox("اختر الموديل الذي تريده:", df['الموديل'])

# عرض تفاصيل الموديل
model_info = df[df['الموديل'] == selected_model].iloc[0]

st.image(model_info['رابط_الصورة'], caption=selected_model)
st.write(f"### السعر: {model_info['السعر']} دج")

if st.button("طلب هذا المنتج"):
    st.success("تم تأكيد اختيارك! يرجى التواصل معنا للتنفيذ.")
  
