import streamlit as st
import pandas as pd

# رابط الجدول الخاص بك
sheet_id = "1M-T1POUH1IvVOXDYX-rW9-Qw27OVGj069j2MiS3TlkA"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet=Sheet1"

@st.cache_data
def load_data():
    return pd.read_csv(url)

# تحميل البيانات
try:
    df = load_data()
    st.title("متجر حوامل البهارات")

    # قائمة اختيار الموديلات
    selected_model = st.selectbox("اختر الموديل:", df['الموديل'])
    product = df[df['الموديل'] == selected_model].iloc[0]

    # عرض البيانات
    st.image(product['رابط_الصورة'])
    st.write(f"### السعر: {product['السعر']} دج")
    
    if st.button("طلب المنتج"):
        st.success("تم الطلب بنجاح!")
except Exception as e:
    st.error("حدث خطأ في قراءة الجدول. تأكد من أن اسم الورقة في الأسفل هو 'Sheet1' وأن الأعمدة هي 'الموديل'، 'السعر'، 'رابط_الصورة'.")
    
