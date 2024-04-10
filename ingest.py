import json
import csv
from avro import datafile, io
import logging
import argparse
import os
import asyncio
import aiofiles
import concurrent.futures

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

# Define constants
DEFAULT_DATA_DIR = 'data/'

# Define a function to ingest JSON data (ad impressions) asynchronously
async def ingest_ad_impressions(json_file):
    """
    Ingest ad impressions data from a JSON file asynchronously.

    Parameters:
        json_file (str): Path to the JSON file containing ad impressions data.

    Returns:
        list: List of dictionaries containing ad impressions data.
    """
    try:
        async with aiofiles.open(json_file, 'r') as f:
            ad_impressions_data = json.loads(await f.read())
        return ad_impressions_data
    except Exception as e:
        logging.error(f"Error ingesting ad impressions data from {json_file}: {e}")
        return []

# Define a function to ingest CSV data (clicks and conversions) asynchronously
async def ingest_clicks_conversions(csv_file):
    """
    Ingest clicks and conversions data from a CSV file asynchronously.

    Parameters:
        csv_file (str): Path to the CSV file containing clicks and conversions data.

    Returns:
        list: List of dictionaries containing clicks and conversions data.
    """
    try:
        async with aiofiles.open(csv_file, 'r') as f:
            reader = csv.DictReader(await f.readlines())
            clicks_conversions_data = list(reader)
        return clicks_conversions_data
    except Exception as e:
        logging.error(f"Error ingesting clicks and conversions data from {csv_file}: {e}")
        return []

# Define a function to ingest Avro data (bid requests) asynchronously
async def ingest_bid_requests(avro_file):
    """
    Ingest bid requests data from an Avro file asynchronously.

    Parameters:
        avro_file (str): Path to the Avro file containing bid requests data.

    Returns:
        list: List of dictionaries containing bid requests data.
    """
    try:
        async with aiofiles.open(avro_file, 'rb') as f:
            reader = datafile.DataFileReader(f, io.DatumReader())
            bid_requests_data = [record for record in reader]
        return bid_requests_data
    except Exception as e:
        logging.error(f"Error ingesting bid requests data from {avro_file}: {e}")
        return []

# Main function to orchestrate data ingestion asynchronously
async def main():
    # Configure command-line arguments
    parser = argparse.ArgumentParser(description='Data Ingestion for AdvertiseX')
    parser.add_argument('--data-dir', default=DEFAULT_DATA_DIR, help='Directory containing data files')
    args = parser.parse_args()

    # Specify file paths for data ingestion
    ad_impressions_file = os.path.join(args.data_dir, 'ad_impressions.json')
    clicks_conversions_file = os.path.join(args.data_dir, 'clicks_conversions.csv')
    bid_requests_file = os.path.join(args.data_dir, 'bid_requests.avro')

    # Ingest data concurrently using asyncio
    async with concurrent.futures.ThreadPoolExecutor() as pool:
        ad_impressions_task = asyncio.get_event_loop().run_in_executor(pool, ingest_ad_impressions, ad_impressions_file)
        clicks_conversions_task = asyncio.get_event_loop().run_in_executor(pool, ingest_clicks_conversions, clicks_conversions_file)
        bid_requests_task = asyncio.get_event_loop().run_in_executor(pool, ingest_bid_requests, bid_requests_file)
        ad_impressions_data, clicks_conversions_data, bid_requests_data = await asyncio.gather(ad_impressions_task, clicks_conversions_task, bid_requests_task)

    logging.info("Data ingestion completed")

    return ad_impressions_data, clicks_conversions_data, bid_requests_data

if __name__ == '__main__':
    ad_impressions_data, clicks_conversions_data, bid_requests_data = asyncio.run(main())  # Call the main function when the script is executed