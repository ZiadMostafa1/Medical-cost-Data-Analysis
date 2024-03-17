import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title='Medical Cost Data Analysis', page_icon=':hospital:', layout='wide', initial_sidebar_state='expanded')

df = pd.read_csv('cleaned_data.csv')

st.title('Medical Cost Data Analysis')

# Histogram of Age
st.subheader('Histogram of Age')
fig_hist_age = go.Figure(data=[go.Histogram(x=df['age'], nbinsx=20, marker_color='skyblue')])
fig_hist_age.update_layout(bargap=0.1)  # Adjust this value to change the gap size
st.plotly_chart(fig_hist_age)

# Countplot of Sex
st.subheader('Countplot of Sex')
fig_count_sex = px.bar(df['sex'].value_counts().reset_index(), x='index', y='sex', color='index', color_discrete_sequence=['skyblue'])
st.plotly_chart(fig_count_sex)

# Charges by Age (Line Plot)
st.subheader('Charges by Age (Line Plot)')
df_avg_charges = df.groupby('age')['charges'].mean().reset_index()
fig_line_charges_age = px.line(df_avg_charges, x='age', y='charges', color_discrete_sequence=['skyblue'])
st.plotly_chart(fig_line_charges_age)

# Charges by Age (Line Plot - different color)
st.subheader('Charges by Age (Line Plot - different color)')
df_avg_charges = df.groupby('age')['charges'].mean().reset_index()
fig_line_charges_age_skyblue = px.line(df_avg_charges, x='age', y='charges', color_discrete_sequence=['orange'])
st.plotly_chart(fig_line_charges_age_skyblue)

# Barplot of Region
st.subheader('Barplot of Region')
fig_bar_region = px.bar(df['region'].value_counts().reset_index(), x='index', y='region', color='index', color_discrete_sequence=['skyblue'])
st.plotly_chart(fig_bar_region)