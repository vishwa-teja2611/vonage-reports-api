import pandas as pd

# Load JSON data
json_data = pd.read_json('/Users/vishwatejabingi/Desktop/reports api/output.json')

# Convert to CSV
json_data.to_csv('vonage_call_log_01152024_12AM_5PM.csv', index=False)
