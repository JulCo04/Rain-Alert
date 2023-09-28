import requests # HTTP requests
from twilio.rest import Client #Twilio Client

# Define the Twilio phone number, account SID, and authentication token.
twilio_number = "+19093774719"
account_sid = "AC6ba1c7c19e4005169f50a9c4e392ed47"
auth_token = "36e410103345966c829aa100a4621f9d"

# Define the endpoint URL for the OpenWeatherMap API and the API key.
endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "ce908abbf1b3d5fa9bc569b9f3f1 50c4"

# Phone number you want the message sent to
cell_num = "###-###-####"

# Define the parameters for the weather API request.
weather_params = {
    "lat": 13.572720,
    "lon": -8.034030,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

# Make a GET request to the OpenWeatherMap API with the defined parameters.
response = requests.get(endpoint, params=weather_params)
response.raise_for_status()  # Check for any HTTP errors.
weather_data = response.json()  # Parse the JSON response.

# Extract the hourly weather data from the API response.
hourly_weather_data = weather_data["hourly"]

# Select the first 13 hours of weather data.
twelve_hours_weather = hourly_weather_data[:13]

# Extract the weather IDs from the selected weather data.
weather_ids = [twelve_hours_weather[num]["weather"][0]["id"] for num in range(12)]

print(weather_ids)

# Initialize a variable to check if it will rain.
will_rain = False

# Check if any of the weather IDs are less than 700 (indicating rain).
for num in weather_ids:
    if num < 700:
        will_rain = True

# If rain is predicted, send a Twilio message.
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="It's going to rain tomorrow, bring an umbrella ☂️.",
                     from_=twilio_number,
                     to=cell_num
                 )
    print(message.status)  # Print the status of the Twilio message.
else:
    print("You're safe, no rain expected.")  # Print a message if no rain is expected.



