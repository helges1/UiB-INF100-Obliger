def r_w_file(infile, outfile):

    with open(infile, encoding="utf8") as f:
        temp_day = []
        new_temp_day = []
        

        for line in f:
            day, temp = line.split()
            temp_day.append((temp, day))
            
        count = 0

        while count < len(temp_day):
            
            if float(temp_day[count][0]) >= 23.5:
                new_temp_day.append(temp_day[count])
            
            count += 1
    
    with open(outfile, "w", encoding="utf8") as f:
        for i in range(len(new_temp_day)):
            f.write(f"{new_temp_day[i][1]} {new_temp_day[i][0]}\n")

#r_w_file("temperatures.txt", "x")