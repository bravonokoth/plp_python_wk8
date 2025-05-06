# PLP Python Week 8 Assignment: COVID-19 Global Data Tracker
# Project: Analyze and visualize global COVID-19 trends using Our World in Data dataset
# Objectives: Load, clean, analyze, and visualize cases, deaths, and vaccinations

# === Import Libraries ===
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime

# Set seaborn style for better visualization
sns.set(style="whitegrid")

# === 1. Data Collection ===
print("=== 1. Data Collection ===")
# Dataset: Our World in Data COVID-19 dataset (owid-covid-data.csv)
# Assumes file is in the same directory as the script
try:
    df = pd.read_csv('owid-covid-data.csv')
    print("Dataset loaded successfully!")
except FileNotFoundError:
    print("Error: 'owid-covid-data.csv' not found. Please download from https://covid.ourworldindata.org/data/owid-covid-data.csv")
    exit()
except Exception as e:
    print(f"Error loading dataset: {e}")
    exit()

# === 2. Data Loading & Exploration ===
print("\n=== 2. Data Loading & Exploration ===")

# Preview first few rows
print("\nFirst 5 rows of the dataset:")
print(df.head())

# Check columns
print("\nColumns in dataset:")
print(df.columns.tolist())

# Dataset info
print("\nDataset Info:")
print(df.info())

# Check missing values
print("\nMissing Values (selected columns):")
key_columns = ['date', 'location', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths', 'total_vaccinations', 'people_vaccinated']
print(df[key_columns].isnull().sum())

# Observations
print("\nInitial Observations:")
print("- Dataset contains global COVID-19 data by date and location.")
print("- Key columns include cases, deaths, and vaccinations.")
print("- Missing values are present, especially in vaccination data (expected for early pandemic).")

# === 3. Data Cleaning ===
print("\n=== 3. Data Cleaning ===")

# Convert date to datetime
df['date'] = pd.to_datetime(df['date'])

# Filter for specific countries (Kenya, USA, India)
countries = ['Kenya', 'United States', 'India']
df = df[df['location'].isin(countries)]

# Drop rows with missing date or location
df = df.dropna(subset=['date', 'location'])

# Handle missing numerical values (fill with 0 for cases/deaths, forward fill for vaccinations)
df['total_cases'] = df['total_cases'].fillna(0)
df['new_cases'] = df['new_cases'].fillna(0)
df['total_deaths'] = df['total_deaths'].fillna(0)
df['new_deaths'] = df['new_deaths'].fillna(0)
df['total_vaccinations'] = df['total_vaccinations'].fillna(method='ffill')
df['people_vaccinated'] = df['people_vaccinated'].fillna(method='ffill')

# Verify cleaning
print("\nMissing Values After Cleaning:")
print(df[key_columns].isnull().sum())

# Observations
print("\nCleaning Observations:")
print("- Filtered for Kenya, USA, and India.")
print("- Converted 'date' to datetime.")
print("- Filled missing cases/deaths with 0, used forward fill for vaccinations.")

# === 4. Exploratory Data Analysis (EDA) ===
print("\n=== 4. Exploratory Data Analysis ===")

# Basic statistics
print("\nBasic Statistics for Numerical Columns:")
print(df[key_columns[2:]].describe())

# Calculate death rate (total_deaths / total_cases)
df['death_rate'] = df['total_deaths'] / df['total_cases']
df['death_rate'] = df['death_rate'].fillna(0)  # Handle division by zero

# Group by country for latest data
latest_data = df[df['date'] == df['date'].max()].groupby('location').agg({
    'total_cases': 'last',
    'total_deaths': 'last',
    'total_vaccinations': 'last',
    'death_rate': 'last'
}).reset_index()

print("\nLatest Data by Country (most recent date):")
print(latest_data)

# Observations
print("\nEDA Observations:")
print("- USA has the highest total cases and deaths.")
print("- India has a high number of cases but lower death rate compared to USA.")
print("- Kenya has significantly fewer cases and deaths.")
print("- Vaccination data shows progress, but coverage varies.")

# === 5. Data Visualization ===
print("\n=== 5. Data Visualization ===")

# Create figure with subplots
plt.figure(figsize=(14, 12))

# 1. Line Chart: Total cases over time by country
plt.subplot(2, 2, 1)
for country in countries:
    country_data = df[df['location'] == country]
    plt.plot(country_data['date'], country_data['total_cases'], label=country)
plt.title('Total COVID-19 Cases Over Time')
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.legend()
plt.xticks(rotation=45)

# 2. Bar Chart: Total cases by country (latest date)
plt.subplot(2, 2, 2)
sns.barplot(x='location', y='total_cases', data=latest_data)
plt.title('Total Cases by Country (Latest Date)')
plt.xlabel('Country')
plt.ylabel('Total Cases')

# 3. Line Chart: Total vaccinations over time
plt.subplot(2, 2, 3)
for country in countries:
    country_data = df[df['location'] == country]
    plt.plot(country_data['date'], country_data['total_vaccinations'], label=country)
plt.title('Total Vaccinations Over Time')
plt.xlabel('Date')
plt.ylabel('Total Vaccinations')
plt.legend()
plt.xticks(rotation=45)

# 4. Histogram: Distribution of daily new cases (all countries)
plt.subplot(2, 2, 4)
sns.histplot(df['new_cases'], bins=30, kde=True, color='skyblue')
plt.title('Distribution of Daily New Cases')
plt.xlabel('Daily New Cases')
plt.ylabel('Frequency')

# Adjust layout and save
plt.tight_layout()
plt.savefig('covid_visualizations.png')
plt.show()

# === 6. Visualizing Vaccination Progress ===
print("\n=== 6. Visualizing Vaccination Progress ===")

# Calculate % vaccinated (people_vaccinated / population)
df['percent_vaccinated'] = df['people_vaccinated'] / df['population'] * 100
latest_vaccination = df[df['date'] == df['date'].max()].groupby('location')['percent_vaccinated'].last().reset_index()

# Bar chart for % vaccinated
plt.figure(figsize=(8, 6))
sns.barplot(x='location', y='percent_vaccinated', data=latest_vaccination)
plt.title('Percentage of Population Vaccinated (Latest Date)')
plt.xlabel('Country')
plt.ylabel('% Vaccinated')
plt.savefig('vaccination_progress.png')
plt.show()

# === 7. Insights & Reporting ===
print("\n=== 7. Insights & Reporting ===")

print("\nKey Insights:")
print("1. The USA has the highest total COVID-19 cases and deaths among the selected countries, reflecting its large population and early pandemic impact.")
print("2. India shows a high number of cases but a lower death rate, possibly due to a younger population or underreporting.")
print("3. Kenya has the lowest cases and deaths, likely due to lower testing capacity or effective early interventions.")
print("4. Vaccination progress is significant in the USA and India, with the USA leading in % vaccinated.")
print("5. Daily new cases show a right-skewed distribution, with most days having low case counts but occasional large spikes.")

print("\nInteresting Patterns:")
print("- Vaccination rollouts accelerated in 2021, with the USA and India showing steep increases.")
print("- Kenya's vaccination data is sparse, indicating slower rollout or data reporting issues.")
print("- Case spikes in India (e.g., 2021 Delta wave) are visible in the line chart.")

# End of script
print("\nScript completed. Visualizations saved as 'covid_visualizations.png' and 'vaccination_progress.png'.")
