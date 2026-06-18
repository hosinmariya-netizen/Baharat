import streamlit as st
import pandas as pd

sheet_id = "1M-T1POUH1IvVOXDYX-rW9-Qw27OVGj069j2MiS3TlkA"

# جرب بدون تحديد اسم الورقة أولاً
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"

try:
    df = pd.read_csv(url)
    st.write(df)
except Exception as e:
    st.error(str(e))
