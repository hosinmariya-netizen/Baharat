import streamlit as st
import pandas as pd

# رابط الجدول الخاص بك مع تحديد اسم الورقة "baharat"
sheet_id = "1M-T1POUH1IvVOXDYX-rW9-Qw27OVGj069j2MiS3TlkA"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet=baharat"

@st.cache_data
def load_data():
    return pd.read_csv(url)

# تحميل البيانات
try:
    df = load_data()
    st.title("متجر حوامل البهارات")

    # اختيار الموديل من القائمة
    selected_model = st.selectbox("اختر الموديل:", df['الموديل'])
    product = df[df['الموديل'] == selected_model].iloc[0]

    # عرض البيانات
    st.image(product['رابط_الصورة'])
    st.subheader(f"السعر: {product['السعر']} دج")
    
    if st.button("طلب المنتج"):
        st.success("تم تأكيد اختيارك! يرجى التواصل معنا للتنفيذ.")

except Exception as e:
    st.error("حدث خطأ! تأكد من أن أسماء الأعمدة في الجدول هي: 'الموديل'، 'السعر'، 'رابط_الصورة'.")
    
