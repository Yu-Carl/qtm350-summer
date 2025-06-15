import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the data
df = pd.read_csv('uk_road_accidents.csv')

# --- Analysis ---
# Calculate average accidents per day of the week
avg_accidents_by_day = df.groupby('day_of_week')['number_of_accidents'].mean().round(2)
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
avg_accidents_by_day = avg_accidents_by_day.reindex(day_order)

most_accidents_day = avg_accidents_by_day.idxmax()
highest_avg = avg_accidents_by_day.max()

# --- Save Summary Statistics ---
with open('summary_stats.txt', 'w') as f:
    f.write('Road Accident Data Summary\n')
    f.write('==========================\n')
    f.write(f'Day with most accidents on average: {most_accidents_day}\n')
    f.write(f'Highest average number of accidents: {highest_avg}\n')
print("summary_stats.txt created successfully.")

# --- Create Visualisation ---
plt.figure(figsize=(10, 6))
sns.barplot(x=avg_accidents_by_day.index, y=avg_accidents_by_day.values)
plt.title('Average Number of Road Accidents by Day of the Week', fontsize=16)
plt.xlabel('Day of the Week')
plt.ylabel('Average Number of Accidents')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('accident_plot.png')
print("Plot saved to accident_plot.png")