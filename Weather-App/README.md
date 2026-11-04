# Weather App

This is a simple Python weather app that gets weather information for a city using the OpenWeatherMap API.

## What The App Does

The program shows a small menu:

```text
****************
Weather App
****************

1. Get Weather
2. Exit

Choose option:
```

If the user chooses option `1`, the program asks for a city name.

Example:

```text
Enter city: Dammam
```

Then it displays a weather report:

```text
=================
Weather Report
=================

City: Dammam
Temperature: 38°C
Humidity: 55%
Wind Speed: 14 km/h
Condition: Sunny
```

## Main Functions

The code has three main functions:

- `get_weather(city)` gets the weather data from the API.
- `display_weather(weather)` displays the weather report.
- `main()` shows the menu and controls the program.

## How To Use It

First, open `weather_app.py` and replace this line:

```python
API_KEY = "PUT_YOUR_API_KEY_HERE"
```

with your real OpenWeatherMap API key:

```python
API_KEY = "your_actual_api_key"
```

Then run the program:

```powershell
python outputs\weather_app.py
```

## Error Handling

The program handles these errors:

- Invalid city name
- No internet connection
- Invalid API key
- API failure
- Invalid weather data from the API

## API Used

This app uses the OpenWeatherMap current weather API:

```text
https://api.openweathermap.org/data/2.5/weather
```
