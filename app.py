import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Logistics Optimization Dashboard", layout="wide")

df = pd.read_csv('logistics_data.csv')

st.sidebar.header("🌍 External Factors & Stress Test")

fuel_price_input = st.sidebar.slider("Current Fuel Price (TRY/L)", min_value=30.0, max_value=70.0, value=44.20)
fuel_increase_pct = ((fuel_price_input - 44.20) / 44.20) * 100

deadhead_rate = st.sidebar.slider("Deadhead Ratio (%)", 0, 50, 20)
is_winter = st.sidebar.checkbox("Is it winter season?")
winter_delay_multiplier = 1.25 if is_winter else 1.0

df['route'] = df['origin'] + " -> " + df['destination']
df['fixed_cost'] = 3500 

df['actual_duration_hrs'] = df['actual_duration_hrs'] * winter_delay_multiplier
df['is_delayed'] = (df['actual_duration_hrs'] > (df['planned_duration_hrs'] + 1)).astype(int)
df['on_time'] = (df['is_delayed'] == 0).astype(int)


df['fuel_cost'] = (df['distance_km'] / 100) * 35 * fuel_price_input
df['delay_cost'] = (df['actual_duration_hrs'] - df['planned_duration_hrs']).clip(lower=0) * 250
cargo_handling_map = {'Dry': 500, 'Cold_Chain': 1500, 'Hazardous': 2000, 'Oversized': 3000}
df['handling_cost'] = df['cargo_type'].map(cargo_handling_map)
df['deadhead_cost'] = (df['fuel_cost'] + df['fixed_cost']) * (deadhead_rate / 100)


df['total_cost_calculated'] = (df['fuel_cost'] + df['delay_cost'] + 
                               df['handling_cost'] + df['fixed_cost'] + 
                               df['deadhead_cost'])

high_delay_routes = df.groupby('route')['is_delayed'].mean()
worst_route = high_delay_routes.idxmax()
worst_route_delay = high_delay_routes.max() * 100
annual_opt_potential = (df['delay_cost'].sum() * 0.20) + (df['deadhead_cost'].sum() * 0.15)

st.title("Logistics Intelligence & Optimization Dashboard")

with st.expander("📝 EXECUTIVE SUMMARY & STRATEGIC OVERVIEW", expanded=True):
    total_saving_pct = (annual_opt_potential / df['total_cost_calculated'].sum()) * 100
    st.markdown(f"""
    * **Optimization Potential:** Identified a **{total_saving_pct:.1f}%** reduction in total operational costs through route and return-load optimization.
    * **Key Bottleneck:** High congestion at major port gates is driving **{df['is_delayed'].mean()*100:.1f}%** of delays, primarily affecting the **{worst_route}** corridor.
    * **Urgent Action:** Implementing the *AI-Driven Decision Support* recommendations could save approximately **{annual_opt_potential:,.0f} TL** annually.
    """)

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Total Shipments", f"{len(df)}")
col2.metric("Avg. Cost (TRY)", f"{df['total_cost_calculated'].mean():,.0f} TL")
col3.metric("Avg Delay Rate", f"%{df['is_delayed'].mean() * 100:.2f}")
col4.metric("On-Time Delivery", f"%{df['on_time'].mean() * 100:.1f}")
col5.metric("Potential Saving", f"{annual_opt_potential:,.0f} TL", delta="Optimization", delta_color="normal")

st.write("### 🚨 Stress Test Impact Analysis")
s_col1, s_col2, s_col3 = st.columns(3)
with s_col1:
    st.warning(f"**Fuel Price Impact:** {fuel_increase_pct:.1f}% change in fuel index.")
with s_col2:
    st.error(f"**Deadhead Loss:** {df['deadhead_cost'].sum():,.0f} TRY hidden cost.")
with s_col3:
    status = "❄️ Winter Mode Active" if is_winter else "☀️ Summer Mode"
    st.info(f"**Status:** {status} (25% delay penalty if active)")

st.divider()

c1, c2 = st.columns(2)
with c1:
    st.subheader("Route Based Cost Analysis")
    fig_cost = px.bar(df.groupby('route')['total_cost_calculated'].mean().reset_index(),
                      x='route', y='total_cost_calculated', color='total_cost_calculated',
                      title="Average Total Cost per Route (Incl. Deadhead)")
    st.plotly_chart(fig_cost, use_container_width=True)

with c2:
    st.subheader("Delay Distribution by Weather")
    fig_delay = px.box(df, x='weather', y='actual_duration_hrs', color='weather',
                       title="Transit Duration Variance by Weather Condition")
    st.plotly_chart(fig_delay, use_container_width=True)

st.divider()

col_a, col_b = st.columns(2)
with col_a:
    st.subheader("💰 Cost Composition by Route")
    cost_cols = ['fuel_cost', 'delay_cost', 'handling_cost', 'fixed_cost', 'deadhead_cost']
    cost_comp = df.groupby('route')[cost_cols].mean().reset_index()
    fig_stack = px.bar(cost_comp, x='route', y=cost_cols, barmode='stack', title="Cost Breakdown")
    st.plotly_chart(fig_stack, use_container_width=True)

with col_b:
    st.subheader("🧠 Correlation Analysis (Root Cause)")
    corr_features = ['distance_km', 'actual_duration_hrs', 'delay_cost', 'port_congestion_level', 'is_delayed']
    corr_df = df[corr_features].corr()
    fig_heat = px.imshow(corr_df, text_auto=True, color_continuous_scale='RdBu_r', title="Delay Drivers")
    st.plotly_chart(fig_heat, use_container_width=True)

st.divider()
st.header("🤖 AI-Driven Decision Support Engine")
st.markdown("Automated recommendations based on real-time operational constraints.")

potential_savings_cons = df[df['cargo_type'] == 'Dry']['total_cost_calculated'].sum() * 0.12

rec_col1, rec_col2 = st.columns(2)
with rec_col1:
    st.subheader("📍 Route & Delay Recommendations")
    if worst_route_delay > 50:
        st.error(f"**Action Required on {worst_route}:**")
        st.write(f"This route has a **{worst_route_delay:.1f}%** delay rate. Logic suggests shifting non-urgent cargo to rail or alternative ports.")
    
    if is_winter:
        st.warning("**Seasonal Buffer Alert:**")
        st.write("Winter conditions are adding 25% to transit times. Adjust client ETAs immediately.")

with rec_col2:
    st.subheader("💰 Financial & Cargo Optimization")
    st.success("**Consolidation Opportunity:**")
    st.write(f"By combining 'Dry Cargo' shipments, you can achieve an estimated **{potential_savings_cons:,.0f} TL** reduction in costs.")
    
    high_cong_ports = df[df['port_congestion_level'] > 7]['origin'].unique()
    if len(high_cong_ports) > 0:
        st.info("**Gate-in Optimization:**")
        st.write(f"High congestion at **{', '.join(high_cong_ports)}**. Suggesting night-shift gate-ins.")

st.write("---")
st.subheader("🛠️ Strategic Intervention Simulator")
efficiency_gain = st.slider("Target Congestion Reduction (%)", 0, 50, 10)
simulated_cost_saving = (df['delay_cost'].sum() * (efficiency_gain / 100))
st.write(f"💡 **Result:** Improving port efficiency by {efficiency_gain}% would save **{simulated_cost_saving:,.2f} TL** in delay penalties.")