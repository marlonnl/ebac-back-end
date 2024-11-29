import pandas as pd

customers = {
    "customer_id": [1, 2, 3, 4, 5, 6],
    "name": ["Ella", "David", "Zachary", "Alice", "Finn", "Violet"],
    "email": [
        "emily.example.com",
        "michael@example.com",
        "sarah@example.com",
        "john@example.com",
        "john@example.com",
        "alice@example.com",
    ],
}

customers_df = pd.DataFrame(customers)
print(customers_df)

print(customers_df.drop_duplicates(['email'], keep='last'))