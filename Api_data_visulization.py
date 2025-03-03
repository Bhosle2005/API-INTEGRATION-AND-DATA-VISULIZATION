import requests
import matplotlib.pyplot as plt

# Your API key
API_KEY = "1a408b779106fc62e64ba0f6801558c3"

# List of predefined cities
cities = [
    "Mumbai", "New York", "London", "Tokyo", "Sydney",
    "Paris", "Berlin", "Beijing", "Moscow", "Los Angeles"
]

def get_weather_data(city):
    """Fetch weather data from OpenWeatherMap API for a given city."""
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={"1a408b779106fc62e64ba0f6801558c3"}&units=metric"
    response = requests.get(URL)
    return response

def bar_chart(cities_data):
    """Bar chart for temperature comparison."""
    city_names = [data['city'] for data in cities_data]
    temperatures = [data['temperature'] for data in cities_data]

    plt.figure(figsize=(10, 6))
    plt.bar(city_names, temperatures, color='orange', alpha=0.8)
    plt.xlabel("Cities")
    plt.ylabel("Temperature (°C)")
    plt.title("Temperature Comparison")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def line_chart(cities_data):
    """Line chart for humidity comparison."""
    city_names = [data['city'] for data in cities_data]
    humidities = [data['humidity'] for data in cities_data]

    plt.figure(figsize=(10, 6))
    plt.plot(city_names, humidities, marker='o', linestyle='-', color='blue')
    plt.xlabel("Cities")
    plt.ylabel("Humidity (%)")
    plt.title("Humidity Levels Across Cities")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def pie_chart(cities_data):
    """Pie chart for wind speed distribution."""
    city_names = [data['city'] for data in cities_data]
    wind_speeds = [data['wind_speed'] for data in cities_data]

    plt.figure(figsize=(8, 8))
    plt.pie(wind_speeds, labels=city_names, autopct='%1.1f%%', startangle=140, colors=plt.cm.tab20c.colors)
    plt.title("Wind Speed Distribution Across Cities")
    plt.tight_layout()
    plt.show()

def main():
    """Fetch and display weather data for predefined cities."""
    cities_data = []

    for city in cities:
        response = get_weather_data(city)
        if response.status_code == 200:
            data = response.json()

            # Extract weather details
            city_weather = {
                "city": city.capitalize(),
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "wind_speed": data["wind"]["speed"],
                "description": data["weather"][0]["description"],
            }
            cities_data.append(city_weather)
            print(f"Weather data for {city.capitalize()} fetched successfully.")
        else:
            print(f"Error fetching data for {city}: {response.json()}")

    if cities_data:
        # Display collected weather data
        print("\nCollected Weather Data:")
        for city_data in cities_data:
            print(f"\nCity: {city_data['city']}")
            print(f"  Temperature: {city_data['temperature']}°C")
            print(f"  Condition: {city_data['description'].capitalize()}")
            print(f"  Humidity: {city_data['humidity']}%")
            print(f"  Wind Speed: {city_data['wind_speed']} m/s")

        # Generate visualizations
        bar_chart(cities_data)  # Temperature comparison
        line_chart(cities_data)  # Humidity levels
        pie_chart(cities_data)  # Wind speed distribution
    else:
        print("No data to display.")

if __name__ == "__main__":
    main()
