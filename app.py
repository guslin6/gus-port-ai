import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Gus AI 高雄港指揮部", layout="wide")

st.title("⚓ Gus 高雄港 AI 運輸指揮系統")
st.write(f"系統時間：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🎙️ 語音下令"):
        st.success("✅ 指令已接收：正在匹配 A 級司機...")
with col2:
    if st.button("📍 司機實體 GPS"):
        df = pd.DataFrame({
            'lat': [22.565, 22.560], 'lon': [120.330, 120.335],
            '司機': ['老張', '阿強']
        })
        st.map(df)
with col3:
    if st.button("💰 領取營收"):
        st.balloons()
        st.metric("本週淨利", "NT$ 175,500")

st.write("---")
st.caption("Owner Gus 專屬系統 v1.1")
