---

# AdvertiseX Data Engineering Case Study

## Table of Contents

1. [Introduction](#introduction)
2. [Project Purpose](#project-purpose)
3. [System Requirements](#system-requirements)
4. [Installation Instructions](#installation-instructions)
5. [Usage](#usage)
6. [File Structure](#file-structure)
7. [Testing](#testing)
8. [Contributing](#contributing)
9. [License](#license)

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
git clone https://github.com/your-username/advertiseX-data-engineering.git
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
│   └── bid_requests.avro
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

## 8. Contributing <a name="contributing"></a>

Contributions to this project are welcome! If you have any suggestions, improvements, or new features to propose, please open an issue or submit a pull request. Ensure that your contributions adhere to the project's coding standards and guidelines.

## 9. License <a name="license"></a>

This project is licensed under the [MIT License](LICENSE).

---
