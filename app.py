# app.py

import streamlit as st
import pandas as pd

from modules.scorer import score_leads
from modules.strategy import generate_strategy

# Streamlit page config
st.set_page_config(page_title="EngageAI", layout="wide")

# 🎨 Hero section
st.markdown("""
<h1 style='text-align: center; color: #4A90E2;'>🤖 EngageAI</h1>
<h4 style='text-align: center; color: gray;'>Smart Lead Prioritization & Outreach Strategy Generator</h4>
""", unsafe_allow_html=True)
st.markdown("---")

# Sidebar info
st.sidebar.title("⚙️ Settings")
st.sidebar.info("""
Upload a CSV of enriched leads and instantly get:

✅ Lead Scores  
✅ Engagement Channels  
✅ CTA Suggestions  
✅ Exportable CSV  
""")

# Upload section
uploaded_file = st.file_uploader("📤 Upload your enriched lead CSV", type=["csv"])

if uploaded_file:
    # Read and clean CSV
    df = pd.read_csv(uploaded_file)
    df.columns = df.columns.str.strip()  # Clean column names

    # Debug
    # st.write("📌 Column names:", df.columns.tolist())

    st.subheader("📊 Uploaded Lead Data")
    st.dataframe(df, use_container_width=True)

    # Required columns
    required_cols = ["Company", "Industry", "Employees", "Funding"]
    if not all(col in df.columns for col in required_cols):
        st.error("❌ Required columns missing: Make sure your CSV includes Company, Industry, Employees, and Funding")
    else:
        # Lead scoring
        df = score_leads(df)

        # Generate engagement strategy
        df = generate_strategy(df)

        st.markdown("---")
        st.subheader("🎯 Engagement Strategy")

        # Filters
        col1, col2 = st.columns(2)

        with col1:
            temp_filter = st.multiselect(
                "🔥 Filter by Lead Temperature",
                options=df["Lead Temperature"].unique(),
                default=df["Lead Temperature"].unique()
            )

        with col2:
            channel_filter = st.multiselect(
                "📡 Filter by Outreach Channel",
                options=df["Best Channel"].unique(),
                default=df["Best Channel"].unique()
            )

        # Filter dataframe
        filtered_df = df[
            df["Lead Temperature"].isin(temp_filter) &
            df["Best Channel"].isin(channel_filter)
        ]

        # Display final table
        st.markdown("### 🧠 Suggested Outreach Plan")
        st.dataframe(filtered_df, use_container_width=True)

        # Download CSV
        st.download_button(
            label="📥 Download Strategy CSV",
            data=filtered_df.to_csv(index=False).encode("utf-8"),
            file_name="engagement_strategy.csv",
            mime="text/csv"
        )

        st.markdown("---")
        st.markdown("<div style='text-align: center; color: gray;'>Built with ❤️ by Ramya for SaaSquatch</div>", unsafe_allow_html=True)

else:
    st.info("Please upload a CSV file to begin.")
