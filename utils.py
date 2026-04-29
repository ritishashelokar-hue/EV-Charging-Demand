import streamlit as st
import base64
import os


def set_bg_and_glass(image_path):
    if not os.path.exists(image_path):
        st.warning("Background image not found.")
        return

    with open(image_path, "rb") as img:
        encoded = base64.b64encode(img.read()).decode()

    st.markdown(
        f"""
        <style>
        /* Semi-blur dark background */
        .stApp {{
            background:
            linear-gradient(rgba(0,0,0,0.45), rgba(0,0,0,0.45)),
            url("data:image/png;base64,{encoded}") no-repeat center center fixed;
            background-size: cover;
        }}

        /* Glass effect for main content */
        .glass-box {{
            background: rgba(255, 255, 255, 0.12);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border-radius: 20px;
            padding: 35px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.35);
            border: 1px solid rgba(255, 255, 255, 0.25);
            max-width: 1000px;
            margin: auto;
            color: white;
        }}

        /* Text color inside glass */
        .glass-box h1,
        .glass-box h2,
        .glass-box h3,
        .glass-box p,
        .glass-box li,
        .glass-box label {{
            color: white !important;
        }}

        /* Improve input field look inside glass */
        .glass-box .stTextInput input,
        .glass-box .stNumberInput input,
        .glass-box .stSelectbox div,
        .glass-box .stDateInput input {{
            background: rgba(255,255,255,0.15) !important;
            color: white !important;
            border-radius: 10px !important;
        }}

        /* Glass-style buttons */
        .glass-box .stButton>button {{
            background: rgba(255,255,255,0.2);
            color: white;
            border-radius: 12px;
            border: 1px solid rgba(255,255,255,0.3);
            backdrop-filter: blur(8px);
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def glass_open():
    return '<div class="glass-box">'


def glass_close():
    return "</div>"

