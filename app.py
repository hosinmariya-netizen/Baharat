import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.title("متجر حوامل البهارات")

# الاتصال يتم الآن عبر الإعدادات التي حفظناها في Secrets
conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read()

# عرض البيانات
selected_model = st.selectbox("اختر الموديل:", df['الموديل'].tolist())
product = df[df['الموديل'] == selected_model].iloc[0]

st.image(product['رابط_الصورة'], use_column_width=True)
st.subheader(f"السعر: {product['السعر']} دج")

if st.button("طلب المنتج"):
    st.success("تم تأكيد اختيارك!")
    
