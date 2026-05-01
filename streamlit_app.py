import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

st.set_page_config(page_title="HHS Operational Command", layout="wide", initial_sidebar_state="expanded")

@st.cache_data
def load_and_calculate():
    # 1. Load data - Ensure this filename is exact in GitHub
    raw_file = 'UAC_Clean_Final.csv'
    df_raw = pd.read_csv(raw_file)

    # 2. DATA ENGINE (Verbatim from your notebook)
    df = df_raw.dropna(subset=['Date']).copy()
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date').drop_duplicates(subset='Date')

    cols_to_fix = [
        'Children in CBP custody', 'Children in HHS Care',
        'Children apprehended and placed in CBP custody*',
        'Children transferred out of CBP custody',
        'Children discharged from HHS Care'
    ]
    for col in cols_to_fix:
        if df[col].dtype == 'object':
            df[col] = df[col].astype(str).str.replace(',', '').str.strip()
        df[col] = pd.to_numeric(df[col], errors='coerce')

    df = df.fillna(0)
    df['Total_System_Load'] = df['Children in CBP custody'] + df['Children in HHS Care']
    df['Net_Intake_Pressure'] = df['Children transferred out of CBP custody'] - df['Children discharged from HHS Care']
    df['Cumulative_Backlog'] = df['Net_Intake_Pressure'].cumsum()

    # Strain Logic (Target: 69 Days)
    load_75th = df['Total_System_Load'].quantile(0.75)
    volatility = df['Children apprehended and placed in CBP custody*'].rolling(window=7).std().fillna(0)
    df['System_Strain'] = (df['Total_System_Load'] > load_75th) & (volatility > volatility.quantile(0.75))
    df['Volatility_Index'] = volatility

    # Pre-caching global stats for static display
    total_in = df['Children transferred out of CBP custody'].sum()
    total_out = df['Children discharged from HHS Care'].sum()

    stats = {
        'total_in': total_in,
        'total_out': total_out,
        'ratio': total_in / total_out if total_out > 0 else 0,
        'strain_sum': int(df['System_Strain'].sum()),
        'avg_load': df['Total_System_Load'].mean(),
        'latest_hhs': df['Children in HHS Care'].iloc[-1],
        'min_date': df['Date'].min(),
        'max_date': df['Date'].max()
    }
    return df, stats

df_full, stats = load_and_calculate()

# --- SIDEBAR ---
with st.sidebar:
    st.header("⚙️ Dashboard Controls")
    date_range = st.date_input(
        "Select Analysis Period",
        value=(stats['min_date'], stats['max_date']),
        min_value=stats['min_date'],
        max_value=stats['max_date']
    )
    st.divider()
    st.success(f"Audit Status: {len(df_full)} Rows Cleaned")

# Filter data
if len(date_range) == 2:
    start_date, end_date = pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])
    df = df_full[(df_full['Date'] >= start_date) & (df_full['Date'] <= end_date)]
else:
    df = df_full

# --- HEADER ---
st.title("🛡️ HHS/CBP Operational Command Center")
st.subheader("System Performance & Capacity Strain Analytics")
st.divider()

# --- INSTANT KPI METRICS (Matching your screenshot)[cite: 1] ---
m1, m2, m3, m4 = st.columns(4)
m1.metric("Active HHS Care", f"{stats['latest_hhs']:,.0f}", delta="+Fixed Thousand-Units")
m2.metric("Discharge Ratio", f"{stats['ratio']:.2f}", delta="-26% vs Target", delta_color="red")
m3.metric("Critical Strain Days", f"{stats['strain_sum']}", help="Days where Load & Volatility > 75th percentile")
m4.metric("Mean System Load", f"{stats['avg_load']:.0f}")

st.divider()

# --- VISUALIZATION SUITE ---
tabs = st.tabs(["📊 Capacity (Fig 1-4)", "🔄 Throughput (Fig 5 & 8)", "⚠️ Strain Analysis (Fig 6-7)"])

with tabs[0]:
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("### Figure 1: Unified System Load")
        fig1 = px.line(df, x='Date', y='Total_System_Load', color_discrete_sequence=['#2E86C1'])
        fig1.add_hline(y=stats['avg_load'], line_dash="dash", line_color="red", annotation_text="Historical Mean")
        st.plotly_chart(fig1, use_container_width=True)
    with c2:
        st.markdown("### Figure 2: Agency Responsibility")
        fig2 = px.area(df, x='Date', y=['Children in CBP custody', 'Children in HHS Care'],
                      color_discrete_map={'Children in CBP custody': '#34495e', 'Children in HHS Care': '#3498db'})
        st.plotly_chart(fig2, use_container_width=True)

with tabs[1]:
    st.markdown("### Figure 5: Monthly Throughput Balance")
    monthly_df = df.set_index('Date')[['Children transferred out of CBP custody', 'Children discharged from HHS Care']].resample('ME').sum().reset_index()
    fig5 = go.Figure()
    fig5.add_trace(go.Bar(x=monthly_df['Date'], y=monthly_df['Children transferred out of CBP custody'], name='Intake', marker_color='#27ae60'))
    fig5.add_trace(go.Bar(x=monthly_df['Date'], y=monthly_df['Children discharged from HHS Care'], name='Discharge', marker_color='#e67e22'))
    fig5.update_layout(barmode='group', xaxis_tickformat='%b %Y')
    st.plotly_chart(fig5, use_container_width=True)

    st.markdown("### Figure 8: Cumulative Backlog Growth")
    fig8 = px.line(df, x='Date', y='Cumulative_Backlog', color_discrete_sequence=['#C0392B'])
    st.plotly_chart(fig8, use_container_width=True)

with tabs[2]:
    st.markdown("### Figure 6: Identification of Acute Strain")
    fig6 = px.line(df, x='Date', y='Total_System_Load', color_discrete_sequence=['#bdc3c7'])
    strain_pts = df[df['System_Strain']]
    fig6.add_trace(go.Scatter(x=strain_pts['Date'], y=strain_pts['Total_System_Load'], mode='markers', marker=dict(color='red', size=6), name='Strain Event'))
    st.plotly_chart(fig6, use_container_width=True)

    st.markdown("### Figure 7: Care Load Volatility")
    fig7 = px.line(df, x='Date', y='Volatility_Index', color_discrete_sequence=['#8E44AD'])
    st.plotly_chart(fig7, use_container_width=True)
