# Lever crawler

This script automates the scrape process in open positions on Lever websites.

## Prerequisites

- Python 3+

## Installation

1. **Create and activate a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    .\venv\Scripts\activate   # Windows
    ```

2. **Install the dependencies** from `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the script, execute:

```bash
scrapy crawl lever -O output.csv
```
