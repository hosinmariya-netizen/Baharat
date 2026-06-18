import streamlit as st
import pandas as pd

sheet_id = "1M-T1POUH1IvVOXDYX-rW9-Qw27OVGj069j2MiS3TlkA"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet=baharat"

@st.cache_data
def load_data():
    df = pd.read_csv(url)
    df.columns = df.columns.str.strip()
    return df

try:
    df = load_data()
    st.title("متجر حوامل البهارات")
    
    st.write("الأعمدة المتاحة:", df.columns.tolist())  # للتشخيص
    st.dataframe(df.head())  # لرؤية البيانات
    
    if 'الموديل' in df.columns:
        selected_model = st.selectbox("اختر الموديل:", df['الموديل'])
        product = df[df['الموديل'] == selected_model].iloc[0]
        
        if 'رابط_الصورة' in df.columns:
            st.image(product['رابط_الصورة'])
        
        if 'السعر' in df.columns:
            st.subheader(f"السعر: {product['السعر']} دج")
        
        if st.button("طلب المنتج"):
            st.success("تم تأكيد اختيارك!")

except Exception as e:
    st.error(f"الخطأ: {e}")
