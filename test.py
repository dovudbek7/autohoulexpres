import requests

# API key and endpoint
api_key = 'f26861f0-66c3-11ef-b464-139a31268584'
state = 'Noord-Holland'
country = 'nl'

# API URL
api_url = f'https://app.zipcodebase.com/api/v1/code/state?apikey={api_key}&state_name={state}&country={country}'

# Sending the request
response = requests.get(api_url)

# Checking if the request was successful
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code} {response.text}")
