import json
import socket
import urllib.error
import urllib.parse
import urllib.request


API_KEY = "3fdcc363592010cc79f9e180d3478eb9"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
    }
    url = BASE_URL + "?" + urllib.parse.urlencode(params)

    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            response_text = response.read().decode("utf-8")

        if response_text == "":
            print("Error: API failure.")
            return None

        data = json.loads(response_text)

        return {
            "city": data["name"],
            "temperature": round(data["main"]["temp"]),
            "humidity": data["main"]["humidity"],
            "wind_speed": round(data["wind"]["speed"] * 3.6),
            "condition": data["weather"][0]["main"],
        }

    except urllib.error.HTTPError as error:
        if error.code == 404:
            print("Error: Invalid city.")
        elif error.code == 401:
            print("Error: API key is invalid. Check your API key.")
        else:
            print("Error: API failure.")
        return None

    except (urllib.error.URLError, socket.timeout):
        print("Error: No internet connection.")
        return None

    except json.JSONDecodeError:
        print("Error: API failure. The API did not return valid weather data.")
        return None

    except (KeyError, IndexError):
        print("Error: API failure.")
        return None


def display_weather(weather):
    print()
    print("=================")
    print("Weather Report")
    print("=================")
    print()
    print(f"City: {weather['city']}")
    print(f"Temperature: {weather['temperature']}{chr(176)}C")
    print(f"Humidity: {weather['humidity']}%")
    print(f"Wind Speed: {weather['wind_speed']} km/h")
    print(f"Condition: {weather['condition']}")


def main():
    while True:
        print("****************")
        print("Weather App")
        print("****************")
        print()
        print("1. Get Weather")
        print("2. Exit")
        print()

        choice = input("Choose option: ")

        if choice == "1":
            city = input("Enter city: ")
            weather = get_weather(city)

            if weather is not None:
                display_weather(weather)

            print()

        elif choice == "2":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1 or 2.")
            print()


if __name__ == "__main__":
    main()