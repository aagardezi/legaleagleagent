import requests
import urllib

# Define the URL with all parameters
url = "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zMi4xMzQzMDQmcz04MjQ4OTc3JnQ9byZkPTIwMjQtMTItMjc%3D&filed_after=01%2F01%2F2020&order_by=score+desc&q=Motor+Vehicle+Personal+Injury&stat_Published=on&type=o"

# Define the Authorization header
headers = {
    "Authorization": "Token 307c372e8a25e2e76527a808b6851ac98d32c8cc"
}

# Send a GET request with the headers
response = requests.get(url, headers=headers)

# Check for successful response (status code 200)
if response.status_code == 200:
    # Get the response data as JSON
    try:
        data = response.json()
        # Print the data (you can explore the data structure here)
        print(data['results'][0])
    except ValueError:  # includes simplejson.decoder.JSONDecodeError
        print(f"Decoding JSON failed for: {response.text}")
        print(f"Status Code: {response.status_code}")
        print(f"Headers: {response.headers}")

elif response.status_code == 401:
    print(f"Authentication Failed. Check your token. Status Code: {response.status_code}")
elif response.status_code == 403:
    print(f"Forbidden. You don't have permission to access this resource. Status Code: {response.status_code}")
else:
    # Handle other unsuccessful responses
    print(f"Error: {response.status_code}")
    print(f"Response Text: {response.text}") # Print the error response from the server

print(urllib.parse.quote("this is a test"))
print(urllib.parse.quote_plus("this is a test"))