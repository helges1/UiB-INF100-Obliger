weather_stations = {
    "Bergen" : {
        "Wind speed": 3.6,
        "Wind direction": "northeast",
        "Precipitation": 5.2,
        "Device": "WeatherMaster500"
    },
    "Trondheim" : {
        "Wind speed": 8.2,
        "Wind direction": "northwest",
        "Precipitation": 0.2,
        "Device": "ClimateDiscoverer3000"
    },
    "Svalbard" : {
        "Wind speed": 7.5,
        "Wind direction": "southwest",
        "Precipitation": 1.1,
        "Device": "WeatherFinder5.0"
    },
}

ant = len(weather_stations)
count = 0

while count < ant:
    sted = list(weather_stations.keys())[count]
    vind = weather_stations[sted]["Wind speed"]
    rettning = weather_stations[sted]["Wind direction"]
    nedbør = weather_stations[sted]["Precipitation"]
    enhet = weather_stations[sted]["Device"]
    
    print(f"The weather in {sted}:")
    print(f"The wind speed is {vind} m/s in the {rettning} direction and the precipitation is {nedbør} mm.")
    print(f"The measurement was done using the {enhet} weather station.")

    if count+1 < ant:
        print()
    else:
        break
    
    count += 1
