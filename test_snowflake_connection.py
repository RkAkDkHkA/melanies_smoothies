import streamlit as st
from snowflake.snowpark.context import get_active_session
from snowflake.connector import connect

st.title("🔍 Snowflake Connection Test")

try:
    # Try connecting directly using your secrets
    conn = connect(
        account="GKSGURB.IK89600",
        user="IK89600",
        private_key_file="C:\Users\deepa\rsa_key.p8",
        warehouse="COMPUTE_WH",
        database="SMOOTHIES",
        schema="PUBLIC",
        role="SYSADMIN"
    )
    st.success("✅ Connection successful!")
except Exception as e:
    st.error(f"❌ Connection failed: {e}")
