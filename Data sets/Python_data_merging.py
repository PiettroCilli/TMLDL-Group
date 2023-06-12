
import pandas as pd
aisles = pd.read_csv("aisles.csv") 
departments = pd.read_csv("departments.csv") 
orders_prior = pd.read_csv("order_products__prior.csv")
orders_train = pd.read_csv("order_products__train.csv") 
orders = pd.read_csv("orders.csv") 
products = pd.read_csv("products.csv") 
#
orders.head()

#Transform characters to categorical variables
aisles['aisle'] = aisles['aisle'].astype('category')
departments['department'] = departments['department'].astype('category')
orders['eval_set'] = orders['eval_set'].astype('category')
products['product_name'] = products['product_name'].astype('category')

merged = pd.merge(orders, orders_prior, on = "order_id" )
merged2 = pd.merge(merged, products, on = "product_id" )
merged3 = pd.merge(merged2, aisles, on = "aisle_id" )
merged4 = pd.merge(merged3, departments, on = "department_id" )

finaldf = merged4
finaldf.head()

# Take a random sample of 10,000 rows
final10000 = finaldf.sample(n=10000, random_state=42)

# Take a random sample of 100,000 rows
final100000 = finaldf.sample(n=100000, random_state=42)

# Take a random sample of 1,000,000 rows
final1000000 = finaldf.sample(n=1000000, random_state=42)

# Save sample_10000 as a CSV file
final10000.to_csv('final10000.csv', index=False)

# Save sample_100000 as a CSV file
final100000.to_csv('final100000.csv', index=False)

# Save sample_1000000 as a CSV file
final1000000.to_csv('final1000000.csv', index=False)

#Another one
finaldf.to_csv("finaldf.csv", index = False)
