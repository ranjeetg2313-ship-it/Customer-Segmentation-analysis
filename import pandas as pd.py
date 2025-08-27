import pandas as pd
import numpy as np
import random
from faker import Faker

fake = Faker()

# Set seed for reproducibility
np.random.seed(42)
random.seed(42)

# Number of rows
n_rows = 150000

# Sample categories
categories = ['T-Shirts', 'Jeans', 'Jackets', 'Dresses', 'Shoes']
subcategories = ['Men', 'Women', 'Kids']
brands = ['h&m', 'zara', 'sparkey', 'raymond','zudio','gucci','Redtape','ck']
sizes = ['S', 'M', 'L', 'XL']
colors = ['Red', 'Blue', 'Black', 'White', 'Green']
payment_methods = ['Credit Card', 'PayPal', 'Cash', 'Debit Card','upi']
transaction_statuses = ['Completed', 'Returned', 'Cancelled']
countries = ['USA', 'India', 'UK', 'Canada', 'Australia']
states = ['California', 'Maharashtra', 'Texas', 'Ontario', 'Uttar Pradesh','karnatak','New South Wales']
cities = ['Los Angeles', 'Mumbai', 'Houston', 'Toronto', 'Sydney']
segments = ['Budget Shoppers', 'Frequent Buyers', 'Luxury Seekers', 'Trendy Teens']

# Generate data
data = {
    "CustomerID": [fake.uuid4() for _ in range(n_rows)],
    "CustomerName": [fake.name() for _ in range(n_rows)],
    "Gender": [random.choice(['Male', 'Female']) for _ in range(n_rows)],
    "Age": np.random.randint(18, 60, size=n_rows),
    "Email": [fake.email() for _ in range(n_rows)],
    "PhoneNumber": [fake.phone_number() for _ in range(n_rows)],
    "MembershipStatus": [random.choice(['Regular', 'Silver', 'Gold', 'VIP']) for _ in range(n_rows)],
    "LoyaltyPoints": np.random.randint(0, 5000, size=n_rows),
    "ProductID": [fake.uuid4() for _ in range(n_rows)],
    "ProductName": [fake.word().capitalize() for _ in range(n_rows)],
    "Category": [random.choice(categories) for _ in range(n_rows)],
    "SubCategory": [random.choice(subcategories) for _ in range(n_rows)],
    "Brand": [random.choice(brands) for _ in range(n_rows)],
    "Size": [random.choice(sizes) for _ in range(n_rows)],
    "Color": [random.choice(colors) for _ in range(n_rows)],
    "UnitPrice": np.round(np.random.uniform(10, 200), 2),
    "OrderID": [fake.uuid4() for _ in range(n_rows)],
    "InvoiceDate": [fake.date_between(start_date='-1y', end_date='today') for _ in range(n_rows)],
    "QuantitySold": np.random.randint(1, 5, size=n_rows),
    "Discount": np.round(np.random.uniform(0, 30), 2),
    "TaxAmount": np.round(np.random.uniform(0, 20), 2),
    "PaymentMethod": [random.choice(payment_methods) for _ in range(n_rows)],
    "TransactionStatus": [random.choice(transaction_statuses) for _ in range(n_rows)],
    "Country": [random.choice(countries) for _ in range(n_rows)],
    "State": [random.choice(states) for _ in range(n_rows)],
    "City": [random.choice(cities) for _ in range(n_rows)],
    "PostalCode": [fake.postcode() for _ in range(n_rows)],
    "StoreLocation": [fake.company() for _ in range(n_rows)],
    "CustomerSegment": [random.choice(segments) for _ in range(n_rows)],
    "PurchaseChannel": [random.choice(['Online', 'In-store', 'Mobile App']) for _ in range(n_rows)],
    "ReturnStatus": [random.choice(['Returned', 'Not Returned']) for _ in range(n_rows)],
    "ReturnReason": [random.choice(['Size Issue', 'Color Mismatch', 'Late Delivery', 'No Return']) for _ in range(n_rows)],
}

# Calculate totals
df = pd.DataFrame(data)
df["TotalSalesAmount"] = df["QuantitySold"] * df["UnitPrice"]
df["FinalAmount"] = df["TotalSalesAmount"] - df["Discount"] + df["TaxAmount"]

# Save CSV
file_path = "C:/Users/ranje/OneDrive/Desktop/generated/customer_sales_clothing_data.csv"
df.to_csv(file_path, index=False)

