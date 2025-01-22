import syncedlyrics
import re
import json

# Input data
query = input("Enter Song Name")
lrc = syncedlyrics.search(query)

# Split the data into lines
lines = lrc.split('\n')

# Initialize a list to store the JSON entries
json_data = []

# Define a regular expression pattern to extract timestamps and text
pattern = r'\[(\d+:\d+\.\d+)\] (.+)'

for line in lines:
    match = re.match(pattern, line)
    if match:
        timestamp, text = match.groups()
        
        # Handle Unicode escape sequences (decoding them properly)
        text = bytes(text, "utf-8").decode("unicode_escape")
        
        json_entry = {
            "time": timestamp,
            "lyrics": text
        }
        json_data.append(json_entry)

# Convert the list of JSON entries to a JSON-formatted string
json_string = json.dumps(json_data, indent=4)

# Print the JSON string
print(json_string)
