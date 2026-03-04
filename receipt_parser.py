# receipt_parser.py

import re
import json

# Step 1 Read the receipt text from raw.txt
with open("raw.txt", "r", encoding="utf-8") as f:
    receipt_text = f.read()

# Step 2: Extract all prices (numbers with 2 decimals)
# Example: 12.50, 3.40
prices = re.findall(r"\d+\.\d{2}", receipt_text)
prices = [float(p) for p in prices]  # convert strings to floats

# Step 3: Extract product names
# Assuming product name comes before the price
# The pattern grabs letters, numbers, spaces, and stops before the price
products_prices = re.findall(r"([A-Za-z0-9\s]+?)\s+(\d+\.\d{2})", receipt_text)
products = [p[0].strip() for p in products_prices]  # remove extra spaces
prices_from_products = [float(p[1]) for p in products_prices]  # prices corresponding to products

# Step 4: Extract total from the receipt (if present)
total_match = re.search(r"Total:\s*(\d+\.\d{2})", receipt_text)
if total_match:
    total = float(total_match.group(1))
else:
    # If Total is not in receipt, sum the prices
    total = sum(prices_from_products)

# Step 5: Extract date and time
# Example format: 04/03/2026 14:35
date_time = re.findall(r"\d{2}/\d{2}/\d{4} \d{2}:\d{2}", receipt_text)

# Step 6: Extract payment method
# Common options: Cash, Credit Card, Debit Card
payment_method = re.findall(r"(Cash|Credit Card|Debit Card)", receipt_text, re.IGNORECASE)

# Step 7: Create structured output as JSON
receipt_data = {
    "products": products,
    "prices": prices_from_products,
    "total": total,
    "date_time": date_time,
    "payment_method": payment_method
}

# Step 8: Print structured JSON output
print(json.dumps(receipt_data, indent=4))