import streamlit as st
from PIL import Image
import base64
from streamlit_option_menu import option_menu

# Configure the page
st.set_page_config(
    page_title="CARE HEALTH",
    page_icon="🏥",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1E40AF;
        text-align: center;
        margin-bottom: 2rem;
    }
    .section-header {
        font-size: 2rem;
        font-weight: bold;
        color: #1F2937;
        text-align: center;
        margin-bottom: 1.5rem;
    }
    .card {
        background-color: white;
        padding: 1.5rem;
        border-radius: 0.75rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 1rem;
    }
    .card-title {
        font-size: 1.25rem;
        font-weight: bold;
        color: #1F2937;
        margin-bottom: 0.75rem;
    }
    .card-text {
        color: #4B5563;
        margin-bottom: 1rem;
    }
    .blue-button {
        background-color: #2563EB;
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 0.375rem;
        text-decoration: none;
        display: inline-block;
        margin: 0.25rem;
    }
    .blue-button:hover {
        background-color: #1D4ED8;
    }
    </style>
""", unsafe_allow_html=True)

# Header
col1, col2, col3 = st.columns([4, 4, 2])
with col1:
    st.markdown("<div style='font-size: 2rem; font-weight: bold; color: #2563EB;'>CARE HEALTH</div>", unsafe_allow_html=True)
with col3:
    st.button("Request Demo")

# Hero Section
st.markdown("<div class='main-header'>Transforming Healthcare Through Integrated Solutions</div>", unsafe_allow_html=True)
st.markdown("""
    <div style='text-align: center; font-size: 1.25rem; color: #4B5563; margin-bottom: 2rem;'>
        A comprehensive clinical workflow platform designed for health systems,
        offering intelligent automation, specialized documentation, and seamless EHR integration.
    </div>
""", unsafe_allow_html=True)

# Navigation
selected = option_menu(
    menu_title=None,
    options=["Solutions", "Flowsheets", "Invoices", "Allergy Shots", "Integrations"],
    icons=["grid", "file-text", "receipt", "activity", "boxes"],
    orientation="horizontal",
)

# Content based on selection
if selected == "Solutions":
    st.markdown("<div class='section-header'>Clinical Management Solutions</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: center; margin-bottom: 2rem;'>Streamlined workflows for enhanced patient care</div>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            <div class='card'>
                <div class='card-title'>Patient Lists</div>
                <div class='card-text'>Create and manage custom patient cohorts with our intelligent list management system.</div>
                <a href='#' class='blue-button'>Learn more →</a>
            </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
            <div class='card'>
                <div class='card-title'>Clinical Documentation</div>
                <div class='card-text'>AI-powered documentation tools that reduce clicks and save time.</div>
                <a href='#' class='blue-button'>Learn more →</a>
            </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown("""
            <div class='card'>
                <div class='card-title'>Care Coordination</div>
                <div class='card-text'>Streamline care coordination across departments with integrated communication tools.</div>
                <a href='#' class='blue-button'>Learn more →</a>
            </div>
        """, unsafe_allow_html=True)

elif selected == "Flowsheets":
    st.markdown("<div class='section-header'>Specialized Clinical Flowsheets</div>", unsafe_allow_html=True)
    
    flowsheets = {
        "Dermatology": [
            "Customized skin condition tracking",
            "Photo documentation integration",
            "Treatment response monitoring",
            "Procedure tracking"
        ],
        "Endocrinology": [
            "Hormone level tracking",
            "Diabetes management",
            "Thyroid disorder monitoring",
            "Treatment response graphs"
        ],
        "Plastic Surgery": [
            "Pre/post procedure documentation",
            "Photo integration",
            "Measurement tracking",
            "Custom procedure templates"
        ]
    }
    
    cols = st.columns(3)
    for idx, (specialty, features) in enumerate(flowsheets.items()):
        with cols[idx]:
            st.markdown(f"""
                <div class='card'>
                    <div class='card-title'>{specialty}</div>
                    <ul>
                        {"".join(f"<li>{feature}</li>" for feature in features)}
                    </ul>
                    <a href='#' class='blue-button'>Learn more →</a>
                </div>
            """, unsafe_allow_html=True)

elif selected == "Allergy Shots":
    st.markdown("<div class='section-header'>Immunotherapy Management</div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
            <div class='card'>
                <div class='card-title'>Allergy Shot Management</div>
                <ul>
                    <li>Immunotherapy dose tracking</li>
                    <li>Automated scheduling</li>
                    <li>Reaction monitoring</li>
                    <li>Patient notification system</li>
                    <li>Vial management</li>
                </ul>
                <a href='#' class='blue-button'>Learn more →</a>
            </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("""
    <div style='text-align: center; padding: 2rem;'>
        © 2024 Care Health. All rights reserved.
    </div>
""", unsafe_allow_html=True)