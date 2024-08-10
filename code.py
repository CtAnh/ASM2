import pandas as pd

# Điều chỉnh đường dẫn tới các file CSV trên hệ thống của bạn
customer_df = pd.read_csv('D:/Python Code/ASM2/Customer_Table.csv')
market_trend_df = pd.read_csv('D:/Python Code/ASM2/Market_Trend_Table.csv')
product_detail_df = pd.read_csv('D:/Python Code/ASM2/Product_Detail_Table.csv')
product_group_df = pd.read_csv('D:/Python Code/ASM2/Product_Group_Table.csv')
sale_df = pd.read_csv('D:/Python Code/ASM2/Sale_Table.csv')
website_access_df = pd.read_csv('D:/Python Code/ASM2/Website_Access_Category_Table.csv')

# Function to fill NaN values based on column dtype
def fill_na_with_default(df):
    for column in df.columns:
        if df[column].dtype == 'float64' or df[column].dtype == 'int64':
            df[column] = df[column].fillna(0)  # Fill numeric columns with 0
        else:
            df[column] = df[column].fillna('Unknown')  # Fill non-numeric columns with 'Unknown'

# Fill NaN values for each dataframe
fill_na_with_default(customer_df)
fill_na_with_default(market_trend_df)
fill_na_with_default(product_detail_df)
fill_na_with_default(product_group_df)
fill_na_with_default(sale_df)
fill_na_with_default(website_access_df)

# Combine the dataframes into one dataframe
combined_df = pd.concat([customer_df, market_trend_df, product_detail_df, product_group_df, sale_df, website_access_df], axis=0, ignore_index=True)

# Save the combined dataframe to a new CSV file
output_file_path = 'D:/Python Code/ASM2/Combined_Data_Filled.csv'
combined_df.to_csv(output_file_path, index=False)

print(output_file_path)
 # type: ignore