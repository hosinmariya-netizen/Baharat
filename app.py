import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.title("متجر حوامل البهارات")

# إنشاء الاتصال بـ Google Sheets
conn = st.connection("gsheets", type=GSheetsConnection)

# قراءة البيانات (باستخدام رابط الملف)
url = "https://docs.google.com/spreadsheets/d/1M-T1POUH1IvVOXDYX-rW9-Qw27OVGj069j2MiS3TlkA/edit?usp=drivesdk"
df = conn.read(spreadsheet=url, usecols=[0, 1, 2]) # سيقرأ أول 3 أعمدة (الموديل، السعر، الرابط)

# تنظيف البيانات (التأكد من أن الأعمدة صحيحة)
df.columns = ['الموديل', 'السعر', 'رابط_الصورة']

# عرض التطبيق
selected_model = st.selectbox("اختر الموديل:", df['الموديل'].tolist())

product = df[df['الموديل'] == selected_model].iloc[0]

st.image(product['رابط_الصورة'], caption=selected_model, use_column_width=True)
st.subheader(f"السعر: {product['السعر']} دج")

if st.button("طلب المنتج"):
    st.success("تم تأكيد اختيارك!")
    
