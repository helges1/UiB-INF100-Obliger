# IO-part (placing the data into a data structure)
# =====================================================

with open("temperatures.txt", encoding="utf8") as f:
    temp_day = []
    for line in f:
        day, temp = line.split()
        temp_day.append((temp, day))

# =====================================================

# data processing/analysis
# =====================================================

# this will sort according to ascending temperature
temp_day.sort()
# print(temp_day)

# =====================================================


# IO-part (presenting the results)
# =====================================================

# day with the lowest temperature
print(
    f"The coldest day was {temp_day[0][1]} with a temperature of {temp_day[0][0]} °C."
)

# day with the highest temperature
print(
    f"The warmest day was {temp_day[-1][1]} with a temperature of {temp_day[-1][0]} °C."
)

# =====================================================
