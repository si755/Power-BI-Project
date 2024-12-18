 import pandas as pd

# Load raw sales data
sales_data = pd.read_csv('data/sales_data_sample.csv')
category_mapping = pd.read_csv('data/product_category_mapping.csv')

# Data cleaning and transformation
sales_data['order_date'] = pd.to_datetime(sales_data['order_date'])
sales_data['profit_margin'] = (sales_data['sales_amount'] - sales_data['cost']) / sales_data['sales_amount']

# Merge with category mapping
sales_data = sales_data.merge(category_mapping, on='product_id', how='left')

# Save cleaned and transformed data
sales_data.to_csv('data/processed_sales_data.csv', index=False)
print("ETL pipeline executed successfully. Processed data saved!")

