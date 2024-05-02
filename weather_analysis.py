import pandas as pd

data = pd.read_csv(r"./weather_data.csv")

# TASK: Find all the unique 'Wind Speed' values in the data.
unique_wind_speed = data["Wind Speed_km/h"].unique()

# TASK: Find the number of times of 'Clear' weather.
clear_weather = data.value_counts("Weather").get("Clear")

# TASK: Find the number of times Wind Speed was exactly 4 km/h.
wind_speed_totals = data.value_counts("Wind Speed_km/h").get(4)

# TASK: Find all null values in the data
null_values = data.isnull().sum()

# TASK: Rename column name 'Weather' to 'Weather Condition'
renamed = data.rename(columns={"Weather": "Weather Condition"})

# TASK: Calculate the mean of 'Visibility_km' (average)
average_visibility = data["Wind Speed_km/h"].mean()

# Calculate standard deviation of pressure
# NOTE: About standard deviation:
# It's a measure of the amount of variation or dispersion of the values from the mean.
# https://en.wikipedia.org/wiki/Standard_deviation
pressure_std = data["Press_kPa"].std()

# Calculate the variance of relative humidity
hum_variance = data["Rel Hum_%"].var()

# How many snow occurrences are in the data?
snow_total = (
    data["Weather"].str.contains("Snow").sum()
)  # false is 0 while true is 1, that's why sum works

# Find all instances where wind speed is above 30 and visibility is 25
wind_speed_with_visibility_occ = data[
    (data["Wind Speed_km/h"] > 30) & (data["Visibility_km"] == 25)
]

# Show records where the weather is fog
fog_records = data[data["Weather"] == "Fog"]

# Find instances of weather clear or visibility above 35
clear_or_visibility = data[(data["Weather"] == "Clear") | (data["Visibility_km"] > 35)]

# Find instances where the weather is clear and relative humidity is above 50, or visibility is above 40
weather_clear_and_humid_or_visibility = data[
    ((data["Weather"] == "Clear") & (data["Rel Hum_%"] > 50))
    | (data["Visibility_km"] > 40)
]
