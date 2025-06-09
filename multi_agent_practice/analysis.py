import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming df is your DataFrame with columns 'category', 'revenue'
plt.figure(figsize=(10, 6))
sns.barplot(x='category', y='revenue', data=df, palette='viridis')
plt.title('Percentage of Total Revenue by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Revenue (in millions)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()