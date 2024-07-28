import requests

# Create a session object
session = requests.Session()

# Now, use the session to perform HTTP requests
response = session.get('https://api.example.com/data')
print(response.json())  # Print the JSON response from the server

# You can use the same session object for multiple requests
response = session.post('https://api.example.com/update', data={'key': 'value'})
print(response.status_code)  # Print the status code of the POST request

# Session object persists cookies across requests automatically
