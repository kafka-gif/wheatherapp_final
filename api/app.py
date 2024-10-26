from flask import Flask, jsonify, request
from datetime import datetime, timedelta
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

def generate_weather_data():
    regions = ["New York", "London", "Tokyo", "Mumbai", "Sydney", "Paris", "Dubai", "Singapore"]
    weather_data = []
    
    # Generate data for last 30 days
    for i in range(30):
        date = (datetime.now() - timedelta(days=i)).strftime("%Y-%m-%d")
        for region in regions:
            weather_data.append({
                "date": date,
                "region": region,
                "temperature": round(random.uniform(15, 35), 1),
                "precipitation": round(random.uniform(0, 1), 2),
                "humidity": random.randint(30, 90),
                "wind_speed": round(random.uniform(0, 30), 1),
                "air_quality_index": random.randint(20, 150),
                "uv_index": round(random.uniform(1, 11), 1),
                "pressure": round(random.uniform(980, 1020), 1)
            })
    return weather_data

# Generate initial weather data
weather_data = generate_weather_data()

@app.route('/weather', methods=['GET'])
def get_weather():
    try:
        date = request.args.get('date')
        region = request.args.get('region')
        
        filtered_data = weather_data
        
        if date:
            filtered_data = [d for d in filtered_data if d['date'] == date]
        if region:
            filtered_data = [d for d in filtered_data if d['region'].lower() == region.lower()]
        
        return jsonify(filtered_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/weather/stats', methods=['GET'])
def get_weather_stats():
    try:
        stats = {
            "total_records": len(weather_data),
            "regions": list(set(d['region'] for d in weather_data)),
            "date_range": {
                "start": min(d['date'] for d in weather_data),
                "end": max(d['date'] for d in weather_data)
            },
            "temperature_range": {
                "min": min(d['temperature'] for d in weather_data),
                "max": max(d['temperature'] for d in weather_data)
            }
        }
        return jsonify(stats)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)