import streamlit as st
import time

st.set_page_config(page_title="Gus AI 真實指揮部", layout="wide")

st.title("⚓ Gus 高雄港 AI 真實指揮部")

# 1. 權限鎖定：只有 Owner Gus 能下令
password = st.sidebar.text_input("請輸入指揮官口令", type="password")

if password == "1188": # 這是您的私人密碼
    st.sidebar.success("身分驗證成功：Owner Gus 登入")
    
    command = st.text_input("🎙️ 請輸入或用語音輸入指令（例如：老張出車）")

    if st.button("確認下達最高指令"):
        if "老張" in command and "出車" in command:
            st.warning("⚠️ 指令確認：老張 118 號碼頭 準備起錨...")
            bar = st.progress(0)
            for i in range(100):
                time.sleep(0.02)
                bar.progress(i + 1)
            st.success("✅ 老張已出發！GPS 開始回傳實時數據。")
        else:
            st.error("❌ 偵測到無效命令。Gus，請明確下達『誰』要『幹嘛』。")
            
else:
    st.warning("🔒 系統鎖定中。請輸入口令以獲取指揮權。")
    st.info("目前的狀態：司機原地待命，營收結算凍結中。")
