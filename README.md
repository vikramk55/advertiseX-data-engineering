Here's the README.md file that provides comprehensive instructions on how to configure the project before running it, making it easier for users to understand and use the project effectively.

# AdvertiseX Data Engineering Case Study

## Table of Contents

 1. [Introduction](#introduction)
 2. [Project Purpose](#project-purpose)
 3. [System Requirements](#system-requirements)
 4. [Installation Instructions](#installation-instructions)
 5. [Usage](#usage)
 6. [File Structure](#file-structure)
 7. [Testing](#testing)
 8. [Configuration](#configuration)
 9. [External Dependencies](#external-dependencies)
10. [Detailed Documentation for Each File](#detailed-documentation)
11. [Contributions](#contributions)
12. [License](#license)

---

## 1. Introduction <a name="introduction"></a>

Welcome to the AdvertiseX Data Engineering Case Study project documentation. This documentation provides detailed information on setting up, using, and contributing to the project.

## 2. Project Purpose <a name="project-purpose"></a>

The purpose of this project is to address the data processing challenges faced by AdvertiseX, a digital advertising technology company specializing in programmatic advertising. The solution includes scalable data ingestion, data processing, storage, and monitoring components to handle various data formats and sources.

## 3. System Requirements <a name="system-requirements"></a>

### Prerequisites:

- Python 3.x
- Pip (Python package installer)
- Prometheus
- Alertmanager
 
In the requirements.txt file, you should include the Python packages that your project depends on. These packages are typically installed using pip and are necessary for running your project. Here's an example of what your requirements.txt file might look like for the AdvertiseX Data Engineering Case Study project:

```
pandas==1.3.3
geoip2==4.1.0
sqlalchemy==1.4.25
fastavro==1.4.4
```

## 4. Installation Instructions <a name="installation-instructions"></a>

Follow the steps below to install and set up the project on your local machine:

### Step 1: Clone the Repository

```bash
git clone https://github.com/vikramk55/advertiseX-data-engineering.git
cd advertiseX-data-engineering
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

## 5. Usage <a name="usage"></a>

Follow the instructions below to generate sample data, run data processing, and start monitoring using Prometheus and Alertmanager:

### Step 1: Generate Sample Data

```bash
python generate_sample_data.py
```

### Step 2: Run Data Processing

```bash
python process.py
```

### Step 3: Start Prometheus Server

```bash
prometheus --config.file=prometheus.yml
```

### Step 4: Start Alertmanager

```bash
alertmanager --config.file=alertmanager.yml
```

## 6. File Structure <a name="file-structure"></a>

The project directory structure is as follows:

```
advertiseX-data-engineering/
│
├── data/
│   ├── ad_impressions.json
│   ├── clicks_conversions.csv
│   ├── bid_requests.avro
│   └── GeoLite2-Country.mmdb   <!-- GeoLite2-Country.mmdb is included here -->
├── prometheus.yml
├── alertmanager.yml
├── alert.rules.yml
├── ingest.py
├── generate_sample_data.py
├── process.py
├── test_process.py
├── metrics.py
└── requirements.txt

```

## 7. Testing <a name="testing"></a>

Unit tests are provided in `test_process.py` to ensure the correctness of data processing logic. Run the tests using the following command:

```bash
python -m unittest test_process.py
```

## 8. Configuration <a name="configuration"></a>

Before running the project, make sure to configure the following settings:

### Sender and Receiver Emails for Alerts

The project uses Alertmanager to send email notifications for triggered alerts. You need to configure the sender email and receiver email in the `alertmanager.yml` file. Here's how to do it:

1. Open the `alertmanager.yml` file.
2. Find the `email_configs` section under the `receivers` section.
3. Set the `from` field to your sender email address.
4. Set the `to` field to the email address where you want to receive alerts.

### SMTP Server Settings

To enable email notifications, you need to configure the SMTP server settings in the `alertmanager.yml` file. Here's how to do it:

1. Open the `alertmanager.yml` file.
2. Find the `email_configs` section under the `receivers` section.
3. Set the `smarthost` field to your SMTP server address and port number. For example, `smtp.example.com:587`.
4. Set the `auth_username` field to your SMTP username.
5. Set the `auth_password` field to your SMTP password.

Make sure to replace placeholders like `${SMTP_SERVER}`, `${SMTP_PORT}`, `${SMTP_USERNAME}`, and `${SMTP_PASSWORD}` with the actual values provided by your SMTP service provider.

### Database URL

The project requires a PostgreSQL database to store processed data. Set the `DATABASE_URL` environment variable to the URL of your PostgreSQL database. Here's how to do it:

```bash
export DATABASE_URL="postgresql://username:password@hostname:port/database_name"
```

Replace `username`, `password`, `hostname`, `port`, and `database_name` with your PostgreSQL database credentials and connection details.

## 9. External Dependencies <a name="external-dependencies"></a>

#### GeoLite2-Country.mmdb

The project utilizes the GeoLite2-Country database file `GeoLite2-Country.mmdb` to extract user country information from IP addresses. This file is located in the `data/` directory of the project. It is crucial for the functionality of the `process.py` script, specifically in the `get_country_from_ip` method of the `DataProcessor` class.

#### Note:

Ensure that you have downloaded and placed the `GeoLite2-Country.mmdb` file in the data/ directory before running the process.py script.
You may need to periodically update this database file to ensure accurate geolocation data.


## 10. Detailed Documentation for Each File <a name="detailed-documentation"></a>

### 1. process.py

The `process.py` script plays a pivotal role in addressing the challenges outlined in the project requirements for AdvertiseX, a digital advertising technology company. Here's a comprehensive breakdown of its functionality and alignment with project objectives:

- **Data Ingestion:**
  - The script facilitates scalable ingestion and processing of data from ad impressions (JSON), clicks/conversions (CSV), and bid requests (Avro). It effectively manages high data volumes in real-time and batch modes, ensuring scalability.

- **Data Processing:**
  - Through functions like `process_ad_impressions`, `process_clicks_conversions`, and `process_bid_requests`, raw data is transformed into structured pandas DataFrames, thereby standardizing and enriching the data.
  - Data validation, filtering, and deduplication are carried out seamlessly with functions such as `validate_data`, `filter_data`, and `deduplicate_data`, thereby ensuring data quality and consistency.
  - The script efficiently correlates ad impressions with clicks and conversions, providing valuable insights into campaign performance.

- **Data Storage and Query Performance:**
  - Processed data is stored efficiently in a PostgreSQL database using SQLAlchemy's `to_sql` function. PostgreSQL's reliability, scalability, and support for analytical queries make it an ideal choice for storing campaign performance data.
  - Although not explicitly implemented in the script, PostgreSQL offers features such as indexing and query optimization, ensuring fast querying and aggregation of ad campaign data.

- **Error Handling and Monitoring:**
  - Robust error handling mechanisms are in place to capture and log errors during data processing and storage, ensuring system robustness and reliability.
  - While monitoring functionalities are not directly implemented in the provided code, additional monitoring tools like Prometheus and Grafana can be integrated to detect anomalies and ensure timely resolution.

The `process.py` script aptly meets the project requirements by providing a scalable data ingestion system, robust data processing logic, efficient data storage, and error handling mechanisms, effectively addressing the challenges faced by AdvertiseX in managing diverse data formats and ensuring data integrity.

### 2. ingest.py

The `ingest.py` script serves as a cornerstone in the data engineering solution for AdvertiseX, facilitating data ingestion, processing, storage, and error handling. Here's a detailed analysis of its functionality in alignment with project objectives:

- **Data Ingestion:**
  - The script encompasses functions to ingest data from JSON, CSV, and Avro files, ensuring flexibility and compatibility with diverse data sources and formats.
  - Each ingestion function handles errors gracefully and logs relevant information, thereby ensuring data ingestion reliability and integrity.

- **Scalability:**
  - Although not explicitly implemented, the script's asynchronous file reading with `aiofiles` lays the groundwork for scalability by allowing concurrent file operations, potentially enhancing performance for large datasets.

- **Data Processing:**
  - While the script primarily focuses on data ingestion, subsequent processing tasks are typically handled in downstream components of the data pipeline.

- **Data Storage and Query Performance:**
  - Direct interactions with data storage solutions are not included in the script. However, the ingested data can be stored in suitable data storage solutions as managed in other components of the data processing pipeline.

- **Error Handling and Monitoring:**
  - Error handling mechanisms are effectively implemented to capture and log errors during data ingestion, contributing to data quality and system reliability.

The `ingest.py` script efficiently fulfills the initial step of data ingestion by seamlessly reading data from diverse sources, thereby laying a solid foundation for subsequent processing, storage, and analysis tasks within the broader data engineering solution for AdvertiseX.

### 3. metrics.py

The `metrics.py` script is instrumental in collecting metrics related to data ingestion and processing using Prometheus. Here's an in-depth exploration of its functionalities and how they align with project requirements:

- **Data Ingestion:**
  - While the script does not directly handle data ingestion, it captures relevant metrics that reflect the performance and health of the data ingestion process.

- **Data Processing:**
  - The script simulates data processing through functions like `process_ad_impressions`, `process_clicks_conversions`, and `process_bid_requests`, showcasing potential metrics that could be monitored during actual processing tasks.

- **Prometheus Metrics:**
  - Prometheus metrics are defined using the `Counter` and `Histogram` classes, registering metrics such as `REQUESTS_TOTAL`, `INGESTION_ERRORS`, and `PROCESSING_TIME` to provide insights into system performance and health.

- **Error Handling and Monitoring:**
  - The script effectively handles errors during data ingestion and processing, logging relevant information and incrementing appropriate counters, thereby contributing to robust error handling and monitoring capabilities.

- **Scalability and Optimization:**
  - Although direct scalability features are not implemented, the captured metrics offer insights that can guide scalability and optimization efforts by identifying performance bottlenecks and areas for improvement.

The `metrics.py` script complements the data processing pipeline by capturing key performance metrics, providing valuable insights into system performance and health, and facilitating effective error handling and monitoring.

### 4. generate_sample_data.py

The `generate_sample_data.py` script is designed to address the data generation aspect of the AdvertiseX case study requirements. Here's a detailed examination of its implementation and alignment with project objectives:

- **Logging Configuration:**
  - The script configures logging to provide comprehensive information about script execution, ensuring visibility into the data generation process.

- **Constants Definition:**
  - Constants such as `DATA_DIR` are defined for configurability and maintainability, allowing easy modification of output directories if required.

- **Timestamp Generation Function:**
  - The `random_timestamp()` function generates random timestamps within a specified range, mimicking real-world data scenarios and ensuring data variability.

- **Data Generation Functions:**
  - Separate functions are implemented to generate sample data for ad impressions, clicks/conversions, and bid requests, ensuring modularity and extensibility of data generation logic.

- **Error Handling:**
  - Error handling mechanisms are in place to catch and log exceptions during data generation, contributing to the reliability and robustness of the script.

- **Data Directory Creation:**
  - The script checks for the existence of the specified data directory and creates it if necessary, ensuring proper organization and storage of generated data.

- **Functionality Alignment:**
  - The script aligns with project requirements by generating sample data in JSON, CSV, and Avro formats for ad impressions, clicks/conversions, and bid requests, facilitating development and testing of the data processing pipeline.

- **Scalability and Configurability:**
  - The script's design allows for scalability by enabling the specification of data volume parameters, ensuring adaptability to varying testing requirements.

The `generate_sample_data.py` script provides a scalable and configurable solution for generating sample data in the required formats, thereby facilitating the development and testing of the data processing pipeline for AdvertiseX.

### 5. test_process.py

The `test_process.py` script encompasses unit tests for validating the functionality of the `process_data` function within the broader data processing solution for AdvertiseX. Here's an overview of its features and alignment with project objectives:

- **Unit Testing Framework:**
  - The script utilizes the `unittest` framework to define and execute test cases systematically, ensuring comprehensive test coverage and reproducibility.

- **Test Cases:**
  - A diverse range of test cases is included, covering scenarios such as valid data, invalid data, edge cases, and additional scenarios, ensuring thorough validation of data processing logic under various conditions.

- **Data Variability:**
  - Test data is diversified to encompass a wide range of scenarios, including valid data, invalid data, edge cases, and additional scenarios, ensuring robust testing of the data processing logic.

- **Error Handling Testing:**
  - Assertions are included to verify that invalid data processing raises exceptions as expected, ensuring effective error handling mechanisms are in place.

- **Correlation Testing:**
  - The processed data can be further validated or tested outside the test function, allowing for correlation testing with expected outcomes or additional assertions to ensure data processing correctness.

- **Scalability:**
  - The script's design facilitates scalability by accommodating varying amounts of test data, ensuring adaptability to evolving testing requirements.

The `test_process.py` script effectively validates the data processing functionality according to

 project requirements, ensuring the accuracy, reliability, and robustness of the data processing solution for AdvertiseX.

### 6. alerts.rules.yml

The `alerts.rules.yml` file contains a comprehensive set of rules for Prometheus alerting, designed to address various aspects of data processing, storage, resource utilization, and system health. Here's a detailed examination of each alert and its significance in meeting project requirements for AdvertiseX:

- **High Ad Impressions Anomaly Detected:**
  - This alert triggers when the rate of ad impressions significantly increases, indicating a potential anomaly in the advertising campaign. It helps detect sudden spikes in ad impressions, facilitating prompt investigation and mitigation to maintain campaign effectiveness.

- **High Click-Through Rate:**
  - This critical alert is triggered when the click-through rate (CTR) exceeds the threshold, indicating a high level of user engagement with the ads. It prompts further analysis to optimize campaign performance and maximize user engagement.

- **High Bid Request Failure Rate:**
  - This critical alert detects when the percentage of failed bid requests exceeds the acceptable threshold, indicating issues with the bidding process. It provides insights into bid request failures, facilitating prompt action to ensure smooth operation of real-time bidding auctions.

- **Data Validation Failure:**
  - This warning alert triggers when data validation errors occur, indicating potential data quality issues in the processed data. It enables timely identification and resolution of data quality issues to maintain the integrity of analytics and reporting.

- **Processing Pipeline Bottleneck:**
  - This warning alert detects bottlenecks in the data processing pipeline, facilitating proactive measures to optimize resource utilization and improve processing efficiency.

- **High Storage Utilization:**
  - This critical alert alerts when storage utilization exceeds the threshold, indicating the need for additional resources or optimization of data storage. It provides early warning about potential storage capacity issues, enabling proactive capacity planning to prevent data loss or service disruption.

- **High CPU/Memory Usage:**
  - This critical alert triggers when CPU or memory usage exceeds the threshold, indicating resource contention or potential performance degradation. It alerts about critical resource utilization, prompting investigation and optimization to ensure optimal system performance and stability.

- **Data Ingestion Failure:**
  - This critical alert detects data ingestion errors, indicating disruptions in the data processing pipeline. It enables rapid response to address issues and minimize data processing downtime.

- **Database Connection Issues:**
  - This critical alert alerts when connection errors occur with the database, impacting data availability and integrity. It provides early warning about database connectivity issues, facilitating prompt resolution to ensure uninterrupted access to critical data.

- **Slow Query Execution:**
  - This warning alert triggers when query execution time exceeds the threshold, indicating slow performance that may affect user experience or analytics. It alerts about slow query execution, prompting investigation and optimization of database queries to improve responsiveness and overall system performance.

These alerts cover various aspects of data processing, storage, resource utilization, and system health, aligning with project requirements for implementing an effective error handling and monitoring system for AdvertiseX. They enable timely detection and resolution of potential issues, ensuring the integrity, availability, and performance of the data processing infrastructure.

### 7. alertmanager.yml

The `alertmanager.yml` configuration file provides comprehensive settings for configuring email notifications, routing alerts, and managing global parameters. Here's a detailed analysis of its functionalities and alignment with project requirements:

- **Email Notification Configuration:**
  - The configuration defines an email notification receiver named `'email_notifications'`, specifying email settings for sending notifications, including recipient address, sender address, SMTP server details, and authentication credentials.

- **Routing Configuration:**
  - The `route` section defines how alerts are grouped and handled, specifying grouping criteria, timing parameters, and the receiver for sending notifications.

- **Global Configuration:**
  - The `global` section sets parameters such as `resolve_timeout`, determining the duration after which an alert should be considered resolved if it stops firing.

The `alertmanager.yml` configuration provides the necessary settings for configuring email notifications, routing alerts, and managing global parameters, aligning with project requirements for implementing an alerting mechanism in the AdvertiseX data processing infrastructure.

### 8. prometheus.yml

The `prometheus.yml` configuration file plays a pivotal role in enabling scalable data ingestion, optimizing performance for high-volume environments, and facilitating error handling and monitoring through alerting rules. Here's a detailed examination of how it fulfills each requirement:

- **Data Ingestion:**
  - The configuration specifies scrape jobs for collecting metrics from relevant targets, enabling Prometheus to ingest data efficiently from multiple sources.

- **Scalability:**
  - Adjustments for high-volume environments are included by setting `scrape_interval` and `evaluation_interval` appropriately, ensuring Prometheus can handle large volumes of incoming data effectively.

- **Data Processing:**
  - While the configuration primarily focuses on data ingestion, it lays the foundation for data processing by collecting metrics from different targets, with data processing logic typically implemented in Prometheus alerting rules referenced in the `rule_files` section.

- **Error Handling and Monitoring:**
  - Alerting rules defined in `alert.rules.yml` enable Prometheus to detect anomalies, discrepancies, or delays in collected data and trigger alerts accordingly. Alerts are sent to the specified Alertmanager for further processing and notification.

Overall, the `prometheus.yml` configuration aligns with project requirements by facilitating scalable data ingestion, performance optimization, and effective error handling and monitoring through alerting rules, thereby contributing to the reliability, integrity, and performance of the data processing infrastructure for AdvertiseX.

## 11. Contributions <a name="contributions"></a>

Contributions to this project are welcome! If you have any suggestions, improvements, or new features to propose, please open an issue or submit a pull request. Ensure that your contributions adhere to the project's coding standards and guidelines.

## 12. License <a name="license"></a>

This project is licensed under the [MIT License](LICENSE).
