# Global Weather Intelligence Dashboard Documentation

## Project Overview
The Global Weather Intelligence Dashboard is a web application that displays and analyzes weather data across different regions. It consists of a Flask backend API and a Streamlit frontend dashboard with real-time data visualization capabilities.

## Table of Contents
1. [System Requirements](#system-requirements)
2. [Project Structure](#project-structure)
3. [Installation Guide](#installation-guide)
4. [Running the Application](#running-the-application)
5. [Features](#features)
6. [API Documentation](#api-documentation)
7. [Troubleshooting](#troubleshooting)

## System Requirements
- Python 3.8 or higher
- pip (Python package installer)
- Terminal/Command Prompt
- Web browser (Chrome/Firefox recommended)

## Project Structure
```
weatherapp/
├── venv/                  # Virtual environment directory
├── api/                   # Backend API directory
│   └── app.py            # Flask API code
├── streamlit_app/        # Frontend directory
│   └── main.py          # Streamlit dashboard code
└── requirements.txt      # Project dependencies
```

## Installation Guide

### 1. Create Project Directory
```bash
mkdir ~/Desktop/weatherapp
cd ~/Desktop/weatherapp
```

### 2. Set Up Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install flask
pip install flask-cors
pip install streamlit
pip install pandas
pip install plotly
pip install requests
```

### 4. Create Required Files
Create two main files with the provided code:
- `api/app.py`: Flask backend API
- `streamlit_app/main.py`: Streamlit frontend dashboard

## Running the Application

### 1. Start the Flask API
```bash
# Open a terminal window
cd ~/Desktop/weatherapp
source venv/bin/activate  # On Windows: venv\Scripts\activate
cd api
python app.py
```
The API should start running on `http://localhost:8000`

### 2. Start the Streamlit Dashboard
```bash
# Open a new terminal window
cd ~/Desktop/weatherapp
source venv/bin/activate  # On Windows: venv\Scripts\activate
cd streamlit_app
streamlit run main.py
```
The dashboard will open automatically in your default browser at `http://localhost:8501`

## Features

### Dashboard Features
1. **Real-time Data Visualization**
   - Temperature distribution
   - Humidity analysis
   - Wind speed monitoring
   - Air quality index
   - Precipitation patterns

2. **Interactive Filters**
   - Date selection
   - Region selection
   - Auto-refresh capability
   - Custom refresh intervals

3. **Data Analysis Tools**
   - Statistical summaries
   - Comparative analysis
   - Trend visualization
   - Raw data access

4. **Export Capabilities**
   - CSV download option
   - Data snapshots
   - Custom date range exports

### API Endpoints

1. **Weather Data Endpoint**
```
GET /weather
Parameters:
- date (YYYY-MM-DD)
- region (string)
```

2. **Statistics Endpoint**
```
GET /weather/stats
Returns:
- Total records
- Available regions
- Date range
- Temperature range
```

## API Documentation

### Base URL
```
http://localhost:8000
```

### Available Endpoints

#### 1. Get Weather Data
```
GET /weather
```
Query Parameters:
- `date`: Filter by specific date (YYYY-MM-DD)
- `region`: Filter by region name

Response Format:
```json
[
    {
        "date": "2024-02-26",
        "region": "New York",
        "temperature": 20.5,
        "precipitation": 0.5,
        "humidity": 65,
        "wind_speed": 15.2,
        "air_quality_index": 45,
        "uv_index": 5.5,
        "pressure": 1013.2
    }
]
```

#### 2. Get Weather Statistics
```
GET /weather/stats
```
Response Format:
```json
{
    "total_records": 240,
    "regions": ["New York", "London", "Tokyo", ...],
    "date_range": {
        "start": "2024-01-27",
        "end": "2024-02-26"
    },
    "temperature_range": {
        "min": 15.0,
        "max": 35.0
    }
}
```

## Troubleshooting

### Common Issues and Solutions

1. **Port Already in Use**
```bash
# Check for processes using the ports
lsof -i :8000  # For API
lsof -i :8501  # For Streamlit

# Kill the process
kill -9 <PID>
```

2. **API Connection Error**
- Ensure Flask API is running
- Check the correct port (8000)
- Verify CORS settings

3. **No Data Showing**
- Verify date range (last 30 days only)
- Check region spelling
- Ensure API is returning data

4. **Virtual Environment Issues**
```bash
# Recreate virtual environment
rm -rf venv
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Additional Notes
- Keep both the Flask API and Streamlit app running simultaneously
- Use the auto-refresh feature for real-time updates
- Data is generated for the last 30 days only
- All timestamps are in UTC

For additional support or feature requests, please refer to the project repository or contact the development team.
