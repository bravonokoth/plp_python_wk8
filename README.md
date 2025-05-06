# PLP Python Week 8 Assignment: COVID-19 Global Data Tracker

## Project Overview
This project analyzes global COVID-19 trends using the Our World in Data dataset. We focus on Kenya, USA, and India, examining cases, deaths, and vaccinations over time. The analysis includes data cleaning, exploratory data analysis (EDA), and visualizations to uncover trends and insights.

## Data Source
- **Dataset**: Our World in Data COVID-19 dataset (`owid-covid-data.csv`)
- **Source**: https://covid.ourworldindata.org/data/owid-covid-data.csv
- **Key Columns**: `date`, `location`, `total_cases`, `new_cases`, `total_deaths`, `new_deaths`, `total_vaccinations`, `people_vaccinated`

## Methodology
1. **Data Loading**: Loaded CSV using pandas.
2. **Cleaning**: Filtered for three countries, converted dates, handled missing values.
3. **EDA**: Computed statistics, death rates, and latest metrics.
4. **Visualizations**: Created line charts, bar charts, and histograms using matplotlib and seaborn.
5. **Vaccination Analysis**: Calculated and visualized % vaccinated.
6. **Reporting**: Summarized key insights and patterns.

## Key Insights
1. The USA leads in total cases and deaths, reflecting its large population and early pandemic impact.
2. India has high cases but a lower death rate, possibly due to demographic factors.
3. Kenya reports the lowest cases and deaths, potentially due to limited testing.
4. Vaccination progress is strongest in the USA, followed by India, with Kenya lagging.
5. Daily new cases are right-skewed, with occasional large spikes.

## Visualizations
See the plots below for trends in cases, deaths, vaccinations, and daily case distributions.

## Conclusion
This analysis highlights significant differences in COVID-19 impact and vaccination progress across Kenya, USA, and India. Future work could include choropleth maps or additional countries for broader comparisons.
