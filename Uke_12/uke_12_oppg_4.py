def read_first_col(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        first_col = []
        for line in lines:
            first_col.append(line.split(' ')[0])
    return "\n".join(first_col)

print(read_first_col("2019-06-01_Oslo.csv"))