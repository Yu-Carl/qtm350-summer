import pandas as pd
import numpy as np
import datetime

# Set seed for reproducibility
np.random.seed(42)

# Generate dates for a full year
dates = pd.to_datetime(pd.date_range(start='2023-01-01', periods=365, freq='D'))

# Generate number of accidents, with higher probability on weekends
day_of_week_effect = [1.0, 1.0, 1.1, 1.2, 1.5, 1.8, 1.6] # Mon-Sun
accidents = []
for date in dates:
    base_accidents = np.random.poisson(lam=10)
    num_accidents = int(base_accidents * day_of_week_effect[date.dayofweek])
    accidents.append(num_accidents)

# Create DataFrame
df = pd.DataFrame({
    'date': dates.date,
    'day_of_week': dates.day_name(),
    'number_of_accidents': accidents
})

# Save to CSV
df.to_csv('uk_road_accidents.csv', index=False)
print("uk_road_accidents.csv created successfully.")