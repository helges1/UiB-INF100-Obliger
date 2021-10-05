def calibration_readout(verdier):

    for index, temp in enumerate(verdier):

        indeks = index % 12

        if indeks == 0: 
            verdier[index] = "Calibration hour", temp
                    
    return (verdier)
            
# print(calibration_readout([3.0, 3.2, 3.3, 3.2, 3.0, 3.1, 3.5, 5.0, 5.0, 4.9, 4.0, 3.0, 2.9, 2.2]))