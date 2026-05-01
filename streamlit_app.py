import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

st.set_page_config(page_title="HHS Operational Command", layout="wide", initial_sidebar_state="expanded")

@st.cache_data
def load_and_calculate():
    # 1. Load the raw data
    data = pd.read_csv('HHS_Unaccompanied_Alien_Children_Program.csv')
    
    # 2. Convert Date
    data['Date'] = pd.to_datetime(data['Date'])
    
    # 3. FORCE Numeric Conversion (The fix for your TypeError)
    numeric_cols = [
        'Children in CBP custody', 
        'Children in HHS Care', 
        'Children transferred out of CBP custody', 
        'Children discharged from HHS Care',
        'Children apprehended and placed in CBP custody*'
    ]
    
    for col in numeric_cols:
        # Remove commas and convert to numeric, forcing errors to NaN
        if data[col].dtype == 'object':
            data[col] = data[col].str.replace(',', '', regex=True)
        data[col] = pd.to_numeric(data[col], errors='coerce').fillna(0)

    # 4. Feature Engineering
    data['Total_System_Load'] = data['Children in CBP custody'] + data['Children in HHS Care']
    
    load_threshold = data['Total_System_Load'].quantile(0.75)
    data['System_Strain'] = data['Total_System_Load'] > load_threshold
    
    data['Volatility_Index'] = data['Total_System_Load'].rolling(window=7).std().fillna(0)
    
    data['Daily_Diff'] = data['Children transferred out of CBP custody'] - data['Children discharged from HHS Care']
    data['Cumulative_Backlog'] = data['Daily_Diff'].cumsum()

    # 5. Global Stats
    stats = {
        'total_in_full': data['Children transferred out of CBP custody'].sum(),
        'total_out_full': data['Children discharged from HHS Care'].sum(),
        'strain_sum_full': int(data['System_Strain'].sum()),
        'avg_load_full': data['Total_System_Load'].mean(),
        'latest_hhs_full': data['Children in HHS Care'].iloc[-1],
        'min_date': data['Date'].min(),
        'max_date': data['Date'].max()
    }
    return data, stats

df_full, stats = load_and_calculate()

# --- SIDEBAR CONTROLS ---
with st.sidebar:
    st.header("⚙️ Dashboard Controls")
    date_range = st.date_input(
        "Select Analysis Period",
        value=(stats['min_date'], stats['max_date']),
        min_value=stats['min_date'],
        max_value=stats['max_date']
    )
    st.divider()
    st.success(f"System Ready: {len(df_full)} Rows Analyzed")

# Filter logic
if len(date_range) == 2:
    start_date, end_date = pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])
    df = df_full[(df_full['Date'] >= start_date) & (df_full['Date'] <= end_date)]
else:
    df = df_full

# Metrics
total_in_filtered = df['Children transferred out of CBP custody'].sum()
total_out_filtered = df['Children discharged from HHS Care'].sum()
discharge_ratio = total_in_filtered / total_out_filtered if total_out_filtered > 0 else 0

# --- UI LAYOUT ---
st.title("🛡️ HHS/CBP Operational Command Center")
st.subheader("System Performance & Capacity Strain Analytics")
st.divider()

m1, m2, m3, m4 = st.columns(4)
m1.metric("Active HHS Care", f"{df['Children in HHS Care'].iloc[-1]:,.0f}")
m2.metric("Discharge Ratio", f"{discharge_ratio:.2f}")
m3.metric("Critical Strain Days", f"{int(df['System_Strain'].sum())}")
m4.metric("Mean System Load", f"{df['Total_System_Load'].mean():.0f}")

st.divider()

# --- TABS ---
tabs = st.tabs(["📊 Capacity", "🔄 Throughput", "⚠️ Strain Analysis"])

with tabs[0]:
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("### Unified System Load")
        fig1 = px.line(df, x='Date', y='Total_System_Load', color_discrete_sequence=['#2E86C1'])
        st.plotly_chart(fig1, use_container_width=True)
    with c2:
        st.markdown("### Agency Responsibility")
        fig2 = px.area(df, x='Date', y=['Children in CBP custody', 'Children in HHS Care'])
        st.plotly_chart(fig2, use_container_width=True)

with tabs[1]:
    st.markdown("### Cumulative Backlog Growth")
    fig8 = px.line(df, x='Date', y='Cumulative_Backlog', color_discrete_sequence=['#C0392B'])
    st.plotly_chart(fig8, use_container_width=True)

with tabs[2]:
    st.markdown("### Identification of Acute Strain")
    fig6 = px.line(df, x='Date', y='Total_System_Load', color_discrete_sequence=['#bdc3c7'])
    strain_pts = df[df['System_Strain']]
    fig6.add_trace(go.Scatter(x=strain_pts['Date'], y=strain_pts['Total_System_Load'], mode='markers', marker=dict(color='red'), name='Strain Event'))
    st.plotly_chart(fig6, use_container_width=True)
