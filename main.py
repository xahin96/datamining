import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# File paths for the datasets
filepaths = [
    "MY2022 Fuel Consumption Ratings.csv",
    "MY2021 Fuel Consumption Ratings.csv",
    "MY2020 Fuel Consumption Ratings(1).csv",
    "MY2015-2019 Fuel Consumption Ratings.csv",
    "MY2023 Fuel Consumption Ratings.csv"
]

# Reading each file and storing the DataFrame in a list
dfs = [pd.read_csv(filepath, encoding='ISO-8859-1') for filepath in filepaths]

# Combine all datasets into a single DataFrame
all_data = pd.concat(dfs)

# Calculating the average CO2 emissions for each make and model across the years
co2_emissions = all_data.groupby(['Model year', 'Make', 'Model'])['CO2 emissions (g/km)'].mean().reset_index()

# Pivot the data to have years as columns and makes and models as rows
co2_emissions_pivot = co2_emissions.pivot_table(index=['Make', 'Model'], columns='Model year', values='CO2 emissions (g/km)')

# Selecting 10 random make and model combinations
random_selection = co2_emissions_pivot.sample(n=2, random_state=50)

# Plotting the trends of CO2 emissions for the randomly selected makes and models over the years
plt.figure(figsize=(8, 5))
for index, row in random_selection.iterrows():
    plt.plot(row.index, row.values, marker='o', label=f"{index[0]} {index[1]}")

# Adjusting the layout to make sure labels are fully visible
plt.subplots_adjust(right=0.6)  # You can adjust the right margin according to your preference

plt.xlabel('Model Year')
plt.ylabel('Average CO2 Emissions (g/km)')
plt.title('Trend of CO2 Emissions by Make and Model Over the Years')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.show()
