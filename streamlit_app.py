import os
from dotenv import load_dotenv
import streamlit as st
import requests

load_dotenv()

API_URL = os.getenv(
    "API_URL", "https://blind-saver-performing-editions.trycloudflare.com"
)
API_KEY = os.getenv("API_KEY", "change-me")
HEADERS = {"X-API-KEY": API-KEY}

st.title("TCP Server Control Panel")

if st.button("Refresh Status"):
    try:
        r = requests.get(f"{API_URL}/status", headers=HEADERS, timeout=10)
    except requests.RequestException:
        st.error("Server not reachable")
    else:
        if r.status_code == 200:
            data = r.json()
            st.subheader("Connected Clients")
            st.write(data.get("clients") or "No clients")
            st.subheader("Messages")
            st.text_area("", "\n".join(data.get("messages", [])), height=300)
        else:
            st.error("Server not reachable")

cmd = st.text_input("Command")

if st.button("Send"):
    try:
        r = requests.post(
            f"{API_URL}/send", headers=HEADERS, json={"command": cmd}, timeout=10
        )
    except requests.RequestException:
        st.error("Send failed")
    else:
        if r.status_code == 200:
            st.success("Command sent")
        else:
            st.error("Send failed")
