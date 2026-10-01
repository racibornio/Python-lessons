# Import the required dependencies
import pandas as pd

# Assuming df is a list of DataFrames and df is the DataFrame we are working with
df = df

# Find the record with the most stable pace
most_stable_record = df.loc[df['Tempo Stabilność'].abs().idxmin()]

# Declare result variable
result = {
    "type": "dataframe",
    "value": most_stable_record.to_frame().T  # Convert the Series to a DataFrame for consistency
}






import pandas as pd

# Assuming df is a list of DataFrames and we are working with the first DataFrame
df = df

# Filter out countries with more than 10 participants
country_counts = df['Kraj'].value_counts()
countries_with_more_than_10 = country_counts[country_counts > 10].index

# Initialize lists to store results
most_stable_participants = []
least_stable_participants = []

# Iterate over each country
for country in countries_with_more_than_10:
    # Filter participants from the current country
    country_participants = df[df['Kraj'] == country]

    # Find the participant with the most stable pace
    most_stable = country_participants.loc[country_participants['Tempo Stabilność'].idxmin()]
    most_stable_participants.append(most_stable)

    # Find the participant with the least stable pace
    least_stable = country_participants.loc[country_participants['Tempo Stabilność'].idxmax()]
    least_stable_participants.append(least_stable)

# Combine results into a single DataFrame
result_df = pd.DataFrame(most_stable_participants + least_stable_participants)






import pandas as pd

# Load the dataframe
df = df

# Filter the top 21 and bottom 50 participants based on 'Miejsce'
top_21 = df.nsmallest(21, 'Miejsce')
bottom_50 = df.nlargest(50, 'Miejsce')

# Calculate the mean pace for each measurement point for both groups
top_21_mean_pace = top_21[['5 km Tempo', '10 km Tempo', '15 km Tempo', '20 km Tempo']].mean()
bottom_50_mean_pace = bottom_50[['5 km Tempo', '10 km Tempo', '15 km Tempo', '20 km Tempo']].mean()

# Calculate the standard deviation of the mean pace for each group
top_21_std_dev = top_21_mean_pace.std()
bottom_50_std_dev = bottom_50_mean_pace.std()

# Declare result var
result = {
    "type": "dataframe",
    "value": pd.DataFrame({
        "Group": ["Top 21", "Bottom 50"],
        "Standard Deviation": [top_21_std_dev, bottom_50_std_dev]
    })
}