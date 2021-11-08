def write_to_csv(filename, rows):
    with open(filename, 'w') as f:
        for row in rows:
            row = [str(value) for value in row]
            f.write(','.join(row) + '\n')

# rows = [
#       ["Come Together", 4, 20, "Lennon/McCartney"],
#       ["Something", 3, 3, "Harrison"],
#       ["Maxwell's Silver Hammer", 3, 27, "Lennon/McCartney"],
#       ["Oh! Darling", 3, 26, "Lennon/McCartney"],
#       ["Octopus's Garden", 2, 51, "Starr"],
#       ["I want you", 7, 47, "Lennon/McCartney"],
#   ]

# write_to_csv("Abbey_Road.csv", rows)