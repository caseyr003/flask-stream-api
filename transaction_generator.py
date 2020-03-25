import json
import random
import string
from datetime import datetime

# Used for testing
# Will update the functions to return random values
def generate_key():
    options = string.ascii_letters + string.digits
    return ''.join(random.choice(options) for i in range(8))

def generate_user():
    return "casey@ocistream.com"

def generate_item():
    return ("Men's Shorts", 29.99)

def generate_type():
    return "online-US"

def generate_date():
    return str(datetime.now())

def generate_data():
    key = generate_key()
    user = generate_user()
    item = generate_item()
    transaction = generate_type()
    date = generate_date()
    data={
        "key":key,
        "user":user,
        "item":item[0],
        "cost":item[1],
        "transaction":transaction,
        "date":date
    }
    return json.dumps(data)