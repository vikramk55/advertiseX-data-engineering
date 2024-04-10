import json
import csv
import random
from datetime import datetime, timedelta
import fastavro
import io
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

# Define constants
DATA_DIR = 'data/'

# Function to generate random timestamp
def random_timestamp(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    random_hours = random.randint(0, 23)
    random_minutes = random.randint(0, 59)
    random_seconds = random.randint(0, 59)
    return start_date + timedelta(days=random_days, hours=random_hours, minutes=random_minutes, seconds=random_seconds)

# Function to generate ad impressions data
def generate_ad_impressions_data(num_entries):
    data = []
    for _ in range(num_entries):
        ad_impression = {
            "ad_creative_id": random.randint(1, 1000),
            "user_id": random.randint(10000, 99999),
            "timestamp": random_timestamp(datetime(2023, 1, 1), datetime(2023, 12, 31)).strftime('%Y-%m-%d %H:%M:%S'),
            "website_url": f"http://example{random.randint(1, 10)}.com/path/{random.randint(1, 100)}"
        }
        data.append(ad_impression)
    return data

# Function to generate clicks and conversions data
def generate_clicks_conversions_data(num_entries):
    data = []
    for _ in range(num_entries):
        click_conversion = {
            "timestamp": random_timestamp(datetime(2023, 1, 1), datetime(2023, 12, 31)).strftime('%Y-%m-%d %H:%M:%S'),
            "user_id": random.randint(10000, 99999),
            "ad_campaign_id": random.randint(1, 10),
            "conversion_type": random.choice(["purchase", "signup", "visit"])
        }
        data.append(click_conversion)
    return data

# Function to generate bid requests data
def generate_bid_requests_data(num_entries):
    data = []
    for _ in range(num_entries):
        bid_request = {
            "bid_amount": round(random.uniform(0.1, 10), 2),
            "user_id": random.randint(10000, 99999),
            "auction_id": f"AUCTION-{random.randint(1, 1000)}",
            "ip_address": f"192.168.{random.randint(1, 255)}.{random.randint(1, 255)}"
        }
        data.append(bid_request)
    return data

# Function to write data to files
def write_data_to_files(data, filename, format):
    try:
        if format == 'json':
            with open(os.path.join(DATA_DIR, filename), 'w') as f:
                json.dump(data, f, indent=4)
        elif format == 'csv':
            with open(os.path.join(DATA_DIR, filename), 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=["timestamp", "user_id", "ad_campaign_id", "conversion_type"])
                writer.writeheader()
                writer.writerows(data)
        elif format == 'avro':
            avro_schema = {
                "type": "record",
                "name": "BidRequest",
                "fields": [
                    {"name": "bid_amount", "type": "float"},
                    {"name": "user_id", "type": "int"},
                    {"name": "auction_id", "type": "string"},
                    {"name": "ip_address", "type": "string"}
                ]
            }
            with io.BytesIO() as avro_output:
                fastavro.writer(avro_output, avro_schema, data)
                avro_output.seek(0)
                with open(os.path.join(DATA_DIR, filename), 'wb') as f:
                    f.write(avro_output.read())
        logging.info(f"Sample data generated successfully and written to {filename}")
    except Exception as e:
        logging.error(f"Error writing sample data to {filename}: {e}")

if __name__ == '__main__':
    # Create data directory if it doesn't exist
    os.makedirs(DATA_DIR, exist_ok=True)

    # Generate ad impressions data
    ad_impressions_data = generate_ad_impressions_data(1000)
    write_data_to_files(ad_impressions_data, 'ad_impressions.json', 'json')

    # Generate clicks and conversions data
    clicks_conversions_data = generate_clicks_conversions_data(1000)
    write_data_to_files(clicks_conversions_data, 'clicks_conversions.csv', 'csv')

    # Generate bid requests data
    bid_requests_data = generate_bid_requests_data(1000)
    write_data_to_files(bid_requests_data, 'bid_requests.avro', 'avro')