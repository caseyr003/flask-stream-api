import json
import random
import string
from datetime import datetime

USERS = [
    "casey@ocistream.com",
    "thomas@ocistream.com",
    "riaz@ocistream.com",
    "madhu@ocistream.com",
    "will@ocistream.com",
    "debbie@ocistream.com"
]

ITEMS = [
    ("Men's Socks", 9.99),
    ("Women's Socks", 12.99),
    ("Men's Shorts", 34.99),
    ("Women's Shorts", 29.99),
    ("Men's Jeans", 49.99),
    ("Women's Jeans", 49.99),
    ("Men's Dress Shirt", 54.99),
    ("Women's Blouse", 54.99),
    ("Men's Shoes", 89.99),
    ("Women's Shoes", 99.99)
]

# Used for testing
# Will update the functions to return random values
def generate_key():
    options = string.ascii_letters + string.digits
    return ''.join(random.choice(options) for i in range(8))

def generate_user():
    return random.choice(USERS)

def generate_item():
    return random.choice(ITEMS)

def generate_date():
    return str(datetime.now())

def generate_data(orderType):
    key = generate_key()
    user = generate_user()
    item = generate_item()
    date = generate_date()
    data={
        "key":key,
        "user":user,
        "item":item[0],
        "cost":item[1],
        "date":date,
        "orderType":orderType
    }
    return json.dumps(data)