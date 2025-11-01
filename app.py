import os
import requests
import streamlit as st

st.set_page_config(page_title="Trend Detector – TikTok Research API Demo", layout="centered")

st.title("Trend Detector – TikTok Research API Demo")
st.write("Private research demo showing the OAuth2 client-credentials token flow. No end-user login or posting.")

with st.expander("What this demo shows"):
    st.markdown(
        """
- Uses TikTok **client_credentials** OAuth (server-to-server).
- Fetches a temporary **access token** from `https://open.tiktokapis.com/v2/oauth/token/`.
- No user login, no posting, no analytics; for reviewer demonstration only.
"""
    )

st.subheader("1) Get Client Access Token (OAuth2)")
ck_default = st.secrets.get("TIKTOK_CLIENT_KEY", "")
cs_default = st.secrets.get("TIKTOK_CLIENT_SECRET", "")

ck = st.text_input(
    "Client Key",
    value=ck_default,
    type="password",
    help="Populate via Streamlit Secrets or paste for demo.",
)
cs = st.text_input(
    "Client Secret",
    value=cs_default,
    type="password",
    help="Populate via Streamlit Secrets or paste for demo.",
)

if st.button("Request Token (demo)"):
    try:
        r = requests.post(
            "https://open.tiktokapis.com/v2/oauth/token/",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data={"client_key": ck, "client_secret": cs, "grant_type": "client_credentials"},
            timeout=20,
        )
        st.code(f"HTTP {r.status_code}\\n\\n{r.text[:2000]}", language="json")
        if r.ok:
            st.success("Access token received (see JSON).")
        else:
            st.warning("Non-200 response shown above (expected in sandbox or if creds are placeholders).")
    except Exception as e:  # pylint: disable=broad-except
        st.error(str(e))

st.subheader("2) Compliance")
col1, col2 = st.columns(2)
with col1:
    st.page_link("privacy.py", label="Privacy Policy", icon="🔒")
with col2:
    st.page_link("terms.py", label="Terms of Service", icon="📄")

st.caption("© 2025 Trend Detector (Private Research Project)")
