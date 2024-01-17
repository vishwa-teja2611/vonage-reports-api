import pandas as pd
from datetime import datetime
import pytz

# Load your CSV file into a pandas DataFrame
df = pd.read_csv('vonage_call_log_01152024_12AM_5PM.csv')

# Assuming your date and time column is named 'utc_datetime'
# Convert the 'utc_datetime' column to datetime objects
df['start'] = pd.to_datetime(df['start'])
df['end'] = pd.to_datetime(df['end'])

# Set the timezone of the 'utc_datetime' column to UTC
df['start'] = df['start'].dt.tz_localize('UTC')
df['end'] = df['end'].dt.tz_localize('UTC')

# Convert the 'utc_datetime' column to Central Time (CT)
df['start'] = df['start'].dt.tz_convert('America/Chicago')
df['end'] = df['end'].dt.tz_convert('America/Chicago')

# Now, 'ct_datetime' column contains the date and time in Central Time

# Save the DataFrame back to a CSV file
df.to_csv('converted_file.csv', index=False)
