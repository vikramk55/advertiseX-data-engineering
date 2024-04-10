import pandas as pd
import geoip2.database
from sqlalchemy import create_engine, pool
import geoip2.errors
import logging
import os
import sys

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

class DataProcessor:
    def __init__(self, db_url):
        # Use a connection pool for managing database connections
        self.pool = pool.QueuePool(lambda: create_engine(db_url, pool_size=20, max_overflow=0))

    def store_data(self, df, table_name):
        """
        Store DataFrame into PostgreSQL table.

        Parameters:
            df (pandas.DataFrame): DataFrame to store.
            table_name (str): Name of the table in the database.
        """
        try:
            with self.pool.connect() as conn:
                df.to_sql(table_name, conn, if_exists='replace', index=False)
            logging.info(f"Data stored successfully in table '{table_name}'")
        except Exception as e:
            logging.error(f"Error storing data in table '{table_name}': {e}")

    def process_data(self, data):
        """
        Process ingested data.

        Parameters:
            data (dict): Dictionary containing ingested data with file names as keys.

        Returns:
            dict: Dictionary containing processed data with file names as keys.
        """
        processed_data = {}
        try:
            for filename, dataset in data.items():
                if filename.endswith('.json'):
                    processed_data[filename] = self.process_ad_impressions(dataset)
                elif filename.endswith('.csv'):
                    processed_data[filename] = self.process_clicks_conversions(dataset)
                elif filename.endswith('.avro'):
                    processed_data[filename] = self.process_bid_requests(dataset)
                else:
                    logging.warning(f"Unsupported file format: {filename}")
        except Exception as e:
            logging.error(f"Error processing data: {e}")

        return processed_data

    def process_ad_impressions(self, data):
        """
        Process ad impressions data.

        Parameters:
            data (list): List of dictionaries containing ad impressions data.

        Returns:
            pandas.DataFrame: Processed DataFrame.
        """
        df = pd.DataFrame(data)
        # Convert timestamp to datetime
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        # Extract domain from website URL
        df['domain'] = df['website'].apply(lambda x: x.split('/')[2] if '/' in x else x)
        return df

    def process_clicks_conversions(self, data):
        """
        Process clicks and conversions data.

        Parameters:
            data (list): List of dictionaries containing clicks and conversions data.

        Returns:
            pandas.DataFrame: Processed DataFrame.
        """
        df = pd.DataFrame(data)
        # Convert timestamp to datetime
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        # Map conversion type to human-readable labels
        conversion_type_mapping = {'purchase': 'Purchase', 'signup': 'Sign-Up', 'visit': 'Website Visit'}
        df['conversion_type'] = df['conversion_type'].map(conversion_type_mapping)
        return df

    def process_bid_requests(self, data):
        """
        Process bid requests data.

        Parameters:
            data (list): List of dictionaries containing bid requests data.

        Returns:
            pandas.DataFrame: Processed DataFrame.
        """
        df = pd.DataFrame(data)
        # Extract user country from IP address
        df['user_country'] = df['user_ip'].apply(self.get_country_from_ip)
        return df

    def get_country_from_ip(self, ip_address):
        """
        Get country from IP address.

        Parameters:
            ip_address (str): IP address.

        Returns:
            str: Country name.
        """
        # Placeholder implementation: Use GeoIP2 database to retrieve country
        # Replace 'GeoLite2-Country.mmdb' with the actual path to the GeoIP2 Country database file
        with geoip2.database.Reader('data/GeoLite2-Country.mmdb') as reader:
            try:
                response = reader.country(ip_address)
                return response.country.name
            except geoip2.errors.AddressNotFoundError:
                return 'Unknown'

    # Additional processing functions
    def validate_data(self, df):
        """
        Validate processed data.

        Parameters:
            df (pandas.DataFrame): Processed DataFrame.

        Returns:
            pandas.DataFrame: DataFrame with invalid rows removed.
        """
        # Remove rows with negative bid amounts
        return df[df['bid_amount'] >= 0]

    def filter_data(self, df, condition):
        """
        Filter processed data based on condition.

        Parameters:
            df (pandas.DataFrame): Processed DataFrame.
            condition (str): Filtering condition.

        Returns:
            pandas.DataFrame: Filtered DataFrame.
        """
        # Filter data based on user country
        return df[df['user_country'] == condition]

    def deduplicate_data(self, df):
        """
        Deduplicate processed data.

        Parameters:
            df (pandas.DataFrame): Processed DataFrame.

        Returns:
            pandas.DataFrame: DataFrame with duplicate rows removed.
        """
        # Remove duplicate rows based on user ID
        return df.drop_duplicates(subset='user_id')

# Check if the database URL is provided as an environment variable
db_url = os.getenv('DATABASE_URL')

if not db_url:
    print("Error: DATABASE_URL environment variable is not set.")
    sys.exit(1)

# Now db_url can be used to create the DataProcessor instance
processor = DataProcessor(db_url)