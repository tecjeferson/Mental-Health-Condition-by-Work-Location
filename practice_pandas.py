import pandas as pd
from IPython.display import display
import streamlit as st
import matplotlib.pyplot as plt

remotework_datapath = "Impact_of_Remote_Work_on_Mental_Health.csv"
remotework_csv = pd.read_csv(
    remotework_datapath, encoding="unicode_escape")

#Men and woman which work remote and hybrid 
men_hybrid = remotework_csv[(remotework_csv['Gender'] == 'Male') &
              (remotework_csv['Work_Location'] == 'Hybrid')]
woman_hybrid = remotework_csv[(remotework_csv['Gender'] == 'Female') &
              (remotework_csv['Work_Location'] == 'Hybrid')]
men_remote= remotework_csv[(remotework_csv['Gender'] == 'Male') &
              (remotework_csv['Work_Location'] == 'Remote')]
woman_remote= remotework_csv[(remotework_csv['Gender'] == 'Female') &
              (remotework_csv['Work_Location'] == 'Remote')]

# Mental health condition by region for men
mental_men_region = remotework_csv[
    (remotework_csv['Gender'] == 'Male') &
    (remotework_csv['Mental_Health_Condition'].notna()) &
    (remotework_csv['Work_Location'].isin(['Remote', 'Hybrid','Other'])) &
    (remotework_csv['Region'] == 'South America')
]

# Mental health condition by region for woman
mental_woman_region = remotework_csv[
    (remotework_csv['Gender'] == 'Female') &
    (remotework_csv['Mental_Health_Condition'].notna()) &
    (remotework_csv['Work_Location'].isin(['Remote', 'Hybrid','Other'])) &
    (remotework_csv['Region'] == 'South America')
]

men_health_grouped = mental_men_region.groupby(['Mental_Health_Condition', 'Work_Location', 'Region']).size().unstack()
woman_health_grouped = mental_woman_region.groupby(['Mental_Health_Condition', 'Work_Location', 'Region']).size().unstack()

st.title("MEN: Mental Health and Work Location Analysis in South America")
st.subheader("Men Grouped Data")
st.write(men_health_grouped)

st.subheader("Woman Grouped Data")
st.write(woman_health_grouped)

# Bar chart for men
st.subheader("Mental Health Condition by Work Location")
chart_data = men_health_grouped.fillna(0)  # Preenche NaN com 0 para o gráfico

fig, ax = plt.subplots()
chart_data.plot(kind='barh', stacked=True, ax=ax)
ax.set_xlabel("Mental Health Condition")
ax.set_ylabel("Count")
ax.set_title("Men: Distribution of Work Locations by Mental Health Condition")
st.pyplot(fig)

# Bar chart for woman
chart_data = woman_health_grouped.fillna(0)  # Preenche NaN com 0 para o gráfico

fig, ax = plt.subplots()
chart_data.plot(kind='barh', stacked=True, ax=ax)
ax.set_xlabel("Mental Health Condition")
ax.set_ylabel("Count")
ax.set_title("Woman: Distribution of Work Locations by Mental Health Condition")
st.pyplot(fig)

display(f"Mental health condition in South America by work location:\n \
{men_health_grouped} ")