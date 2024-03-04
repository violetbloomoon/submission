import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')

# Load your data
all_daydf = pd.read_csv("all_dataday.csv")

# Streamlit app header
st.header("Bike Sharing Dashboard Information")
st.subheader("Demografi pengaruh cuaca terhadap sewa sepeda")

# Scatter plot for 'temp' vs 'count'
fig, ax1 = plt.subplots(1, 3, figsize=(15, 5))

sns.scatterplot(
    x='temp',
    y='count',
    data=all_daydf,
    alpha=0.5,
    ax=ax1[0]
)
ax1[0].set_title('Temperature vs Count')

# Scatter plot for 'atemp' vs 'count'
sns.scatterplot(
    x='atemp',
    y='count',
    data=all_daydf,
    alpha=0.5,
    ax=ax1[1]
)
ax1[1].set_title('Feels Like Temperature vs Count')

# Scatter plot for 'hum' vs 'count'
sns.scatterplot(
    x='hum',
    y='count',
    data=all_daydf,
    alpha=0.5,
    ax=ax1[2]
)
ax1[2].set_title('Humidity vs Count')
st.pyplot(fig)

# Streamlit subheader for weekdays and weekend analysis
st.subheader("Demografi pengaruh weekdays dan weekend pada sewa sepeda")

# Bar plot based on holidays
fig, ax2 = plt.subplots(nrows=2, ncols=1, figsize=(15, 10))

sns.barplot(
    x='holiday',
    y='count',
    data=all_daydf,
    ax=ax2[0],
    color='yellow'
)
ax2[0].set_title('Banyaknya rental sepeda pada hari libur')
ax2[0].set_xlabel('Hari Libur')
ax2[0].set_ylabel('Jumlah rental sepeda')

# Bar plot based on weekdays
sns.barplot(
    x='weekday',
    y='count',
    data=all_daydf,
    ax=ax2[1]
)
ax2[1].set_title('Banyaknya rental sepeda pada hari biasa')
ax2[1].set_xlabel('Weekday')
ax2[1].set_ylabel('Jumlah rental sepeda')

# Streamlit display
st.pyplot(fig)