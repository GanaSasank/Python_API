import requests

API_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"


def main():
    data = get_weather_data()

    while True:
        print("\n1. Get Temperature\n2. Get Wind Speed\n3. Get Pressure\n0. Exit")
        choice = input("Enter your choice: ")

        if choice == '0':
            print("Exiting the program.")
            break
        elif choice in ['1', '2', '3']:
            target_date_time = input(
                "Enter the date and time in the format (YYYY-MM-DD HH:MM:SS): ")

            if choice == '1':
                temperature = get_temperature(data, target_date_time)
                if temperature is not None:
                    print(
                        "Temperature at {target_date_time}: {temperature} K")
                else:
                    print("No data available for the given date and time.")

            elif choice == '2':
                wind_speed = get_wind_speed(data, target_date_time)
                if wind_speed is not None:
                    print(
                        f"Wind Speed at {target_date_time}: {wind_speed} m/s")
                else:
                    print("No data available for the given date and time.")

            elif choice == '3':
                pressure = get_pressure(data, target_date_time)
                if pressure is not None:
                    print(f"Pressure at {target_date_time}: {pressure} hPa")
                else:
                    print("No data available for the given date and time.")
        else:
            print("Invalid choice. Please enter a valid option.")


def get_weather_data():
    response = requests.get(API_URL)
    data = response.json()
    return data


def get_temperature(data, target_date_time):
    for entry in data['list']:
        if entry['dt_txt'] == target_date_time:
            return entry['main']['temp']
    return None


def get_wind_speed(data, target_date_time):
    for entry in data['list']:
        if entry['dt_txt'] == target_date_time:
            return entry['wind']['speed']
    return None


def get_pressure(data, target_date_time):
    for entry in data['list']:
        if entry['dt_txt'] == target_date_time:
            return entry['main']['pressure']
    return None


if __name__ == "__main__":
    main()
