import pandas as pd

# Muat data dari file CSV dengan delimiter ;
df_customer = pd.read_csv('Case Study - Customer.csv', delimiter=';')
df_store = pd.read_csv('Case Study - Store.csv', delimiter=';')
df_product = pd.read_csv('Case Study - Product.csv', delimiter=';')
df_transaction = pd.read_csv('Case Study - Transaction.csv', delimiter=';')

# Asumsikan ada kolom tambahan di transaction yang menunjukkan CustomerID dan StoreID dan ProductID
# Gabungkan df_transaction dengan df_customer, df_store, dan df_product berdasarkan ID yang sesuai
merged_data = df_transaction.merge(df_customer, on='CustomerID', how='left').merge(df_store, on='StoreID', how='left').merge(df_product, on='ProductID', how='left')

# Menyimpan data yang telah digabungkan ke file CSV baru dengan delimiter ;
merged_data.to_csv('merged_data.csv', sep=';', index=False)
