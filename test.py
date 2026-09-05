import os
import streamlit as st
import os
from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col, when_matched

st.write("Current working directory:", os.getcwd())
