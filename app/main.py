import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Title and Intro
st.title("Solar Radiation Dashboard")
st.write("Analysis of Solar Farm Data from Benin, Sierra Leone, and Togo")

# 2. Load Data (Use the cleaned data)
@st.cache_data
def load_data():
    
    benin = pd.read_csv('data/benin_clean.csv')
    sierra = pd.read_csv('data/sierraleone_clean.csv')
    togo = pd.read_csv('data/togo_clean.csv')
    benin['Country'] = 'Benin'
    sierra['Country'] = 'Sierra Leone'
    togo['Country'] = 'Togo'
    return pd.concat([benin, sierra, togo], axis=0)

try:
    df = load_data()
except:
    st.error("Data not found. Please run the EDA notebooks to generate cleaned CSVs in the data/ folder.")
    st.stop()

# 3. Sidebar Widgets
st.sidebar.header("Filters")
selected_country = st.sidebar.selectbox("Select Country", df['Country'].unique())

# 4. Filter Data
country_data = df[df['Country'] == selected_country]

# 5. Main Visuals
st.subheader(f"GHI Distribution for {selected_country}")
fig, ax = plt.subplots()
sns.histplot(country_data['GHI'], kde=True, ax=ax, color='orange')
st.pyplot(fig)

st.subheader("Correlation Matrix")
# Selecting only numeric columns for correlation
numeric_cols = ['GHI', 'DNI', 'DHI', 'Tamb', 'WS']
corr = country_data[numeric_cols].corr()
fig2, ax2 = plt.subplots()
sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax2)
st.pyplot(fig2)