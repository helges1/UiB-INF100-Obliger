def update_weather(verdier):
    float_tuple = tuple(map(float, verdier.split()))
    return float_tuple

# print(update_weather(("16.1 14.1 13.3 15.0 13.0 13.2 12.9")))

def tuesday_weather(verdier):
    tirsdag = verdier[1]
    return tirsdag

# print(tuesday_weather((16.1, 14.1, 13.3, 15.0, 13.0, 13.2, 12.9)))